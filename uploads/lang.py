from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.tools import tool
import os
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
llm_client = ChatOpenAI(
    api_key=OPENROUTER_API_KEY,
    model="x-ai/grok-4.1-fast",
    base_url="https://openrouter.ai/api/v1",)

@tool
def get_weather(location: str) -> str:
    """Returns the current weather for a specific city or location."""
    return f"The weather in {location} is sunny and 25°C."

agent=create_agent(
    model=llm_client,
    tools=[get_weather],
    system_prompt=("you are a helpful assistant that selects exactly ONE tool to satisfy the user's request. ")
)



response = agent.invoke(
        {"messages": [{"role": "user", "content": "What is the weather like in London?"}]}
    )

for message in response["messages"]:
    print(f"{message.type.upper()}: {message.content}")