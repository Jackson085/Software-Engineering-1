import os
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash


class DatabaseService:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['kunsthandel']
        self.user_collection = self.db['collection_user']
        self.admin_collection = self.db['collection_admin']

    # region user
    def create_user(self, username, password):
        return self._create_account(self.user_collection, username, password)

    def get_user_password(self, username):
        entry = (self.user_collection.find_one({"username": username}))
        if entry is not None and (key := "password") in entry.keys():
            return entry[key]
        return ""
    # endregion

    # region admin
    def create_admin(self, username, password):
        return self._create_account(self.admin_collection, username, password)

    def get_admin_password(self, username):
        entry = (self.user_collection.find_one({"username": username}))
        if entry is not None and (key := "password") in entry.keys():
            return entry[key]
        return ""

    # endregion
    def _create_account(self, collection, username, password):
        hashed_password = generate_password_hash(password)
        if collection.find_one({"username": username}):
            raise KeyError(f"Account with username {username} already exists.")

        collection.insert_one({
            "username": username,
            "password": hashed_password
        })