from langchain_core.messages import AIMessage, HumanMessage
from src.chains.itinerary import ItineraryChain
from src.utils import logger
from src.utils.logger import get_logger
from src.utils.custom_exception import CustomException

logger = get_logger(__name__)

class Planner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itinerary = ""
        logger.info(f"Initialized travel planner instance.")

    def set_city(self, city: str):
        try :
            self.city = city
            self.messages.append(HumanMessage(content=f"City set to: {city}"))
            logger.info(f"Set city to: {city}")
        except Exception as e:
            logger.error(f"Error occurred while setting city: {e}")
            raise CustomException("Failed to set city") from e
        
    def set_interests(self, interests: list[str]):
        try:
            self.interests = [interest.strip() for interest in interests]
            self.messages.append(HumanMessage(content=f"Interests set to: {interests}"))
            logger.info(f"Set interests to: {interests}")
        except Exception as e:
            logger.error(f"Error occurred while setting interests: {e}")
            raise CustomException("Failed to set interests") from e
        
    def generate_itinerary(self):
        try:
            itinerary_chain = ItineraryChain()
            self.itinerary = itinerary_chain.generate_itinerary(self.city, self.interests)
            self.messages.append(AIMessage(content=f"Generated itinerary for {self.city} with interests {self.interests}"))
            logger.info(f"Generated itinerary for city: {self.city} with interests: {self.interests}")
            return self.itinerary
        except Exception as e:
            logger.error(f"Error occurred while generating itinerary: {e}")
            raise CustomException("Failed to generate itinerary") from e
