from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="travel_agent",
    version="0.1.0",
    author="naveen",
    description="A travel agent application using LangChain",
    packages=find_packages(),
    install_requires=requirements,
)