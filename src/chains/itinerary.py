from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import Config

class ItineraryChain:
    def __init__(self):
        self.groq_client = ChatGroq(api_key=Config.GROQ_API_KEY, model="llama-3.3-70b-versatile", temperature=0.3)

    def itinerary_prompt(self, city:str, interests:list[str]):
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", "You are a travel agent that creates personalized travel itineraries based on user interests. Give the response in bullet points."),
            ("human", "Create a 1-day itinerary for a trip to {city} that includes activities related to the following interests: {interests}. Provide a brief description for each activity and suggest local dining options nearby.")
        ])
        return prompt_template.invoke({"city": city, "interests": ", ".join(interests)})

    def generate_itinerary(self, city:str, interests:list[str]) -> str:
        response = self.groq_client.invoke(
            self.itinerary_prompt(city, interests)
        )
        return response.content
