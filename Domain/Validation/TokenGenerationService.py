# Generate token if the credentials are valid
import datetime

import jwt

SECRET_KEY_USER = 'secret_key_USER'
SECRET_KEY_ADMIN = 'secret_key_ADMIN'

def create_token_for_user(username, expiration_time=60):
    return jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_time)
    }, SECRET_KEY_USER, algorithm="HS256")

def create_token_for_admin(username, expiration_time=60):
    return jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_time)
    }, SECRET_KEY_ADMIN, algorithm="HS256")