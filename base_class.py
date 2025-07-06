""" using duck typing instead of abc """
import math
from datetime import datetime

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
