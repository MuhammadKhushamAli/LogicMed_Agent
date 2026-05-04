from pydantic import BaseModel, Field

class UserContext(BaseModel):
    user_id: str = Field(..., description="The unique identifier of the user")
    prev_history_id: str | None = Field(None, description="The ID of the previous conversation history, if any")
