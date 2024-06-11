from .config import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number INTEGER,
            account_balance INTEGER,
            account_type TEXT NOT NULL,
            date_opened TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address INTEGER,
            phone TEXT NOT NULL,
            email TEXT NOT NULL,
            account_number INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def drop_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        DROP TABLE IF EXISTS accounts 
    ''')
    cursor.execute('''
        DROP TABLE IF EXISTS customers 
    ''')
    
    conn.commit()
    conn.close()
