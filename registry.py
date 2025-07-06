""" registry is sort of like a phonebook where you can store 
all your tools then look where it is for later """
from typing import Any

tool_registry: dict[str, Any] = {}
""" creates a global dictionary called tool_registry 
and dict[str, object] means that the there's str = name and object = tool 
(e.g. "calculator") """

def register_tool(name: str, tool_obj: Any):
    tool_registry[name] = tool_obj
""" you register the tool you want"""

def get_calculator(name: str) -> Any:
    return tool_registry.get(name)
""" this is the tool function for the calculator later used in main.py"""

def get_datetime(name: str) -> Any:
    return tool_registry.get(name)
""" this is the tool function for the date_time later used in main.py"""

def list_tools() -> list[str]:
    return list(tool_registry.keys())


