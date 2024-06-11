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
