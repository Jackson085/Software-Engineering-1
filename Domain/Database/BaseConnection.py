from pymongo import MongoClient

class BaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.database = self.client['kunsthandel']