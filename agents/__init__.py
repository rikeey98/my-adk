"""
Google ADK Agents Package

This package contains the root agent and specialized sub-agents.

Structure:
- root_agent: Main agent defined in agent.py
- calculator_agent: Sub-agent specialized for arithmetic operations
"""

from .agent import root_agent

__all__ = ["root_agent"]
