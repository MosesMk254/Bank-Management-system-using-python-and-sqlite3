# Importing necessary functions from other modules
from .config import get_db_connection # Function to establish database connection
from .setup import create_tables, drop_tables # Functions to create and drop tables
from .data_validation import validate_account_number,validate_account_balance, validate_account_type # Functions for data validation

class Account:
    def __init__(self, account_number, account_balance, account_type, date_opened, id=None):
        # Initializing an Account instance with validated attributes
        self.id = id
        self.account_number = validate_account_number(account_number) # Validate account number
        self.account_balance = validate_account_balance(account_balance) #Validate account balance
        self.account_type= validate_account_type(account_type) #Validate account_type
        self.date_opened = date_opened

    def __repr__(self) -> str:
        # a string representation for the Account instance
        return f'<Account: {self.account_number}>'
    
    @classmethod 
    def create_table(cls):
        # Class method to create the database tables for accounts
        create_tables()
    
    @classmethod
    def drop_table(cls):
        # Class method to drop the database tables for accounts
        drop_tables()

    def save(self):
        # Saving the Account instance to the database
        conn = get_db_connection() # get db connection
        cursor = conn.cursor() #creating a cursor object to execute sql commmands

        #creating a sql command to insert data int a table
        sql = """
            INSERT INTO accounts (
            account_number, account_balance, account_type, date_opened
            ) VALUES (?, ?, ?, ?)
        """

         # Executing the SQL command with the instance's attributes
        cursor.execute(sql, (self.account_number, self.account_balance, self.account_type, self.date_opened,))
        conn.commit() #commit the transactions

        self.id = cursor.lastrowid # Get the ID of the newly inserted row

    @classmethod
    def create(cls, account_number, account_balance, account_type, date_opened):
        # Class method to create a new Account instance and save it to the db
        account = cls(account_number, account_balance, account_type, date_opened) # Creating a new Account instance
        account.save() # Saving the new account to the db

        return account #Returning the newly created account instance
    
    def update(self):
         # Updating the Account instance in the db
        conn = get_db_connection()  # get db connection
        cursor = conn.cursor()  #creating a cursor object to execute sql commmands
        
        #creating an sql command to update an account
        sql = """
            UPDATE accounts SET account_number = ?, account_balance = ?, account_type = ?, date_opened = ?
            WHERE id = ?
        """

        # Executing the SQL command with update attribute
        cursor.execute(sql, (self.account_number, self.account_balance, self.account_type, self.date_opened, self.id,))
        conn.commit() #commit the transaction
        
    def delete(self):
        # Deleting the account instance from the db
        conn =get_db_connection() # get db connection
        cursor = conn.cursor() #creating a cursor object to execute sql commmands

        #creating an sql command to delete an account
        sql = """
            DELETE FROM accounts
            WHERE id = ?
        """

         # Executing the SQL command to delete an account by its ID
        cursor.execute(sql, (self.id,))
        conn.commit()

    @classmethod
    def get_all(cls):
        conn = get_db_connection() #get db connection
        cursor = conn.cursor() #creating a cursor object to execute sql commands

        #sql command to get all data from accounts table
        sql = "SELECT * FROM accounts"

        #executing sql command to fetch all the data from the acconts table
        cursor.execute(sql)
        rows = cursor.fetchall()
        conn.close()

        #creating a class property to store data from the class table
        accounts = []

        #looping over each rows and appending the instances
        for row in rows:
            try:
                accounts.append(cls(account_number=str(row[1]), account_balance=row[2], account_type=str(row[3]), date_opened=row[4], id=row[0]))
            except ValueError as e:
                # Log the error or handle it as needed
                print(f"Error processing account ID {row[0]}: {e}")
        return accounts
