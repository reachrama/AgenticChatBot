import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage    
import json

class DisplayResult:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        st.write("DisplayResult initialized with usecase:", self.usecase, self.graph, self.user_message)  # Debugging line to check initialization
        

    def display_result_on_ui(self):
        st.write("Inside Dispaly Result on UI")
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        st.write("UseCase :" + usecase )
        st.write("user_message :" + self.user_message )
        st.write(self.graph)
        if usecase == "Basic Chatbot":
            
            for event in graph.stream({"messages" : ("user", user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        # st.markdown(f"**User:** {value['messages'][-1].content}")
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        # st.markdown(f"**Assistant:** {value['messages'][-1].content}")
                        st.write(value['messages'].content)


        elif usecase == "Chatbot with Web":
            # Prepare state and ivoke ther graph
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)
            for message in res["messages"]:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Started")
                        st.write(message.content)
                        st.write("Tool Call Ended")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)