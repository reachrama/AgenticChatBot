from pydantic import BaseModel
from typing_extensions import List, TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    Represents the structure of the state used in graph.
    """
    message: Annotated[List, add_messages]