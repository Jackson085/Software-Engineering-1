from flask import request, jsonify, Blueprint

from Domain.Validation.TokenGenerationService import create_token_for_user, create_token_for_admin
from Domain.Validation.TokenValidationService import user_token_required, admin_token_required
from Domain.Validation.ValidationService import ValidationService

validation_service = ValidationService()

login_app_bp = Blueprint('login', __name__)


@login_app_bp.route('/login', methods=['POST'])
def login():
    """
    User or Admin Login
    ---
    tags:
      - Authentication
    parameters:
      - name: auth
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: user
              description: Username for the user or admin
            password:
              type: string
              example: user
              description: Password for the user or admin
    responses:
      200:
        description: Token generated successfully
        schema:
          type: object
          properties:
            token:
              type: string
              description: JWT token for future authentication
      400:
        description: Username and password required
      401:
        description: Invalid credentials
    """
    auth = request.get_json()
    if not auth or not auth.get("username") or not auth.get("password"):
        return jsonify({"message": "Username and password required"}), 400

    username = auth.get("username")
    password = auth.get("password")

    if validation_service.validate_user(username, password):
        user_token = create_token_for_user(username)
        return jsonify({"token": user_token}), 200

    if validation_service.validate_admin(username, password):
        token = create_token_for_admin(username)

        return jsonify({"token": token}), 200

    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Sample protected route
@login_app_bp.route('/protected/user', methods=['GET'])
@user_token_required
def protected_user():
    """
    Protected User Route just for testing
    ---
    tags:
      - Protected Routes
    summary: Access protected user route
    description: This endpoint requires a valid JWT token in the Authorization header.
    parameters:
      - name: Authorization
        in: header
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              description: JWT token for authentication. Format Bearer {token}
    responses:
      200:
        description: Access granted to protected user route
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Access granted"
      401:
        description: Token missing, invalid, or expired
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Token missing, invalid, or expired"
    """
    return jsonify({"message": "Access granted to protected route"}), 200

@login_app_bp.route('/protected/admin', methods=['GET'])
@admin_token_required
def protected_admin():
    """
    Protected Admin Route just for testing
    ---
    tags:
      - Protected Routes
    summary: Access protected admin route
    description: This endpoint requires a valid JWT token in the Authorization header.
    parameters:
      - name: Authorization
        in: header
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              description: JWT token for authentication. Format Bearer {token}
    responses:
      200:
        description: Access granted to protected user route
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Access granted"
      401:
        description: Token missing, invalid, or expired
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Token missing, invalid, or expired"
    """
    return jsonify({"message": "Access granted to protected route"}), 200