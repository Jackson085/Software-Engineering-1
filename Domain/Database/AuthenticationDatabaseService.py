from Domain.Database.BaseConnection import BaseConnection
from werkzeug.security import generate_password_hash

class AuthenticationDatabaseService(BaseConnection):
    def __init__(self):
        BaseConnection.__init__(self)

        self.user_collection = self.database['collection_user']
        self.admin_collection = self.database['collection_admin']

        self.user_collection.create_index("username", unique=True)
        
    # region user
    def get_all_usernames(self):
        return [user['username'] for user in self.user_collection.find({}, {"username": 1, "_id": 0})]

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

    @staticmethod
    def _create_account(collection, username, password):
        hashed_password = generate_password_hash(password)
        if collection.find_one({"username": username}):
            raise KeyError(f"Account with username {username} already exists.")

        collection.insert_one({
            "username": username,
            "password": hashed_password
        })

if __name__ == '__main__':
    a = AuthenticationDatabaseService()
    x = a.get_all_usernames()
    print(x)
