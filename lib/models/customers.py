# Importing necessary functions from other modules
from .config import get_db_connection # Function to establish database connection
from .setup import create_tables, drop_tables # Functions to create and drop tables
from .data_validation import validate_name, validate_address, validate_phone, validat_email, validate_account_number # Functions for data validation

class Customer:
    def __init__(self, name, address, phone, email, account_number, id=None):
        # Initializing a Customer instance with validated attributes
        self.id = id
        self.name = validate_name(name) # Validate name
        self.address = validate_address(address) # Validate address
        self.phone = validate_phone(phone) # Validate phone number
        self.email = validat_email(email) # Validate email
        self.account_number = validate_account_number(account_number) # Validate account number

    def __repr__(self) -> str:
        # a string representation for the Customer instance
        return f'<customer: {self.name}>'
    
    @classmethod 
    def create_table(cls):
         # Class method to create the database tables for customers
        create_tables()
    
    @classmethod
    def drop_table(cls):
        # Class method to drop the database tables for accounts
        drop_tables()

    def save(self):
        # Saving the Customer instance to the database
        conn = get_db_connection() # get db connection
        cursor = conn.cursor() #creating a cursor object to execute sql commmands

        #creating a sql command to insert data int a table
        sql = """
            INSERT INTO customers (
            name, address, phone, email, account_number
            ) VALUES (?, ?, ?, ?, ?)
        """

         # Executing the SQL command with the instance's attributes
        cursor.execute(sql, (self.name, self.address, self.phone, self.email, self.account_number,))
        conn.commit() #commit the custome

        self.id = cursor.lastrowid # Get the ID of the newly inserted row

    @classmethod
    def create(cls,  name, address, phone, email, account_number):
        # Class method to create a new Customer instance and save it to the db
        customer = cls(name, address, phone, email, account_number) # Creating a new Customer instance
        customer.save() # Saving the new customer to the db

        return customer #Returning the newly created customer instance
    
    def update(self):
        # updating the Customer instance to the database
        conn = get_db_connection() # get db connection
        cursor =conn.cursor() #creating a cursor object to execute sql commmands

        #creating a sql command to update data int a table
        sql = """
            UPDATE customers SET name = ?, address = ?, phone = ?, email = ?, account_number = ?
            WHERE id = ?
        """

        # Executing the SQL command with update attribute
        cursor.execute(sql, (self.name, self.address, self.phone, self.email, self.account_number, self.id,))
        conn.commit() #commit the customer

    def delete(self):
        # updating the Customer instance to the database
        conn =get_db_connection() # get db connection
        cursor = conn.cursor() #creating a cursor object to execute sql commmands

        # sql command to delete data from the db
        sql = """
            DELETE FROM customers
            WHERE id = ?
        """
        
         # Executing the SQL command to delete an customer by its ID
        cursor.execute(sql, (self.id,))
        conn.commit()

