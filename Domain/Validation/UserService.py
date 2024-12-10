from werkzeug.security import check_password_hash

from Domain.Database.AuthenticationDatabaseService import AuthenticationDatabaseService
from Domain.Validation.MailValidationService import MailValidationService


class UserService:
    def __init__(self):
        self.database_service = AuthenticationDatabaseService()
        self.mail_validator = MailValidationService()

    def validate(self, username, password):
        pw_from_database = self.database_service.get_user_password(username)
        return check_password_hash(pw_from_database, password)

    def create_user(self, username, password, mail):
        self.mail_validator.validate_email(mail)

        if not password or not username or len(password) <= 8:
            raise TypeError('password or username is invalid. Password should have 8 characters minimum')

        if username in self.database_service.get_all_usernames():
            raise KeyError(f'{username} already exists')

        self.database_service.create_user(username, password, mail)
