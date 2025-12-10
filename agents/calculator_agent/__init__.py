"""Calculator agent package."""

from .agent import agent

# ADK Web UI looks for 'root_agent' by convention
root_agent = agent

__all__ = ["agent", "root_agent"]
