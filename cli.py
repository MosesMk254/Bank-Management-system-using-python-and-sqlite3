# Importing classes and functions from the models module
from lib.models.accounts import Account #importing the Account class
from lib.models.customers import Customer #importing the customer class
from lib.models.setup import create_tables #importing the create table function

# Function to create a new account
def create_account():
    try:
        # Prompting user for account details
        account_number = input('Enter account number: ')
        account_balance = input('Enter account balance: ')
        account_type = input('Enter account type: ')
        date_opened = input('Enter date of creation: ')

        # Creating a new Account object using the provided details
        new_account = Account.create(account_number, account_balance, account_type, date_opened)
        # Informing the user of successful account creation
        print('Account created successfully.', new_account)
    except ValueError as e:
        # Handling any ValueError that occurs during account creation
        print(f"Error creating account: {e}")

#function to retrive all the accounts data
def get_all_accounts():
    all_accounts = Account.get_all() #getting all the accounts

    #looping through the accounts and displaying every detail to the cli
    for account in all_accounts:
        print(f"ID: {account.id}")
        print(f"Account Number: {account.account_number}")
        print(f"Account Balance: {account.account_balance}")
        print(f"Account Type: {account.account_type}")
        print(f"Date Opened: {account.date_opened}")
        print("-------------")
    return all_accounts

# Function to create a new customer
def create_customer():
    try:
        # Prompting user for customer details
        customer_name = input('Enter your name: ')
        customer_address = input('Enter your address: ')
        customer_phone = input('Input your phone number: ')
        customer_email = input('Input your email: ')
        customer_account_number = input('Enter your account number: ')

        # Creating a new Customer object using the provided details
        new_customer = Customer.create(customer_name, customer_address, customer_phone, customer_email, customer_account_number)
        # Informing the user of successful customer creation
        print('Customer created successfully.', new_customer)
    except ValueError as e:
        # Handling any ValueError that occurs during customer creation
        print(f'Error creating customer: {e}')

# Main function to run the Bank Management System
def main():
    # setting up the db
    create_tables()
    print("Bank Management System")
    while True:
        # Displaying menu options to the user
        print("""
            Select Your Options:
            1. Create an account
            2. Create a customer
            3. Retrive the accounts data
            4. Exit app
            """)
        # Getting user input for the desired option
        option = input('Enter your option: ')
        # Call create_account if option 1 is selected
        if option == "1":
            create_account()
        # Call create_customer if option 2 is selected
        elif option == '2':
            create_customer()
        #call get_all_accounts if option 3 is selected
        elif option == '3':
            get_all_accounts()
        # exit loop if option 4 is selected
        elif option == '4':
            break
        else:
            # Inform the user of invalid input
            print("Invalid option. Please choose again.")

# Entry point of the cli program
if __name__ == "__main__":
    main()
