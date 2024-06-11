import sqlite3

DATABASE_NAME = './db/bank.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn
