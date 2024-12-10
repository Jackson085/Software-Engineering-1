import re
from email.utils import parseaddr

import dns.resolver


class MailValidationService:
    EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    @staticmethod
    def is_valid_format(email: str) -> bool:
        return bool(re.match(MailValidationService.EMAIL_REGEX, email))

    @staticmethod
    def is_valid_domain(email: str) -> bool:
        if '@' not in email:
            return False

        domain = email.split('@')[-1]
        try:
            dns.resolver.resolve(domain, 'MX')
            return True
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            return False

    def validate_email(self, email: str) -> None:
        email = parseaddr(email)[1]

        if not self.is_valid_format(email):
            raise TypeError("Invalid email format")

        if not self.is_valid_domain(email):
            raise TypeError("Domain does not have valid MX records")
