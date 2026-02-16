from langgraph.graph import StateGraph, START, END
from src.langgraph_agentic_ai.state.state import State
from src.langgraph_agentic_ai.nodes.basic_chatbot_node import BasicChatbotNode
import streamlit as st


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
    
    def setup_graph(self, usecase:str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chat_build_graph()
        else:
            raise ValueError(f"Unsupported use case: {usecase}")        
        
        return self.graph_builder.compile()