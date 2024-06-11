from lib.models.accounts import Account
from lib.models.customers import Customer
from lib.models.setup import create_tables

def main():
    create_tables()

    customer_name = input('Enter your name: ')
    customer_address = input('Enter your address: ')
    customer_phone = input('Input your phone number: ')
    customer_email = input('Input your email: ')
    customer_account_number = input('Enter your account number: ')

    account_number = input('Enter account number: ')
    account_balance = input('Enter account balance: ')
    account_type = input('Enter account type: ')
    date_opened = input('Enter date of creation: ')

    new_customer = Customer.create(customer_name, customer_address, customer_phone, customer_email, customer_account_number)

    new_account = Account.create(account_number, account_balance, account_type, date_opened)

    print("Customer created:", new_customer)
    print ('Account created:', new_account)

if __name__ == "__main__":
    main()
