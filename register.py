from bank import *
from customer import *
import random

def SignUp():
    username=input("Create Username: ")
    temp=db_query(f"SELECT username from customers WHERE username='{username}';")
    
    if temp:
        print("Username is Already Exists")
        SignUp()
    else:
        print("Username is Available Please Proceed")
        password=input("Enter Your Password ")
        name=input("Enter Your Name: ")
        age=input("Enter Your age:")
        city=input("Enter Your City: ")


        while True:
            account_no=int(random.randint(1000000000,9999999999))
            temp = db_query(f"SELECT account_no FROM customers WHERE account_no='{account_no}';")
            if  temp:
                continue
            else:
                print("Your Account Number is:",account_no)
                break 

    cobj=Customer(username, password, name, age, city, account_no)
    cobj.createuser()
    bobj = Bank(username, account_no)
    bobj.create_transaction_table()
def SignIn():
    username=input("Enter Username: ")
    temp=db_query(f"SELECT username from customers WHERE username='{username}';")
    if temp:
         while True:
            password=input(f"Welcome {username.capitalize()}Enter Password: ")
            temp=db_query(f"SELECT password from customers WHERE username='{username}';")
            if temp[0][0] == password:
                print("Sign IN Succesfully")
                return username
            else:
                print("Wrong Password Try Again")
                continue
    else:
         print("Enter Correct Username")
         SignIn()

