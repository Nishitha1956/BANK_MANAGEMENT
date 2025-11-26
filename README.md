🏦 Bank Account Management System (Python + MySQL)

This is a command-line based banking system built using Python and MySQL.
It supports user account creation, secure sign-in, and database-backed storage of users.

📌 Features

✔ User Registration (SignUp)
✔ User Login (SignIn)
✔ MySQL database connectivity
✔ Persistent user storage
✔ Unique account number generation
✔ Password authentication
✔ Customer table auto-creation

🗂 Project Structure
├── main.py
├── register.py
├── customer.py
├── database.py
└── bank.py   (expected but not uploaded — referenced in register.py)

File Responsibilities
File	Purpose
main.py	App entry point; main menu loop
register.py	SignUp / SignIn logic
customer.py	Customer object + DB insert
database.py	MySQL connection + query functions
bank.py	Expected to contain transaction functions (but not provided)


⚙️ Requirements
Install Python libraries:
pip install mysql-connector-python

MySQL Setup

Create a MySQL database:

CREATE DATABASE bank;


🔌 Database Configuration

Inside database.py, update:

mydb = sql.connect(
    host="127.0.0.1",
    user="root",
    password="YOUR_PASSWORD",
    database="bank"
)


▶️ Running the Application
python main.py


Then in console:

Welcome to our Bank
1.SignUp
2.SignIn



🧠 How SignUp Works (flow)

Check if username already exists

Accept password, name, age, city

Generate unique 10-digit account number

Create Customer object

Insert into MySQL

Create a transaction table (via Bank class — requires bank.py)


🔐 Security Considerations

⚠️ Passwords are stored in plain text
⬆️ Should be hashed using:

import bcrypt



🚀 Future Enhancements

Deposit / withdrawal system

Balance checking

Transaction history

Admin panel

GUI or web UI

Email / SMS OTP login
