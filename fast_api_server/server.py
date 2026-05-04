from fastapi import FastAPI, Query, Body
from .output_structure.output import Output
from .pydantic_model.user_context import UserContext
from agent.agent import talk_to_chat_bot

app: FastAPI = FastAPI()



@app.get("/")
async def root():
    return Output(status=200, response="Agent is on the Road")


@app.post("/talk")
async def talk_to_dr_logicmed(
    query: str = Query(..., description="The Query You want to ask to the agent"),
    user_id: UserContext = Body(..., description="The User Context"),
):
    response = await talk_to_chat_bot(query, user_id=user_id.user_id, prev_history_id = user_id.prev_history_id)

    return Output(status=200, response=response["response"], prev_history_id=response["history_id"])