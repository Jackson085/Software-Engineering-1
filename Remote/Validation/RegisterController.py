from flask import Blueprint, request, jsonify

from Domain.Validation.UserService import UserService

user_service = UserService()

register_app_bp = Blueprint('register', __name__)

@register_app_bp.route('/register', methods=['POST'])
def register_user():
    """
    User Registration
    ---
    tags:
      - Authentication
    summary: Register a new user
    description: Register a new user by providing a unique username and a password. Returns a success message if the user is registered, or an error if there are issues with the data provided.
    parameters:
      - name: user_data
        in: body
        required: true
        schema:
          type: object
          properties:
            username:
              type: string
              example: "new_user"
              description: "The unique username for the new user"
            password:
              type: string
              example: "secure_password"
              description: "The password for the new user"
    responses:
      201:
        description: User registered successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "registered successfully"
      400:
        description: Missing username or password
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Username and password are required"
      409:
        description: Username already exists
        schema:
          type: object
          properties:
            message:
              type: string
              example: "user: new_user already exists"
      500:
        description: Server error
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Internal server error message"
    """
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    try:
        user_service.create_user(username, password)
        return jsonify({"message": "registered successfully"}), 201

    except KeyError:
        return jsonify({"message": f'user: {username} already exists'}), 409

    except TypeError:
        return jsonify({"message": "Username and password are required"}), 400

    except Exception as e:
        return jsonify({"message": str(e)}), 500
