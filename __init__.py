#Importing classes from modules
from lib.models.accounts import Account #importing the Account class 
from lib.models.customers import Customer #importing the Customer class

Account.drop_table() #droppimg the Account table
Account.create_table() #creating the Account 

Customer.drop_table() #droping the Customer table
Customer.create_table() #creating the Customer table

#Assigning the accounts
account1= Account.create('1234567890', 100000, 'Current', '10th July 2003')
account2= Account.create('1089256342', 10484800, 'Fixed', '15th January 2017')
account3= Account.create('1000231784', 389848759202, 'Savings', '13 August 2022')
account4= Account.create('6590290167', 136578292, 'Current', '10th July 2020')
account5= Account.create('1002209378', 100, 'Savings', '6th June 2024')

#Updating the account data
account1.account_type = 'Savings'
account1.update()

#deleting am account
# account4.delete()

#Assigning the customers
customer1 =Customer.create('Moses Mutisya', '123-Nairobi', '0746962449', 'mutisyamoses722@gmail.com', account3.account_number)
customer2 =Customer.create('Jessica Pears', '12454-Kisumu', '0747667676', 'jessicapears722@gmail.com', account1.account_number)
customer3 =Customer.create('Michael Ross', '12465-Nakuru', '07469665659', 'michaelross722@gmail.com', account5.account_number)
customer4 =Customer.create('Harvey Specter', '125-Mombasa', '07469646449', 'harveyspecter@gmail.com', account2.account_number)
customer5 =Customer.create('Dona Marie', '4743-Nairobi', '0746101019', 'donamarie@gmail.com', account4.account_number)

#updating the Customers data
customer4.name = 'Louis Litt'
customer4.update()

#deleting the customer data
# customer5.delete()