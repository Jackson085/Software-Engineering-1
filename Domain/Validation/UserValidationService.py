USER_DATA = {
    "username": "user",
    "password": "user"
}


def validate_user(username, password):
    # todo
    return username == USER_DATA["username"] and password == USER_DATA["password"]