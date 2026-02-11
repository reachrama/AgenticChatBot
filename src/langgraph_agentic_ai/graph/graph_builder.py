from langgraph.graph import StateGraph, START, END
from src.langgraph_agentic_ai.state.state import State


class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)


    def basic_chat_build_graph(self):
        """
        Build a basic chat graph with LLM node.
        This method initializes a chatbot node using the `BasicChatbotNode` class and adds it to the graph. 
        The chatbot node is configured to use the specified LLM model for generating responses. 
        The chatbot node is set as both the entry and exit point of the graph.
        """
       
        self.graph_builder.add_node("chatbot","")
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

        return self.graph_builder