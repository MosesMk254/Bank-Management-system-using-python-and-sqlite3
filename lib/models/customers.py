from .config import get_db_connection
from .setup import create_tables, drop_tables
from .data_validation import validate_name, validate_address

class Customer:
    def __init__(self, name, address, phone, email, account_number, id=None):
        self.id = id
        self.name = validate_name(name)
        self.address = validate_address(address)
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
    
    def update(self):
        conn = get_db_connection()
        cursor =conn.cursor()

        sql = """
            UPDATE customers SET name = ?, address = ?, phone = ?, email = ?, account_number = ?
            WHERE id = ?
        """

        cursor.execute(sql, (self.name, self.address, self.phone, self.email, self.account_number, self.id,))
        conn.commit()

    def delete(self):
        conn =get_db_connection()
        cursor = conn.cursor()

        sql = """
            DELETE FROM customers
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()

