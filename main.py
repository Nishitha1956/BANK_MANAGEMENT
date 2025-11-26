from register import *


print("Welcome to our Bank")
while True:
    try:
        register=int(input("1.signUp\n"
                           "2.SignIn"))
        
        if register==1:
                SignUp()
        elif register==2:
                SignIn()
        else:
            print("Please enter Valid Input From Options")

    except ValueError:
        print("Invalid Input Try Again with Valid Input")
       