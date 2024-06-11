class Account:
    def __init__(self, account_number, account_balance, account_type, date_opened, id=None):
        self.id = id
        self.account_number = account_number
        self.account_balance = account_balance
        self.account_type= account_type
        self.date_opened = date_opened

    def __repr__(self) -> str:
        return f'<Account: {self.account_number}>'