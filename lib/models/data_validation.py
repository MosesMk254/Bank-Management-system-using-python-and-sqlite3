def validate_account_number(account_number):
    if len(account_number) != 10 or not account_number.isdigit():
        raise ValueError("Account number must be exactly 10 digits long.")
    return account_number