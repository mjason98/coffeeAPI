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


def get_top3_coffee(userid):
    best_coffee = ''

    try:
        conn = create_conn()

        query = f'''
            SELECT c1,c2,c3 from UserCoffee
            WHERE UserId='{userid}'
        '''

        result = conn.execute(query).fetchone()
        best_coffee = result

        conn.close()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise 'Connection error'

    return best_coffee


def set_top3_coffee(userid, list3):
    try:
        assert len(list3) == 3, 'the list of coffees most be of size 3'

        conn = create_conn()

        query = f'''
            UPDATE UserCoffee
            SET c1='{list3[0]}',c2='{list3[1]}',c3='{list3[2]}'
            WHERE UserId={userid}
        '''

        conn.execute(query)
        conn.commit()
        conn.close()
    except Exception as e:
        conn.rollback()
        print(f"An error occurred: {str(e)}")
        raise 'An error ocurred'
