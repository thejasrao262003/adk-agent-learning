What will be covered?
- Types of tools
- How to Add tools to your agents
- Best Practice and Limitation
- Showtool calling in Action

Three types of tools in ADK:
- Function calling tools: Be used 99% of the time. 
    - Functions/Methods: So we create a function and ask the agent to call it.
    - Agents-as-Tools: Use another, potenially specialized agent as a tool for a parent agent. Multi agent system
    - Long running function tools: Out of scope of the courese.
- Build-In-Tools: Ready to use tools provided by framework for common tasks. Examples: Google search, Code execution etc
- This party tools: Integrate with third party like LangChain, CrewAI etc

Notes: Multiple tools cannot be used at a time in the single agent