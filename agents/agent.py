"""
Root Agent using Google ADK with LiteLLM
This is the main agent that can be extended with various capabilities.
"""
import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm

# Load environment variables
load_dotenv()

# Load configuration from environment variables
model = os.getenv("MODEL", "gpt-3.5-turbo")
llm_endpoint = os.getenv("LLM_ENDPOINT", "https://api.openai.com/v1")
llm_key = os.getenv("LLM_KEY", "")

# Initialize LiteLLM model
llm = LiteLlm(
    model=model,
    api_base=llm_endpoint,
    api_key=llm_key,
)

# Create the root agent with LiteLLM
root_agent = LlmAgent(
    model=llm,
    name="root_agent",
    description="A general-purpose AI agent powered by LiteLLM, capable of handling various tasks and conversations.",
)
