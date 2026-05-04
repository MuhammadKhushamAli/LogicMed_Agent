import firebase_admin
from firebase_admin import credentials, firestore_async
from google.cloud.firestore_v1.base_query import FieldFilter, Or
import os
import json


class Firestore:
    def __init__(self):
        credentials_firebase_json = json.loads(os.getenv("FIREBASE_JSON"))
        credentials_firebase: any = credentials.Certificate(credentials_firebase_json)
        firebase_admin.initialize_app(credentials_firebase)
        self.firestore_db = firestore_async.client()
    
    async def get_user(self, user_id: str):
        response = await self.firestore_db.collection("users").document(user_id).get()
        return response.to_dict()
    
    async def get_user_appointments(self, user_id: str):
        response = await self.firestore_db.collection("appointments").where(
            filter=Or([
                FieldFilter("patientId", "==", user_id),
                FieldFilter("doctorId", "==", user_id)
            ])
        ).get()

        appointments = []
        for appointment in response:
            appointments.append(appointment.to_dict())
        
        return appointments
   
    async def get_user_messages(self, user_id: str):
        response = await self.firestore_db.collection("messages").where(
            filter=FieldFilter("senderId", "==", user_id)
        ).get()

        messages = []
        for message in response:
            messages.append(message.to_dict())
        
        return messages

    async def get_all_doctors(self):
        response = await self.firestore_db.collection("doctors").get()

        doctors = []
        for doctor in response:
            doctors.append(doctor.to_dict())
        
        return doctors


firestore_db: Firestore = Firestore()