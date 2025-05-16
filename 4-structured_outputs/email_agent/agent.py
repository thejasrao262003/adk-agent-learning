from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descritive"
        )
    body: str = Field(
        description="""The body of the email.
        Should be well-formatted with proper greeting, paragraphs, and signature"""
        )

root_agent = LlmAgent(
    name="email_agent",
    model="gemini-2.0-flash",
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
    - Suggest relevant attachments if applicable (empty list if none needed)
    - Email tone should match the purpose (formal for business, friendly for colleagues)
    - Keep emails concise but complete

    IMPORTANT: Your response MUST be valid JSON with the following format:
    {
        "subject": "Subject Line here",
        "body": "Email body here with proper paragraphs and formatting"
    }
    DO NOT include any explanatins or additional text outside the JSON response.
    """,
    description="Generates professional emails with structured subject and body",
    output_schema=EmailContent,
    output_key="email",
)


