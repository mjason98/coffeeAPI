import sqlite3
import os


def create_conn(path=None):
    db_connection = os.getenv("DB_NAME")

    if path:
        db_connection = os.path.join(path, db_connection)

    conn = sqlite3.connect(db_connection)
    conn.execute("PRAGMA foreign_keys = ON")

    return conn
