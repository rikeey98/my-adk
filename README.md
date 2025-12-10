# Google ADK App

A basic Python application using Google's Agent Development Kit (ADK) to create AI agents with tools.

## Overview

This project demonstrates how to build a simple AI agent using Google's Agent Development Kit. The agent includes basic calculator tools and can process natural language requests.

## Prerequisites

- Python 3.11 or higher
- UV package manager
- API key for your LLM provider (OpenAI, Azure, Anthropic, etc.)

## Installation

1. Clone the repository
2. Install dependencies:

```bash
uv sync
```

## Configuration

This application uses LiteLLM to support OpenAI-compatible models. Create a `.env` file in the project root:

1. Copy the example file:
```bash
cp .env.example .env
```

2. Edit `.env` and configure your settings:
```bash
MODEL=gpt-3.5-turbo                    # Your model name
LLM_ENDPOINT=https://api.openai.com/v1  # API endpoint
LLM_KEY=your-api-key-here              # Your API key
```

Supported providers include OpenAI, Azure OpenAI, Anthropic Claude, and any OpenAI-compatible endpoint.

## Usage

### Option 1: Web UI (Recommended)

Run the interactive browser-based development UI:

```bash
uv run adk web agents
```

This will start a FastAPI server at `http://localhost:8000` with a rich web interface featuring:
- Agent selection
- Chat interface
- Event inspection
- Trace visualization

**Note**: The Web UI is designed for development and debugging purposes only.

### Option 2: Command Line

Run the simple CLI version:

```bash
uv run main.py
```

### Option 3: Interactive CLI Agent

Run the agent in interactive CLI mode:

```bash
uv run adk run agents/calculator_agent
```

## Available Tools

The calculator agent includes the following tools:
- `add_numbers`: Add two numbers together
- `multiply_numbers`: Multiply two numbers together
- `subtract_numbers`: Subtract two numbers
- `divide_numbers`: Divide two numbers

## Project Structure

```
.
├── agents/                      # Agent directory for adk web
│   ├── agent.py                 # Root agent using LlmAgent
│   └── calculator_agent/        # Calculator agent
│       ├── __init__.py          # Package initialization (exports root_agent)
│       └── agent.py             # Calculator-specific agent with arithmetic tools
├── main.py                      # CLI version of the agent
├── pyproject.toml               # Project configuration and dependencies
├── .env.example                 # Environment variables template
├── README.md                    # This file
└── .python-version              # Python version specification
```

## Features

- Google ADK integration with LiteLLM using LlmAgent
- Multi-tool agent support
- OpenAI-compatible model support (OpenAI, Azure, Anthropic, etc.)
- Environment-based configuration (.env file)
- Interactive browser-based development UI (adk web)
- Modular agent structure (root agent + specialized agents)
- Calculator agent with 4 arithmetic operations (add, multiply, subtract, divide)

## Resources

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google ADK Python GitHub](https://github.com/google/adk-python)
- [ADK Web UI GitHub](https://github.com/google/adk-web)
- [PyPI Package](https://pypi.org/project/google-adk/)

## License

MIT
