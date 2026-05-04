from agents import function_tool
from firebase.firebase import firestore_db
from typing import List, Dict


@function_tool
async def get_user_data(user_id: str) -> Dict:
    """
    It takes doctors and patients id and return the data of the user given in the database
    Params: user_id: str
    Output: Dict
    """
    return await firestore_db.get_user(user_id)

@function_tool()
async def get_user_appointments(user_id: str) -> List:
    """
    It takes doctors and patients id and return the appointments of the user given in the database
    Params: user_id: str
    Output: list
    """
    return await firestore_db.get_user_appointments(user_id)

@function_tool
async def get_user_messages(user_id: str) -> List:
    """
    It takes doctors and patients id and return the messages of the user with doctors given in the database
    Params: user_id: str
    Output: list
    """
    return await firestore_db.get_user_messages(user_id)

@function_tool
async def get_all_doctors() -> List:
    """
    It returns all the doctors in the database
    Output: List
    """
    return await firestore_db.get_all_doctors()