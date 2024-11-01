from flask import Flask, request, jsonify
import jwt
import datetime

from Domain.Validation.TokenGenerationService import create_token_for_user
from Domain.Validation.TokenValidationService import token_required
from Domain.Validation.UserValidationService import validate_user

app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get("username") or not auth.get("password"):
        return jsonify({"message": "Username and password required"}), 400

    username = auth.get("username")
    password = auth.get("password")

    if validate_user(username, password):
        token = create_token_for_user(username)

        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# Sample protected route
@app.route('/protected', methods=['GET'])
@token_required
def protected():
    return jsonify({"message": "Access granted to protected route"}), 200


if __name__ == '__main__':
    app.run(debug=True)
