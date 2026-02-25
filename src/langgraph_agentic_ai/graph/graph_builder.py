from langgraph.graph import StateGraph, START, END
from src.langgraph_agentic_ai.state.state import State
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode
import streamlit as st
from src.langgraph_agentic_ai.tools.search_tool import get_tools, create_tool_node    
from langgraph.prebuilt import ToolNode, tools_condition
from src.langgraph_agentic_ai.nodes.chatbot_with_tool_node import ChatBotWithToolNode   

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
        st.write("GraphBuilder initialized with model")  # Debugging line to check model initialization


    def basic_chat_build_graph(self):
        """
        Build a basic chat graph with LLM node.
        This method initializes a chatbot node using the `BasicChatbotNode` class and adds it to the graph. 
        The chatbot node is configured to use the specified LLM model for generating responses. 
        The chatbot node is set as both the entry and exit point of the graph.
        """
       
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        st.write("Basic chat graph built successfully")  # Debugging line to confirm graph construction
        return self.graph_builder
    

    def chatbot_with_tools_build_graph(self):
        """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbox graph that includes both a chatbot node and tool node.
        It defines tools, initializes that chatbot with tool capabilities, and set up conditional and direct edges between nodes.
        The chatbot node is set as the entry point.
        """
        # Define tools and initialize chatbot with tool capabilities
        tools = get_tools()
        tool_node = create_tool_node(tools)
        # Add nodes and edges to the graph
        llm = self.llm

        obj_chatbot_with_node = ChatBotWithToolNode(llm)
        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        # Define edges between nodes
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)  # Direct edge to END if no tools are used


    
    def setup_graph(self, usecase:str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chat_build_graph()
        if usecase == "Chatbot with Web":
            self.chatbot_with_tools_build_graph()
        else:
            raise ValueError(f"Unsupported use case: {usecase}")        
        
        return self.graph_builder.compile()