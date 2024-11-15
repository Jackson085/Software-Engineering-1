import unittest
from unittest.mock import patch
from werkzeug.security import generate_password_hash

from Domain.Database.AuthenticationDatabaseService import AuthenticationDatabaseService
from Domain.Validation.UserService import UserService


class UserServiceTest(unittest.TestCase):
    def setUp(self):
        patcher = patch(f"{UserService.__module__}.{AuthenticationDatabaseService.__name__}")
        self.MockAuthDatabaseService = patcher.start()
        self.addCleanup(patcher.stop)

        self.user_service = UserService()
        self.mock_db_service_instance = self.MockAuthDatabaseService.return_value

    def test_validate_success(self):
        username = "testuser"
        password = "correct_password"
        hashed_password = generate_password_hash(password)
        self.mock_db_service_instance.get_user_password.return_value = hashed_password

        is_valid = self.user_service.validate(username, password)

        self.mock_db_service_instance.get_user_password.assert_called_once_with(username)
        self.assertTrue(is_valid)

    def test_validate_incorrect_password(self):
        username = "testuser"
        correct_password = "correct_password"
        incorrect_password = "wrong_password"
        hashed_password = generate_password_hash(correct_password)
        self.mock_db_service_instance.get_user_password.return_value = hashed_password

        is_valid = self.user_service.validate(username, incorrect_password)

        self.mock_db_service_instance.get_user_password.assert_called_once_with(username)
        self.assertFalse(is_valid)

    def test_validate_nonexistent_user(self):
        username = "nonexistent_user"
        password = "password"
        self.mock_db_service_instance.get_user_password.return_value = ""

        is_valid = self.user_service.validate(username, password)

        self.mock_db_service_instance.get_user_password.assert_called_once_with(username)
        self.assertFalse(is_valid)

    def test_create_user_success(self):
        username = "new_user"
        password = "valid_password"
        self.mock_db_service_instance.get_all_usernames.return_value = []

        self.user_service.create_user(username, password)

        self.mock_db_service_instance.get_all_usernames.assert_called_once()
        self.mock_db_service_instance.create_user.assert_called_once_with(username, password)

    def test_create_user_invalid_password(self):
        username = "new_user"
        password = "short"

        with self.assertRaises(TypeError) as context:
            self.user_service.create_user(username, password)
        self.assertEqual(str(context.exception), "password or username is invalid")

    def test_create_user_existing_username(self):
        username = "existing_user"
        password = "valid_password"
        self.mock_db_service_instance.get_all_usernames.return_value = ["existing_user"]

        with self.assertRaises(KeyError) as context:
            self.user_service.create_user(username, password)
        self.assertEqual(str(context.exception), "'existing_user already exists'")

    def test_create_user_empty_username(self):
        username = ""
        password = "valid_password"

        with self.assertRaises(TypeError) as context:
            self.user_service.create_user(username, password)
        self.assertEqual(str(context.exception), "password or username is invalid")


if __name__ == '__main__':
    unittest.main()
