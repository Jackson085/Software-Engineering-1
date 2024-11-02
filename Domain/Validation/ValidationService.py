USER_DATA = {
    "username": "user",
    "password": "user",
    "username_admin": "admin",
    "admin_password": "admin"
}

from werkzeug.security import generate_password_hash, check_password_hash
def validate_user(username, password):
    # todo
    return username == USER_DATA["username"] and password == USER_DATA["password"]

def validate_admin(username, password):
    # todo
    return username == USER_DATA["username_admin"] and password == USER_DATA["admin_password"]