from Domain.Database.DatabaseService import DatabaseService
from werkzeug.security import check_password_hash


class ValidationService:
    def __init__(self):
        self.database_service = DatabaseService()

    def validate_user(self, username, password):
        pw_from_database = self.database_service.get_user_password(username)
        return check_password_hash(pw_from_database, password)

    def validate_admin(self, username, password):
        pw_from_database = self.database_service.get_admin_password(username)
        return check_password_hash(pw_from_database, password)