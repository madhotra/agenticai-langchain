from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import OpenAI, ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_tavily import TavilySearch

load_dotenv()


class Source(BaseModel):
    """Schema for a source used by agent"""

    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Scheme for agent response with answer and sources"""

    answer:str = Field(description="The agent's answer to the wuery")
    source:List[Source] = Field(default_factory=List, description="The list of sources used to generate the answer")

llm = ChatOpenAI(model="gpt-5")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for an AI engineer using langchain in Toronto on linkedin and list their details.")})
    print(result)


        
if __name__ == "__main__":
    main()
