from .config import get_db_connection
from .setup import create_tables, drop_tables

class Customer:
    def __init__(self, name, address, phone, email, account_number, id=None):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.account_number = account_number

    def __repr__(self) -> str:
        return f'<customer: {self.name}>'
    
    @classmethod 
    def create_table(cls):
        create_tables()
    
    @classmethod
    def drop_table(cls):
        drop_tables()

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO customers (
            name, address, phone, email, account_number
            ) VALUES (?, ?, ?, ?, ?)
        """

        cursor.execute(sql, (self.name, self.address, self.phone, self.email, self.account_number,))
        conn.commit()

        self.id = cursor.lastrowid

    @classmethod
    def create(cls,  name, address, phone, email, account_number):
        customer = cls(name, address, phone, email, account_number)
        customer.save()

        return customer
