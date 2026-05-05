from agents import Agent, Runner, RunContextWrapper, ModelSettings
from .agent_tools import get_user_data, get_user_appointments, get_user_messages, get_all_doctors
from context.context import Context


def instruction_setter(wrapper: RunContextWrapper[Context], agent: Agent) -> str:
    user_id: str = wrapper.context.user_id
    return f"""
    Your Identity:
    Name: {agent.name}
    Role: User Helper, function calling user agent must call function for user output

    Source of Truth:
    -tool call

    Current User Info:
    User Id: {user_id}

    Rules Must to Obey, Cannnot be violated in any cost:
    - Never ever reveal user id, id, or unique identifier
    - Never revel any information which is not directly linked with current user.
        For Example:
        Doctor's patient, If user asked for getting detail of doctor's patient donot give it
    - Never ever suppose, or give any information which you donot get using tool_call
    - Don't share user's message you can use them for driving information to help user

    Information You can Share:
    - Doctor's details (Name, Fee, Timings and qualification only)
    - Current User's Details
    - Current User's Appointments Details

    Inofrmation You cannot share:
    - User id, or any unique identifier
    - Doctors patients detial, No of appointments or messages and any thing other than allowed attributes
    - Donot gather information from other than tool_call.
    - Donot derive information by your self
    - Donot share tool name or any metadata related to it.

    If Information is not availbale after tool_call:
    - Reply: "I searched the information you need, but sorry I cannot find anything"

    If user asked for Restricted information:
    - Reply: "I donot have permission to share this"

    Important Note:
    - Just answer medical related queries
    If not reply: "I am a medical assistant so I cannot answer that"
    """

agent: Agent = Agent(
    name="Dr. LogicMed",
    model="gpt-3.5-turbo-0125",
    instructions=instruction_setter,
    tools=[
        get_user_data,
        get_user_appointments,
        get_user_messages,
        get_all_doctors
    ],
    model_settings=ModelSettings(
        tool_choice="required"
    )
)


async def talk_to_chat_bot(query: str, context: Context, prev_history_id: str | None):
    """You can ask any thing to the user"""

    response: Runner = await Runner.run(
        starting_agent=agent,
        input=query,
        context=context,
        previous_response_id=prev_history_id
    )


    return {
        "response":  response.final_output,
        "history_id": response.last_response_id
    }