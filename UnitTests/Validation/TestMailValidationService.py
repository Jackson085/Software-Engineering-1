import unittest
from unittest.mock import patch
import dns.resolver

from Domain.Validation.MailValidationService import MailValidationService


class TestMailValidationService(unittest.TestCase):

    def setUp(self):
        self.mail_service = MailValidationService()

    def test_valid_email(self):
        email = "test@example.com"

        with patch('dns.resolver.resolve') as mock_resolve:
            mock_resolve.return_value = ['mx.example.com']  # Simulate MX record found
            try:
                self.mail_service.validate_email(email)
                result = "Valid email"
            except TypeError as e:
                result = str(e)

        self.assertEqual(result, "Valid email")

    def test_invalid_email_format(self):
        email = "invalid-email.com"

        with patch('dns.resolver.resolve'):
            with self.assertRaises(TypeError) as context:
                self.mail_service.validate_email(email)

        self.assertEqual(str(context.exception), "Invalid email format")

    def test_invalid_domain(self):
        email = "test@invalid-domain.com"

        with patch('dns.resolver.resolve') as mock_resolve:
            mock_resolve.side_effect = dns.resolver.NoAnswer  # Simulate no MX record
            with self.assertRaises(TypeError) as context:
                self.mail_service.validate_email(email)

        self.assertEqual(str(context.exception), "Domain does not have valid MX records")

    def test_missing_at_symbol(self):
        email = "missingatsign.com"

        with patch('dns.resolver.resolve'):
            with self.assertRaises(TypeError) as context:
                self.mail_service.validate_email(email)

        self.assertEqual(str(context.exception), "Invalid email format")

    def test_valid_email_with_mx_check(self):
        email = "test@valid-domain.com"

        with patch('dns.resolver.resolve') as mock_resolve:
            mock_resolve.return_value = ['mx.valid-domain.com']  # Simulate MX record found
            self.mail_service.validate_email(email)

        mock_resolve.assert_called_with('valid-domain.com', 'MX')

    def test_invalid_email_with_no_mx(self):
        email = "test@invalid-domain.com"

        with patch('dns.resolver.resolve') as mock_resolve:
            mock_resolve.side_effect = dns.resolver.NoAnswer  # Simulate no MX record
            with self.assertRaises(TypeError) as context:
                self.mail_service.validate_email(email)

        self.assertEqual(str(context.exception), "Domain does not have valid MX records")


if __name__ == "__main__":
    unittest.main()