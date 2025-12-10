"""
Basic Google ADK Agent Application
This is a simple example of using Google's Agent Development Kit (ADK)
with LiteLLM for OpenAI-compatible models
"""
import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai.types import Tool, FunctionDeclaration

# Load environment variables from .env file
load_dotenv()


# Define a simple calculator tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


def main():
    """Run the basic ADK agent with LiteLLM."""
    print("🤖 Starting Google ADK Agent with LiteLLM...\n")

    # Load configuration from environment variables
    model = os.getenv("MODEL")
    llm_endpoint = os.getenv("LLM_ENDPOINT")
    llm_key = os.getenv("LLM_KEY")

    # Validate required environment variables
    if not all([model, llm_endpoint, llm_key]):
        print("⚠️  Error: Missing required environment variables")
        print("Please create a .env file with the following variables:")
        print("  - MODEL: Model name (e.g., gpt-3.5-turbo)")
        print("  - LLM_ENDPOINT: API endpoint (e.g., https://api.openai.com/v1)")
        print("  - LLM_KEY: Your API key")
        print("\nSee .env.example for a template\n")
        return

    print(f"Model: {model}")
    print(f"Endpoint: {llm_endpoint}")
    print()

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

    # Create tools list
    tools = [add_tool, multiply_tool]

    # Initialize LiteLLM model
    llm = LiteLlm(
        model=model,
        api_base=llm_endpoint,
        api_key=llm_key,
    )

    # Create the agent with LiteLLM and tools
    agent = Agent(
        model=llm,
        tools=tools,
    )

    print("✅ Google ADK Agent initialized successfully!")
    print(f"Available tools: {', '.join([t.name for t in tools])}")
    print("\nExample usage:")
    print("  - What is 5 + 3?")
    print("  - Multiply 4 by 7")
    print("\nAgent is ready to process requests!\n")

    # Example interaction
    prompt = "What is 5 + 3?"
    print(f"User: {prompt}")

    # Generate response using the agent
    response = agent.run(prompt)

    print(f"Agent: {response}\n")


if __name__ == "__main__":
    main()
