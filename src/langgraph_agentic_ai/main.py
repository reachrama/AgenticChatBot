import streamlit as st

from src.langgraph_agentic_ai.ui.streamlitui.load_ui import LoadStreamlitUI 

def load_langraph_agentic_ai_app():
    """
    Loads and runs the LangGraph Agentic AI application using Streamlit UI.
    This function initializes the UI, handles user interactions, and configures the LLM Model, sets up the 
    graph based on the selected use case, and displays the output while implemetting  excpetion handling
    for roubustness.
    """
    ui_loader = LoadStreamlitUI()
    user_controls = ui_loader.load_ui()

    if not user_controls:
        st.warning("Please select the required options to proceed.")
        return
    
    user_message = st.chat_input("Enter your message here:")

    return user_controls