#Structured outputs in ADK

This example demonstrates how to implement structured outputs in ADK using Pydantic models. 

These are the different options:
- input_schema: Defina a pydantic BaseModel class representing the expected input structure. (Stay away from this)
- output_schema: Define a Pydantic BaseModel class representing the desired output structure.

    constraint: Using output_schema enables controlled generation within the LLM but disables agent's ability to use tools or transfer control to other agents
- output_key: Provide a string key. If set, the text content of agent's final repsonse will be automatically saved to session's state dictionary under this key (e.g., session_state[output_key] = agent_response_text). Useful for passing results between agents or steps in workflow. 
##
What are Structured outputs?
