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

# architecture
