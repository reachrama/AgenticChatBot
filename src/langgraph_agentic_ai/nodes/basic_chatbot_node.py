

from src.langgraph_agentic_ai.state.state import State
import streamlit as st

class BasicChatbotNode:
    """
    A basic chatbot node that can be used in a LangGraph.
    This node will simply echo the user's input back to them.
    """
    def __init__(self, model: str):
        self.model = model

    def process(self, state:State) -> dict:
        """
        Process the input state and generates chat bot response.
        In this basic implementation, it simply echoes the input.
        """       
        st.write("BasicChatbotNode processing state:", state)  # Debugging line to check input state
        return {"message": self.model.invoke(state["message"])}