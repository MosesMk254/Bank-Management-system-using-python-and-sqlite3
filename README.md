# Bank Management System

## Date 2024/06/13

## By Moses Mutisya

## Description
The Bank Management System is a CLI-based application designed to manage bank accounts and customers. It provides functionalities to create, update, delete, and retrieve accounts and customer details. The system uses SQLite as its database.

## Features
- Create and delete bank accounts
- Create and delete customers
- Update account and customer details
- Retrieve all accounts and customers
- Find specific account or customer by ID

## Installation

1. fork and clone repository using the link:

https://github.com/MosesMk254/Bank-Management-system-using-python-and-sqlite3.git

or by downloading a zip file of the code.

2. The repository, if downloaded as a .zip file will need to be extracted to your preferred location.

3. Navigate to the project folder on your bash terminal.

4. create a virtual environment using:

    pipenv install

5. Activate the virtual environment using:

    pipenv shell

6. To open the cli run:

    cli.py

7. to generate the existing db run:

    __init__.py


## Project Structure
.
├── db
│ └── bank.db # SQLite database file
├── lib
│ └── models
│ ├── accounts.py # Account class definition
│ ├── customers.py # Customer class definition
│ └── setup.py # Functions to create and drop tables
├── main.py # Main entry point for the CLI application
├── config.py # Database connection configuration
├── data_validation.py # Data validation functions
└── README.md # Project README file

## Technologies Used

Github, python, sqlite3

# Support and Contact details

github.com/MosesMK254 or mutisyamoses722@gmail.com

# Licence 

The content of this site is licenced under the MIT licence Copyright  (c) 2024.