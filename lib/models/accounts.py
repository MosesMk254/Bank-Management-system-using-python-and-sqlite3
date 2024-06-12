from .config import get_db_connection
from .setup import create_tables, drop_tables
from .data_validation import validate_account_number,validate_account_balance

class Account:
    def __init__(self, account_number, account_balance, account_type, date_opened, id=None):
        self.id = id
        self.account_number = validate_account_number(account_number)
        self.account_balance = validate_account_balance(account_balance)
        self.account_type= account_type
        self.date_opened = date_opened

    def __repr__(self) -> str:
        return f'<Account: {self.account_number}>'
    
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
            INSERT INTO accounts (
            account_number, account_balance, account_type, date_opened
            ) VALUES (?, ?, ?, ?)
        """

        cursor.execute(sql, (self.account_number, self.account_balance, self.account_type, self.date_opened,))
        conn.commit()

        self.id = cursor.lastrowid

    @classmethod
    def create(cls, account_number, account_balance, account_type, date_opened):
        account = cls(account_number, account_balance, account_type, date_opened)
        account.save()

        return account
    
    def update(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            UPDATE accounts SET account_number = ?, account_balance = ?, account_type = ?, date_opened = ?
            WHERE id = ?
        """

        cursor.execute(sql, (self.account_number, self.account_balance, self.account_type, self.date_opened, self.id,))
        conn.commit()
        
    def delete(self):
        conn =get_db_connection()
        cursor = conn.cursor()

        sql = """
            DELETE FROM accounts
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))
        conn.commit()

