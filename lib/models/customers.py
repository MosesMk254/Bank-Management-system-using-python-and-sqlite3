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

    def drop_table(cls):
        drop_tables()
