def validate_account_number(account_number):
    if len(account_number) != 10 or not account_number.isdigit():
        raise ValueError("Account number must be exactly 10 digits long.")
    return account_number

def validate_account_balance(account_balance):
    try:
        balance = float(account_balance)
        if balance < 0:
            raise ValueError("Account balance cannot be negative.")
    except ValueError:
        raise ValueError("Account balance must be a valid number.")
    return balance