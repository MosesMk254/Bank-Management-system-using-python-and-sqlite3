from .config import get_db_connection # importing the db connection

def create_tables():
    # A function to create a table
    conn = get_db_connection() # get db connection
    cursor = conn.cursor()  #creating a cursor object to execute sql commmands
    
    # executing an sql command to create accounts table if it does not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number INTEGER,
            account_balance INTEGER,
            account_type TEXT NOT NULL,
            date_opened TIMESTAMP
        )
    ''')
    # executing an sql command to create customers table if it does not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            account_number INTEGER
        )
    ''')

    conn.commit() #commiting the transaction
    conn.close() #closing the db connection

def drop_tables():
    # A function to drop a table
    conn = get_db_connection() # get db connection
    cursor = conn.cursor() #creating a cursor object to execute sql commmands
    
    # executing an sql command to drop accounts table if it exists
    cursor.execute('''
        DROP TABLE IF EXISTS accounts 
    ''')

    # executing an sql command to create customers table if it exists
    cursor.execute('''
        DROP TABLE IF EXISTS customers 
    ''')
    
    conn.commit() #commiting the customers
    conn.close() #closing the db connection
