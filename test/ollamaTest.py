from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

# 1. Define custom tools for the agent
@tool
def get_current_time() -> str:
    """Returns the current local time."""
    from datetime import datetime
    return datetime.now().isoformat()

# 2. Load the local Ollama model (must support tool calling)
llm = ChatOllama(model="qwen3.5:4b", temperature=0)

tools = [get_current_time]

# 3. Create a ReAct (Reasoning and Acting) agent
agent_executor = create_react_agent(llm, tools)

# 4. Invoke the agent
response = agent_executor.invoke({
    "messages": [("user", "What time is it right now?")]
})
print(response["messages"][-1].content)
