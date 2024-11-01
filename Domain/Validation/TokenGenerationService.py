# Generate token if the credentials are valid
import datetime

import jwt

SECRET_KEY = 'secret_key'

def create_token_for_user(username, expiration_time=60):
    return jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_time)  # Token expiration time
    }, SECRET_KEY, algorithm="HS256")