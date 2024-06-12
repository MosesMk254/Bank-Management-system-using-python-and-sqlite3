from lib.models.accounts import Account
from lib.models.customers import Customer
from lib.models.setup import create_tables

def create_account():
    try:
        account_number = input('Enter account number: ')
        account_balance = input('Enter account balance: ')
        account_type = input('Enter account type: ')
        date_opened = input('Enter date of creation: ')

        new_account = Account.create(account_number, account_balance, account_type, date_opened)
        print('Account created successfully.', new_account)
    except ValueError as e:
        print(f"Error creating account: {e}")


def create_customer():
    try:
        customer_name = input('Enter your name: ')
        customer_address = input('Enter your address: ')
        customer_phone = input('Input your phone number: ')
        customer_email = input('Input your email: ')
        customer_account_number = input('Enter your account number: ')

        new_customer = Customer.create(customer_name, customer_address, customer_phone, customer_email, customer_account_number)
        print('Customer created successfully.', new_customer)
    except ValueError as e:
        print(f'Error creating customer: {e}')

def main():
    create_tables()
    print("Bank Management System")
    while True:
        print("""
            Select Your Options:
            1. Create an account
            2. Create a customer
            3. Exit app
            """)
        option = input('Enter your option: ')
        if option == "1":
            create_account()
        elif option == '2':
            create_customer()
        elif option == '3':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
