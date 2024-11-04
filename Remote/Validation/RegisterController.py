from flask import Blueprint, request, jsonify

from Domain.Database.DatabaseService import DatabaseService

database_service = DatabaseService()

register_app_bp = Blueprint('register', __name__)

@register_app_bp.route('/register', methods=['POST'])
def register_user():
    """
    User Registration
    ---
    tags:
      - Authentication
    parameters:
      - name: registration_data
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: new_user
              description: Desired username for the new account
            password:
              type: string
              example: password123
              description: Desired password for the new account
    responses:
      201:
        description: User registered successfully
      400:
        description: Missing username or password
      409:
        description: User with this username already exists
    """
    data = request.get_json()
    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"message": "Username and password are required"}), 400

    username = data["username"]
    password = data["password"]

    try:
        database_service.create_user(username, password)
        return jsonify({"message": "registered successfully"}), 201

    except KeyError as ke:
        return jsonify({"message": ke.__str__()}), 409

    except Exception:
        return jsonify({"message": "Username and password are required"}), 400