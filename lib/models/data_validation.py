import re  # Import the regular expression module for email validation 

def validate_account_number(account_number):
    """
    Validate the account number.
    The account number must be exactly 10 digits long.
    """
    if len(account_number) != 10 or not account_number.isdigit():
        raise ValueError("Account number must be exactly 10 digits long.")
    return account_number

def validate_account_balance(account_balance):
    """
    Validate the account balance.
    The account balance must be a non-negative number.
    """
    try:
        balance = float(account_balance)
        if balance < 0:
            raise ValueError("Account balance cannot be negative.")
    except ValueError:
        raise ValueError("Account balance must be a valid number.")
    return balance

def validate_account_type(account_type):
    """
    Validate the account type.
    The account type must be one of the predefined valid types.
    """
    valid_types = ['Savings', 'Checking', 'Business', 'Fixed', 'Current']
    if account_type not in valid_types:
        raise ValueError(f"Account type must be one of the following: {', '.join(valid_types)}.")
    return account_type

def validate_name(name):
    """
     Validate the name.
    The name must be at least 2 characters long and contain only alphabets and spaces.
    """
    if len(name) < 2 or not name.replace(' ', '').isalpha():
        raise ValueError("Name must be at least 2 characters long and contain only alphabets and spaces.")
    return name

def validate_address(address):
    """
    Validate the address.
    The address must be at least 5 characters long.
    """
    if len(address) < 5:
        raise ValueError("Address must be at least 5 characters long.")
    return address

def validate_phone(phone):
    """
    Validate the phone number.
    The phone number must be exactly 10 digits long.
    """
    if len(phone) < 10:
        raise ValueError("Phone number must be exactly 10 digits long.")
    return phone

def validat_email(email):
    """
    Validate the email address.
    The email must match the regular expression pattern for a valid email address.

    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 
    if(re.fullmatch(regex, email)):
        return email
    else:
        raise ValueError("Invalid Email")