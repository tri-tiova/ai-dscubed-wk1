""" using duck typing instead of abc """
import math
from datetime import datetime
import python_weather 

class Calculator:
    name = "calculator"
    description = "mathematical expression evaluation"

    def calculator(self, expression: str) -> str:
        """ to validate that the initial expression the user inputted 
        is safe and valid"""
        try:   
            result = eval(expression, {"__builtins__": {}}, math.__dict__)
            return "Result: " + str(result)

        except Exception as e:
            return "Error: " + str(e)
        
class DateTimeTool:
    name = "date_time"
    description = "date and time information"

    def date_time(self) -> str:
        """ to get the date and time """
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

class WeatherTool:
    name = "weather"
    description = "weather information for a given location"

    def weather(self, location: str) -> str:
        """ to get the weather for a given location """
        try:
            import asyncio
            import python_weather as pw
            
            async def get_weather_data():
                async with pw.Client(unit=pw.METRIC) as client:
                    weather = await client.get(location)
                    return f"Temperature: {weather.temperature}°C, {weather.description}"
            
            # Run the async function
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(get_weather_data())
            loop.close()
            return result
        except Exception as e:
            return f"Error getting weather for {location}: {str(e)}"
