from services.connect import create_conn
from flask import request


def auth_limiter_function():
    auth = request.authorization
    lim_key = f'user_{auth.username}'
    return lim_key


def get_userid_from_credentials(username, password):
    user_id = -1

    try:
        conn = create_conn()

        query = f'''
            SELECT Id from Users
            WHERE Name='{username}' AND
            Pwd='{password}'
        '''

        result = conn.execute(query).fetchone()
        user_id = result[0]

        conn.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return user_id


def check_credentials(username, password):
    ide = get_userid_from_credentials(username, password)

    return ide


def auth_checker(auth):
    ide = check_credentials(auth.username, auth.password)

    if not auth or ide <= 0:
        return 0

    return ide  # user Id for the future
