from fastapi import FastAPI, Query, Body
from .output_structure.output import Output
from .pydantic_model.user_context import UserContext
from agent.agent import talk_to_chat_bot
from context.context import Context

app: FastAPI = FastAPI()



@app.get("/")
async def root():
    return Output(status=200, response="Agent is on the Road")


@app.post("/talk")
async def talk_to_dr_logicmed(
    query: str = Query(..., description="The Query You want to ask to the agent"),
    context: UserContext = Body(..., description="The User Context"),
):
    response = await talk_to_chat_bot(query, context=Context(user_id=context.user_id), prev_history_id = context.prev_history_id)

    return Output(status=200, response=response["response"], prev_history_id=response["history_id"])