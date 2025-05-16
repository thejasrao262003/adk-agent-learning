from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService, Session
from google.genai import types
from question_answering_agent import question_answering_agent
import uuid
load_dotenv()

session_service_stateful = InMemorySessionService()

initial_state = {
    "user_name": "Brandon",
    "user_preferences":"""
        I like to play Pickleball, Disc Gold and tennis.
        My favourite food is Sushi.
        My favourite TV show is Breaking Bad.
        Loves it when people like and subscribe to his youtube channel.
    """,
}

APP_NAME = "Brandon Bot"
USER_ID = "123"
SESSION_ID = str(uuid.uuid4())

stateful_session: Session = session_service_stateful.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state,
)

print("CREATED NEW SESSION:")
print(f"\tSession ID: {stateful_session.id}")

runner = Runner(
    agent=question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service_stateful,
)

new_message = types.Content(
    role="user", parts=[types.Part(text="What is Brandon's favourite TV show?")]
)

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message,
):
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"Final response: {event.content.parts[0].text}")


print("==== Session Event Exploration ====")
session = session_service_stateful.get_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
)

for key, value in session.state.items():
    print(f"{key}: {value}")

print("==== End of Session Exploration ====")