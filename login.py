from os import system
from turtle import bgcolor
from console_colors import bcolors
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
        err = user["error"]
        input(f"{bcolors.FAIL}{err}{bcolors.ENDC}\nPress Any Key to Continue")
        
                
    
    return -1
    

