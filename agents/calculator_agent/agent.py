"""
Calculator Agent using Google ADK with LiteLLM
This agent can perform basic arithmetic operations.
"""
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai.types import FunctionDeclaration

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


# Define function declarations for the tools
add_tool = FunctionDeclaration(
    name="add_numbers",
    description="Add two numbers together",
    parameters={
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number"},
            "b": {"type": "number", "description": "Second number"},
        },
        "required": ["a", "b"],
    },
)

multiply_tool = FunctionDeclaration(
    name="multiply_numbers",
    description="Multiply two numbers together",
    parameters={
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number"},
            "b": {"type": "number", "description": "Second number"},
        },
        "required": ["a", "b"],
    },
)

subtract_tool = FunctionDeclaration(
    name="subtract_numbers",
    description="Subtract the second number from the first number",
    parameters={
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "First number"},
            "b": {"type": "number", "description": "Second number to subtract"},
        },
        "required": ["a", "b"],
    },
)

divide_tool = FunctionDeclaration(
    name="divide_numbers",
    description="Divide the first number by the second number",
    parameters={
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "Numerator"},
            "b": {"type": "number", "description": "Denominator (cannot be zero)"},
        },
        "required": ["a", "b"],
    },
)

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
agent = Agent(
    model=llm,
    tools=[add_tool, multiply_tool, subtract_tool, divide_tool],
    name="Calculator Agent",
    description="A helpful calculator agent that can perform basic arithmetic operations including addition, subtraction, multiplication, and division.",
)
