# ai-dscubed-wk1
tool calling chatbot project

as of 21:30 pm, there's:
- calculator and the datetime tools
- CLI with Rich

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

# make new tools
how to make a new tool from what I've learned:
- get some external libraries 
- make a class in the base_class 
- make the get_tool registry
- in main.py:
    - make the schema
    - register it 
    - put it in message and tool list
    - put in if response_message.tool_calls
