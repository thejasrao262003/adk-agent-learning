# Sessions and State management in ADK

This example demonstrates how to create and manage stateful sessions in the ADK, enabling your agents to maintain context and remember user information across interactions

What we will be doing?
- Overview of Session, State and Runner in ADK
- Code review
- Run code

A session has a state and events
What is state?
- you can store all sorts of values in the form of a dictionary. 

Events are all the events that take place for the entire action to go through. It can include agent response, task calling etc.

So it can be said, that it stores message between us and agent

Different types of session:
- InMemorySession: Save session information in-memory. Once the program is stopped, we loose session info
- DatabaseSession: Store session informatioin in a databse. It is persistent
- VertexAISession: Store sessions in cloud (VertexAI - Google's AI cloud deployment platform)


example code:
from google.adk.sessions import InMemorySessionService, Session

temp_service = InMemorySessionService()
example_session: Session = temp_service.create_session(
    app_name="my_app",
    user_id="example_user",
    state={"initial_key": "initial_value"}
)

print(example_session.id)
print(example_session.app_name)
print(example_session.state)
print(example_session.user_id)
print(example_session.events)


Runner:
It is a collection of two pieces of information: Agents and Session

Agents: Runner knows what agents I have and which Agent does what.
Session: Runner wants access to message history and core components from Session to maintain the context

Ex:
User says what is the return policy for this business: 
So first the runner will see this is user Brandon using your user_id, 
Go to session get all sessions for user 123, get message history
Passes it to the agent
The agent takes message history as context, generates an answer and writtens the response.

