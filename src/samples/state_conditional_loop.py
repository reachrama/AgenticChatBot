from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    """
    Represents the structure of the state used in graph.
    """
    count: int


# Define nodes that operate on the shared state
def increment(state: State) -> dict:
    """
    A simple function to increment the count in the state.
    """
    new_count = state["count"] + 1  
    print(f"Current state in increment function: {state}, new count: {new_count}")  # Debugging line to check input state and new count
    return {"count": new_count}

def finish(state: State) -> dict:
    """
    A simple function to finish the graph execution.
    """
    print("Current state in finish function:", state)  # Debugging line to check input state
    return {"result": state["count"]} # No change, just pass through the count as result

# Router function to determine the next node based on the count value   
def route(state: State) -> dict:
    """
    A simple function to route the execution based on the count value.
    If count is less than 3, it will route back to increment, otherwise it will route to finish.
    """
    print("Current state in route function:", state)  # Debugging line to check input state
    if state["count"] < 3:
        return "increment"
    else:
        return "finish"
    

# Build the graph with multiple nodes
graph = StateGraph(State)
graph.add_node("increment", increment)  
graph.add_node("finish", finish)


# Define the execution order of the nodes
graph.set_entry_point("increment")
graph.add_conditional_edges(
    "increment",  # from this node
    route, {
        "increment": "increment",  # if route returns "increment", go back to increment
        "finish": "finish"           # if route returns "finish", go to finish
    } 
)  # Add conditional edges based on the route function
graph.add_edge("finish", END)

# Compile and execute the graph
app = graph.compile()   
result = app.invoke({"count": 0})
print(result)