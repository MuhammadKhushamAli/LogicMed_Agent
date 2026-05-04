from agents import Agent, Runner
from .agent_tools import get_user_data, get_user_appointments, get_user_messages

agent: Agent = Agent(
    name="Dr. LogicMed",
    model="gpt-3.5-turbo",
    instructions="You are a medical agent. Your name is Dr LogicMed. You have to help the user according to their questions and encourage them. You can call the tools to get the user data for context if needed. You can address the user to appointment if needed. You have to introduce you self on users first interaction with you.",
    tools=[
        get_user_data,
        get_user_appointments,
        get_user_messages
    ]
)


async def talk_to_chat_bot(query: str, user_id: str, prev_history_id: str | None):
    """You can ask any thing to the user"""

    response: Runner = await Runner.run(
        starting_agent=agent,
        input=query,
        context=user_id,
        previous_response_id=prev_history_id
    )


    return {
        "response":  response.final_output,
        "history_id": response.last_response_id
    }