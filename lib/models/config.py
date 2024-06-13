import sqlite3 #importing the inbuilt sqlite3 to help me build a db connection

DATABASE_NAME = './db/bank.db' #variable that carries the name of my db

def get_db_connection():
    # function to establish a db connection
    conn = sqlite3.connect(DATABASE_NAME) #making a connection to the db
    return conn #returning the connection
