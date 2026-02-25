from src.langgraph_agentic_ai.state.state import State

class ChatBotWithToolNode:
    """
    Chatbot logic enhanced with tool integration
    """
    def __init__(self, model):
       self.llm = model


    def process(self, state: State) -> dict:
        """
        Process the input state and generate a response using the language model
        """
        # Extract relevant information from the state
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role": "user", "content": user_input}])

        #Simulate tool-specific logic
        tools_response = f"Tool response based on: {user_input}"
        return {"messages": [llm_response, tools_response]}

        # user_input = state.get('user_input', '')
        # tool_data = state.get('tool_data', {})
        
        # # Combine user input with tool data for context
        # combined_input = f"{user_input}\nTool Data: {tool_data}"
        
        # # Generate a response using the language model
        # response = self.llm.generate(combined_input)
        
        # return {"response": response}


    def create_chatbot(self, tools):
        """
        Create a chatbot node with tool integration
        """
        # This method can be expanded to create a more complex chatbot node that integrates tools
        llm_with_tools = self.llm.bind_tools(tools)
        def chatbot_node(state: State) -> dict:
            """Chatbot logic for processing the input state and returning a response"""
            return {"messages" : [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node