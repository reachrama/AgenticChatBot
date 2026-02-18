from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    """
    Represents the structure of the state used in graph.
    """
    count: int

def increment(state: State) -> dict:
    """
    A simple function to increment the count in the state.
    """
    print("Current state in increment function:", state)  # Debugging line to check input state
    return {"count": state["count"] + 1}


graph = StateGraph(State)
graph.add_node("increment", increment)
graph.set_entry_point("increment")
graph.add_edge("increment", "END")

app = graph.compile()
result = app.invoke({"count": 0})
print(result)


