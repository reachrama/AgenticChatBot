from pydantic import BaseModel
from typing_extensions import list, TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    Represents the structure of the state used in graph.
    """
    message: Annotated[list, add_messages]