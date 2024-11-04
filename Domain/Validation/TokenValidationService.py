from functools import wraps

import jwt
from flask import request, jsonify
from jwt import InvalidSignatureError

SECRET_KEY_USER = 'secret_key_USER'
SECRET_KEY_ADMIN = 'secret_key_ADMIN'

def _is_token_valid(SECRET_KEY):
    token = request.headers.get('Authorization')
    if not token:
        return False

    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True

    except InvalidSignatureError or jwt.ExpiredSignatureError or jwt.InvalidTokenError or jwt.exceptions.InvalidSignatureError as e:
        return False


def user_token_required(f):
    """Decorator to ensure token is present and valid for protected routes."""
    @wraps(f)
    def decorated(*args, **kwargs):

        if not _is_token_valid(SECRET_KEY_USER):
            # admin should have access to all user routes
            if not _is_token_valid(SECRET_KEY_ADMIN):
                return jsonify({"message": "Token invalid or expired"}), 401

        return f(*args, **kwargs)
    return decorated

def admin_token_required(f):
    """Decorator to ensure token is present and valid for protected routes."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not _is_token_valid(SECRET_KEY_ADMIN):
            return jsonify({"message": "Token invalid or expired"}), 401

        return f(*args, **kwargs)
    return decorated