"""
Calculator Agent using Google ADK with LiteLLM
This agent can perform basic arithmetic operations.
"""
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

# Load environment variables
load_dotenv()


# Define calculator tools
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
    return a * b


def subtract_numbers(a: float, b: float) -> float:
    """Subtract two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        The result of a - b
    """
    return a - b


def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers.

    Args:
        a: First number (numerator)
        b: Second number (denominator)

    Returns:
        The result of a / b

    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


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

# Create the agent with tools
# Google ADK automatically converts Python functions to tools using their docstrings and type hints
agent = Agent(
    model=llm,
    tools=[add_numbers, multiply_numbers, subtract_numbers, divide_numbers],
    name="calculator_agent",
    description="A helpful calculator agent that can perform basic arithmetic operations including addition, subtraction, multiplication, and division.",
)
