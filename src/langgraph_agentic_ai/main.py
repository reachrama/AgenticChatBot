import streamlit as st

from src.langgraph_agentic_ai.ui.streamlitui.load_ui import LoadStreamlitUI 
from src.langgraph_agentic_ai.LLMs.groq_llm import GroqLLM
from src.langgraph_agentic_ai.graph.graph_builder import GraphBuilder 
from src.langgraph_agentic_ai.ui.streamlitui.display_result import DisplayResult  

def load_langraph_agentic_ai_app():
    """
    Loads and runs the LangGraph Agentic AI application using Streamlit UI.
    This function initializes the UI, handles user interactions, and configures the LLM Model, sets up the 
    graph based on the selected use case, and displays the output while implemetting  excpetion handling
    for roubustness.
    """
    ui_loader = LoadStreamlitUI()
    user_controls = ui_loader.load_ui()
    st.write("*****User Controls:", user_controls)  # Debugging line to check user controls

    if not user_controls:
        st.warning("Please select the required options to proceed.")
        return
    
    user_message = st.chat_input("Enter your message here:")

    if user_message:
        try:
            st.write("User Message:", user_message)  # Debugging line to check user message
            obj_llm_config = GroqLLM(user_controls=user_controls)
            model= obj_llm_config.get_llm_model()


            if not model:
                st.error("Failed to initialize the LLM model. Please check your configuration.")
                return
            
            usecase = user_controls.get("selected_usecase")
            if not usecase:
                st.error("Please select a use case to proceed.")
                return
            
            # Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResult(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error building graph for use case '{usecase}': {e}")
                return

        except Exception as e:            
            st.error(f"An error occurred: {str(e)}")

    return user_controls