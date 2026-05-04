from agents import function_tool, RunContextWrapper
from firebase.firebase import firestore_db
from typing import Dict, Any


@function_tool
async def get_user_data(wrapper: RunContextWrapper[str]):
    """
    It takes user id and return the data of the user given in the database
    """
    return await firestore_db.get_user(wrapper.context)

@function_tool(strict_mode=False)
async def get_user_appointments(wrapper: RunContextWrapper[str]):
    """
    It takes user id and return the appointments of the user given in the database
    """
    return await firestore_db.get_user_appointments(wrapper.context)

@function_tool
async def get_user_messages(wrapper: RunContextWrapper[str]):
    """
    It takes user id and return the messages of the user with doctors given in the database
    """
    return await firestore_db.get_user_messages(wrapper.context)