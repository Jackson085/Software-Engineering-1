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
    description: Register a new user by providing a unique username, password (min 8 characters), and a valid email. Returns a success message if the user is registered, or an error message if there are issues with the provided data.
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
              description: "The unique username for the new user."
            password:
              type: string
              example: "secure_password"
              description: "The password for the new user (must be at least 8 characters long)."
            mail:
              type: string
              example: "new_user@example.com"
              description: "The email address for the new user (must be a valid email)."
    responses:
      201:
        description: User registered successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "User registered successfully"
      400:
        description: Invalid input (missing or invalid username, password, or email)
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Password or username is invalid. Password should have 8 characters minimum."
      409:
        description: Username already exists
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Username 'new_user' already exists"
      500:
        description: Server error
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Internal server error"
    """
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")
    mail = data.get("mail")

    try:
        user_service.create_user(username, password, mail)
        return jsonify({"message": "User registered successfully"}), 201

    except KeyError as e:
        return jsonify({"message": str(e)}), 409  # Conflict, e.g., username already exists
    except TypeError as e:
        return jsonify({"message": str(e)}), 400  # Invalid input (e.g., short password, invalid username)
    except ValueError as e:
        return jsonify({"message": str(e)}), 400  # Invalid email or other validation error
    except Exception as e:
        return jsonify({"message": "Internal server error", "error": str(e)}), 500  # Catch all unexpected errors
