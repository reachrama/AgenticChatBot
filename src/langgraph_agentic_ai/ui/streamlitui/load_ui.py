import streamlit as st
import os

from src.langgraph_agentic_ai.ui.ui_config_file import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())

        with st.sidebar:
            #Get options from Config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()            

            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)
            if self.user_controls["selected_llm"] == "Groq":
                groq_model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Groq Model", groq_model_options)
                self.user_controls["GROQ_API_KEY"] = st.text_input("Enter Groq API Key", type="password")
                # Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("Please enter your Groq API Key to use Groq models.")
        
            # Use Case Selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Use Case", usecase_options)
            
        return self.user_controls
    
        
        

