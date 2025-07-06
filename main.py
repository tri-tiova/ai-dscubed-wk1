# main.py
import os
import json
import math
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.panel import Panel
from datetime import datetime
from base_class import Calculator, DateTimeTool, WeatherTool
from registry import register_tool, get_calculator, get_datetime, get_weather

# This is for the API key, they'll validate it before continuing
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set OPENAI_API_KEY in your .env file")

client = OpenAI(api_key=api_key)
console = Console()

# === Define tool schema ===
calculator_schema = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "mathematical expression evaluation using a calculator tool",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "A math expression, like '2 + 3 * 5'"
                }
            },
            "required": ["expression"]
        }
    }
}

date_time_schema = {
    "type": "function",
    "function": {
        "name": "date_time",
        "description": "date and time information",
        "parameters": {
                "type": "object",
                "properties": {},
                "required": []
        }
    }
}

weather_schema = {
    "type": "function",
    "function": {
        "name": "weather",
        "description": "weather information for a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location to get weather information for"
                }
            },
            "required": ["location"]
        }
    }
}

# === Register tool ===
calculator = Calculator()
register_tool(calculator.name, calculator)

date_time = DateTimeTool()
register_tool(date_time.name, date_time)

weather = WeatherTool()
register_tool(weather.name, weather)

# === Start CLI loop ===
console.print(Panel("🤖 AI CLI Assistant — type 'exit' to quit", style="bold green"))

# Initialize chat history
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant. "
            "You can use tools like a calculator to solve math problems, "
            "and a datetime tool to tell the current date and time. "
            "Only call tools when needed."
        )
    }
]

while True:
    user_response = input(">>> ").strip()
    if user_response.lower() in {"exit", "quit"}:
        console.print(Panel("Goodbye!", style="bold red"))
        break

    # Add user message
    messages.append({"role": "user", "content": user_response})

    # Send to OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=[calculator_schema, date_time_schema, weather_schema],
        tool_choice="auto"
    )

    response_message = response.choices[0].message
    messages.append(response_message.model_dump())

    # === Handle tool call ===
    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)

            if name == "calculator":
                tool = get_calculator("calculator")
                result = tool.calculator(args["expression"])

                # Add result as tool response
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": name,
                    "content": result
                })
            
            elif name == "date_time":
                tool = get_datetime("date_time")
                result = tool.date_time()
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": name,
                    "content": result
                })

            elif name == "weather":
                tool = get_weather("weather")
                result = tool.weather(args["location"])
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": name,
                    "content": result
                })

        # Continue chat after tool result
        second_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        assistant_reply = second_response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_reply})
        console.print(Panel(assistant_reply, style="bold green"))

    else:
        # Direct response (no tool)
        assistant_reply = response_message.content
        console.print(Panel(assistant_reply, style="bold green"))
