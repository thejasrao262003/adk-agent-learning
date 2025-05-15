from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time() -> dict:
    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="A root agent that can use tools to search the web",
    tools=[google_search],
    instruction="""
    You are a helpful assistant that can use the following tools:
    - get_current_time
    - google_search
    """,
)

