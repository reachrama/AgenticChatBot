from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END

# 1. Define the shared state structure using TypedDict  
class State(TypedDict):
    """
    Represents the structure of the state used in graph.
    """
    count: int

# 2, Define nodes that operate on the shared state
def increment(state: State) -> dict:
    """
    A simple function to increment the count in the state.
    """
    print("Current state in increment function:", state)  # Debugging line to check input state
    return {"count": state["count"] + 1}

def double(state: State) -> dict:
    """
    A simple function to double the count in the state.
    """
    print("Current state in double function:", state)  # Debugging line to check input state
    return {"count": state["count"] * 2}    

def finish(state: State) -> dict:
    """
    A simple function to finish the graph execution.
    """
    print("Current state in finish function:", state)  # Debugging line to check input state
    return {"result": state["count"]} # No change, just pass through the count as result

# 3. Build the graph with multiple nodes
graph = StateGraph(State)
graph.add_node("increment", increment)
graph.add_node("double", double)
graph.add_node("finish", finish)

# Defin the execution order of the nodes
graph.set_entry_point("increment")
graph.add_edge("increment", "double")   
graph.add_edge("double", "finish")
graph.add_edge("finish", END)

# 4. Compile and execute the graph
app = graph.compile()
result = app.invoke({"count": 1})
print(result)
print(result["count"])