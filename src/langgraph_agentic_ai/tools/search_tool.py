from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """Defines and returns a list of tools to be used in the agentic AI graph."""
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """Creates and returns a ToolNode with the provided tools."""
    tool_node = ToolNode(tools=tools)
    return tool_node