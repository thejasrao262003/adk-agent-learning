# Structured Outputs in ADK

## Overview
This module demonstrates how to implement structured outputs in ADK using Pydantic models. Structured outputs enable you to define clear schemas for your agent's responses, ensuring type safety, validation, and consistent data formats. This is particularly useful for building reliable AI applications that need to integrate with other systems or maintain specific data structures.

## Key Concepts

### Structured Outputs
Structured outputs allow you to:
- Define clear response schemas
- Validate output data
- Ensure type safety
- Maintain consistent data formats
- Integrate with other systems

### Output Schema Options

1. **output_schema**
   - Define a Pydantic BaseModel class for the desired output structure
   - Enables controlled generation within the LLM
   - Disables agent's ability to use tools or transfer control to other agents
   - Best for simple, well-defined output structures

2. **output_key**
   - Provide a string key for storing the agent's response
   - Automatically saves text content to session's state dictionary
   - Useful for passing results between agents
   - Enables multi-step workflows

## Implementation Guide

### 1. Defining Output Schemas
```python
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive"
    )
    body: str = Field(
        description="""The body of the email.
        Should be well-formatted with proper greeting, paragraphs, and signature"""
    )
```

### 2. Creating an Agent with Structured Output
```python
from google.adk.agents import LlmAgent

email_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
    description="Generates professional emails with structured subject and body",
    instruction="""
    You are an expert email writer.
    You are given a task to write an email based on the user's request.
    - You should use the user's request to generate an email with a subject and body.
    These are the instructions:
    - Create an appropriate subject line
    - Write a well-structured email body with:
        * Professional greeting
        * Clear and concise main content
        * Appropriate closing
        * Your name as signature
    - Email tone should match the purpose (formal for business, friendly for colleagues)
    - Keep emails concise but complete

    IMPORTANT: Your response MUST be valid JSON with the following format:
    {
        "subject": "Subject Line here",
        "body": "Email body here with proper paragraphs and formatting"
    }
    DO NOT include any explanations or additional text outside the JSON response.
    """,
    output_schema=EmailContent,
    output_key="email"
)
```

### 3. Using Output Keys for State Management
```python
from google.adk.sessions import InMemorySessionService

session_service = InMemorySessionService()
session = session_service.create_session(
    app_name="email_app",
    user_id="user123",
    state={}
)

# The agent's response will be automatically stored in:
# session.state["email"]
```

## Best Practices

1. **Schema Design**
   - Keep schemas simple and focused
   - Use clear, descriptive field names
   - Provide detailed field descriptions
   - Include validation rules where appropriate

2. **Output Formatting**
   - Be explicit about expected formats
   - Include examples in instructions
   - Handle edge cases gracefully
   - Validate output before use

3. **Error Handling**
   - Implement proper validation
   - Handle malformed outputs
   - Provide clear error messages
   - Log validation failures

## Common Use Cases

1. **Data Extraction**
   - Form filling
   - Information parsing
   - Data classification
   - Entity recognition

2. **Content Generation**
   - Email composition
   - Report generation
   - Document creation
   - Code generation

3. **Multi-step Workflows**
   - Sequential processing
   - Data transformation
   - State management
   - Pipeline integration

## Limitations and Considerations

1. **Tool Usage**
   - Agents with output_schema cannot use tools
   - Consider using output_key for tool-enabled agents
   - Plan workflow accordingly

2. **Response Format**
   - Must match schema exactly
   - No additional text allowed
   - Strict validation rules
   - Clear formatting requirements

3. **Performance**
   - Schema validation overhead
   - Memory usage for complex schemas
   - Response time considerations
   - State management impact

## Troubleshooting

Common issues and solutions:

1. **Validation Errors**
   - Check schema definition
   - Verify field types
   - Review required fields
   - Test with sample data

2. **Format Issues**
   - Validate JSON structure
   - Check field names
   - Verify data types
   - Review formatting rules

3. **Integration Problems**
   - Test schema compatibility
   - Verify state management
   - Check data flow
   - Review error handling

## Additional Resources

- [ADK Documentation](https://developers.google.com/agent-development-kit)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Structured Output Best Practices](https://developers.google.com/agent-development-kit/docs/best-practices)
- [API Reference](https://developers.google.com/agent-development-kit/docs/api-reference)
