from services.connect import create_conn


def get_best_coffee(userid):
    best_coffee = ''

    try:
        conn = create_conn()

        query = f'''
            SELECT c1 from UserCoffee
            WHERE UserId='{userid}'
        '''

        result = conn.execute(query).fetchone()
        best_coffee = result[0]

        conn.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise 'Connection error'

    return best_coffee
