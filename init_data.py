from services.connect import create_conn
from dotenv import load_dotenv
import os


load_dotenv()


if __name__ == '__main__':
    username = os.getenv("DB_USER_NAME")
    userpwd = os.getenv("DB_USER_PWD")

    conn = create_conn()

    drop_table_query1 = "DROP TABLE IF EXISTS Users"
    drop_table_query2 = "DROP TABLE IF EXISTS UserCoffee"

    conn.execute(drop_table_query1)
    conn.execute(drop_table_query2)

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Users (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Pwd TEXT
            )
    '''

    conn.execute(create_table_query)

    insert_first_user = f'''
    INSERT INTO Users (Name, Pwd)
    VALUES ('{username}', '{userpwd}')
    '''

    conn.execute(insert_first_user)

    # First Coffee Info

    create_table_coffes = '''
    CREATE TABLE IF NOT EXISTS UserCoffee (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            UserId INTEGER,
            c1 VARCHAR(100),
            c2 VARCHAR(100),
            c3 VARCHAR(100),
            FOREIGN KEY (UserId) REFERENCES Users(Id)
            )
    '''

    conn.execute(create_table_coffes)

    insert_first_coffee = '''
    INSERT INTO UserCoffee (UserId, c1, c2, c3)
    VALUES (1, 'espresso', 'capuccino', 'latte')
    '''

    conn.execute(insert_first_coffee)

    conn.commit()
    conn.close()
