from agents import function_tool
from firebase.firebase import firestore_db


@function_tool
async def get_user_data(user_id: str):
    """
    It takes user id and return the data of the user given in the database
    """
    return await firestore_db.get_user(user_id)

@function_tool
async def get_user_appointments(user_id: str):
    """
    It takes user id and return the appointments of the user given in the database
    """
    return await firestore_db.get_user_appointments(user_id)

@function_tool
async def get_user_messages(user_id: str):
    """
    It takes user id and return the messages of the user with doctors given in the database
    """
    return await firestore_db.get_user_messages(user_id)