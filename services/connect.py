import sqlite3
import os


def create_conn():
    db_connection = os.getenv("DB_NAME")
    conn = sqlite3.connect(db_connection)
    conn.execute("PRAGMA foreign_keys = ON")

    return conn
