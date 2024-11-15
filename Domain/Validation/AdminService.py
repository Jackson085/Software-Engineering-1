from werkzeug.security import check_password_hash

from Domain.Database.AuthenticationDatabaseService import AuthenticationDatabaseService


class AdminService:
    def __init__(self):
        self.database_service = AuthenticationDatabaseService()

    def validate(self, username, password):
        pw_from_database = self.database_service.get_admin_password(username)
        return check_password_hash(pw_from_database, password)
