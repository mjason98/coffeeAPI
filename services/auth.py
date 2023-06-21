from services.connect import create_conn
from services.aws_sqs import send_message_to_query
import json


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


def add_user(username, pwd, email):
    try:
        conn = create_conn()

        query = f'''
            INSERT INTO Users (Name, Pwd, Email)
            VALUES ('{username}', '{pwd}', '{email}')
        '''

        conn.execute(query)
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        print(f"An error occurred: {str(e)}")
        raise 'An error ocurred'

    # send email query
    try:
        message = {'email': email, 'user': username}
        message = json.dumps(message)
        send_message_to_query(message)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
