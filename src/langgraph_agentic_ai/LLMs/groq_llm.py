import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls):
        self.user_controls = user_controls
        self.model_name = user_controls.get("selected_groq_model")
        self.api_key = user_controls.get("GROQ_API_KEY")
        self.client = None  


    def get_llm_model(self):
        if not self.api_key:
            st.error("Groq API Key is required to initialize the model.")
            return None
        
        try:
            self.client = ChatGroq(api_key=self.api_key, model=self.model_name)            
        except Exception as e:
            st.error(f"Error initializing Groq model: {e}")
            return ValueError(f"Error initializing Groq model: {e}")
        return self.client 