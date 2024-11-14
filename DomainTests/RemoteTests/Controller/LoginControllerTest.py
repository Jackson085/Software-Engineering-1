import unittest
from unittest.mock import patch

from flask import Flask

from Domain.Validation.AdminService import AdminService
from Domain.Validation.UserService import UserService
from Remote.Validation.LoginController import login_app_bp


class LoginControllerTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(login_app_bp)

        # Create test client
        self.client = self.app.test_client()

        # Mock the services
        patcher_user_service = patch.object(UserService, 'validate', return_value=True)
        patcher_admin_service = patch.object(AdminService, 'validate', return_value=True)
        patcher_create_token_for_user = patch('Domain.Validation.TokenGenerationService.create_token_for_user', return_value="user_token")
        patcher_create_token_for_admin = patch('Domain.Validation.TokenGenerationService.create_token_for_admin', return_value="admin_token")

        self.mock_user_service = patcher_user_service.start()
        self.mock_admin_service = patcher_admin_service.start()
        self.mock_create_token_for_user = patcher_create_token_for_user.start()
        self.mock_create_token_for_admin = patcher_create_token_for_admin.start()

        self.addCleanup(patcher_user_service.stop)
        self.addCleanup(patcher_admin_service.stop)
        self.addCleanup(patcher_create_token_for_user.stop)
        self.addCleanup(patcher_create_token_for_admin.stop)

    def test_login_missing_credentials(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Username and password required', response.get_json()['message'])

    def test_login_invalid_credentials(self):
        self.mock_user_service.return_value = False
        self.mock_admin_service.return_value = False

        response = self.client.post('/login', json={"username": "invalid_user", "password": "wrong_password"})
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid credentials', response.get_json()['message'])

    def test_login_success_user(self):
        self.mock_user_service.return_value = True
        self.mock_create_token_for_user.return_value = "user_token"

        response = self.client.post('/login', json={"username": "user", "password": "valid_password"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())

    def test_login_success_admin(self):
        self.mock_admin_service.return_value = True
        self.mock_create_token_for_admin.return_value = "admin_token"

        response = self.client.post('/login', json={"username": "admin", "password": "valid_password"})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())


if __name__ == '__main__':
    unittest.main()
