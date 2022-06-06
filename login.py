from os import system
from database import database

def login():
    system("cls")
    print("Login Page")
    uname=input("Enter Your Username: ")
    passw=input("Enter your password: ")
    user=database.getAUser(uname,passw)

    if user["code"]=="200":
        currentUser = user["userData"]
        return currentUser
    
    else:
        print(user["error"])        
    
    return -1
    

