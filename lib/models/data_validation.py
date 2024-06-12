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

def validate_account_type(account_type):
    valid_types = ['Savings', 'Checking', 'Business', 'Fixed', 'Current']
    if account_type not in valid_types:
        raise ValueError(f"Account type must be one of the following: {', '.join(valid_types)}.")
    return account_type