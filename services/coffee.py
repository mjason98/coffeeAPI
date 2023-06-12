from services.connect import create_conn


def get_best_coffee(userid):
    best_coffe = 'None'

    try:
        conn = create_conn()

        query = f'''
            SELECT Id from Users
            WHERE Name='{username}' AND
            Pwd='{password}'
        '''

        result = conn.execute(query)

        print(result)

        user_id = result[0]

        conn.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return user_id
