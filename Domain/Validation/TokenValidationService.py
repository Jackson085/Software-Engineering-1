from functools import wraps

import jwt
from flask import request, jsonify

SECRET_KEY_USER = 'secret_key_USER'
SECRET_KEY_ADMIN = 'secret_key_ADMIN'

def _decode_token(token, secret_key):
    try:
        if token is None:
            return None

        return jwt.decode(token, secret_key, algorithms=["HS256"])

    except jwt.ExpiredSignatureError or jwt.InvalidTokenError or jwt.exceptions.InvalidSignatureError:
        return None

def user_token_required(f):
    """Decorator to ensure token is present and valid for protected routes."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        claims = _decode_token(token, SECRET_KEY_USER)

        if not claims:
            # Allow admin tokens to access user routes
            claims = _decode_token(token, SECRET_KEY_ADMIN)

        if not claims:
            return jsonify({"message": "Token invalid or expired"}), 401

        return f(*args, username=claims["username"], **kwargs)
    return decorated

def admin_token_required(f):
    """Decorator to ensure token is present and valid for protected routes."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        claims = _decode_token(token, SECRET_KEY_USER)

        if not claims:
            return jsonify({"message": "Token invalid or expired"}), 401

        return f(*args, username=claims["username"], **kwargs)
    return decorated
