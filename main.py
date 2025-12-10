"""
Basic Google ADK Agent Application
This is a simple example of using Google's Agent Development Kit (ADK)
"""
import os
from google.adk.agents import Agent
from google.genai.client import Client
from google.genai.types import GenerateContentConfig, Tool, FunctionDeclaration


# Define a simple calculator tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


def main():
    """Run the basic ADK agent."""
    print("🤖 Starting Google ADK Agent...\n")

    # Initialize the Gemini client
    # Note: You need to set GOOGLE_API_KEY environment variable
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        print("⚠️  Warning: GOOGLE_API_KEY environment variable not set")
        print("To use this agent with Gemini, please set your API key:")
        print("export GOOGLE_API_KEY='your-api-key-here'\n")
        return

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

    # Create the agent with tools
    tools = Tool(function_declarations=[add_tool, multiply_tool])

    # Create agent configuration
    config = GenerateContentConfig(
        temperature=0.7,
        tools=[tools],
    )

    # Initialize the client
    client = Client(api_key=api_key)

    print("✅ Google ADK Agent initialized successfully!")
    print("Available tools: add_numbers, multiply_numbers")
    print("\nExample usage:")
    print("  - What is 5 + 3?")
    print("  - Multiply 4 by 7")
    print("\nAgent is ready to process requests!\n")

    # Example interaction
    prompt = "What is 5 + 3?"
    print(f"User: {prompt}")

    # Generate response using the agent
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp",
        contents=prompt,
        config=config,
    )

    print(f"Agent: {response.text}\n")


if __name__ == "__main__":
    main()
