# ai-dscubed-wk1
tool calling chatbot project

# quick start

1. **Clone and install dependencies:**
   ```bash
   pip install -r requires.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

3. **Run the chatbot:**
   ```bash
   python main.py
   ```
# available tools

1. **Calculator**
- function: mathematical expression evaluation
- example: "what's 2 + 2?"

2. **DateTimeTool**
- function: gives the current date and time
- example: "what's the time right now?"

3. **WeatherTool**
- function: gives the weather of an inputted city
- example" "what's the weather in Melbourne right now?"

# how to add new tools
it's messy right now but you can make a new tool by:
- get some (internal/external) libraries of the tool you want to make 
- make a class in the base_class 
- make the get_tool registry
- in main.py:
    - make the schema
    - register it 
    - put it in message and tool list
    - put in the response message statement

# current (attempted) architecture
'''
