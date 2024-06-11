from lib.models.accounts import Account
from lib.models.customers import Customer

Account.drop_table()
Account.create_table()

Customer.drop_table()
Customer.create_table()

account1= Account.create(1234, 100000, 'Current account', '10th July 2003')
account2= Account.create(1089, 10484800, 'Fixed account', '15th January 2017')
account3= Account.create(1000, 389848759202, 'Savings account', '13 August 2022')
account4= Account.create(6590, 136578292, 'Current account', '10th July 2020')
account5= Account.create(1002, 100, 'Savings account', '6th June 2024')

customer1 =Customer.create('Moses Mutisya', '123-Nairobi', '0746962449', 'mutisyamoses722@gmail.com', account3.account_number)
customer2 =Customer.create('Jessica Pears', '12454-Kisumu', '0747667676', 'jessicapears722@gmail.com', account1.account_number)
customer3 =Customer.create('Michael Ross', '12465-Nakuru', '07469665659', 'michaelross722@gmail.com', account5.account_number)
customer4 =Customer.create('Harvey Specter', '125-Mombasa', '07469646449', 'harveyspecter@gmail.com', account2.account_number)
customer5 =Customer.create('Dona Marie', '4743-Nairobi', '0746101019', 'donamarie@gmail.com', account4.account_number)