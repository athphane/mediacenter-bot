import json

from pyrogram import Message
from mediacenter.database import database
from datetime import datetime


class Incident:
    def __init__(self):
        self.incidents = database()['incidents']

    def all_incidents(self):
        incidents = self.incidents.find()
        return incidents

    def find_latest_incident(self):
        return self.incidents.find().sort(
            'timestamp', -1
        ).limit(1)

    def create_incident(self, message: Message):
        data = {
            'user': {
                "id": message.chat.id,
                "first_name": message.chat.first_name,
                "last_name": message.chat.last_name,
                "username": message.chat.username,
            },
            'crime': message.text,
            'full_traceback': json.loads(str(message)),
            'timestamp': datetime.utcnow(),
        }

        return self.incidents.insert_one(data)

    def create_user_with_id(self, user_id):
        user = self.incidents.find_one({
            "id": int(user_id)
        })

        if user:
            return
        else:
            self.incidents.insert_one({
                "id": int(user_id),
            })

    def update_user(self, message: Message):
        query = {
            "id": message.chat.id,
        }

        data = {
            "f_name": message.chat.first_name,
            "l_name": message.chat.last_name,
            "username": message.chat.username,
        }

        new_values = {"$set": data}

        self.incidents.update_one(query, new_values)
        return self.find_user(message)

    def find_or_create(self, message: Message):
        user = self.find_user(message)

        if user is None:
            self.create_user(message)
            user = self.find_user(message)

        return user

    def update_state(self, message: Message, state):
        query = {
            "id": message.chat.id,
        }

        data = {
            "state": state,
        }

        new_values = {"$set": data}

        self.incidents.update_one(query, new_values)
