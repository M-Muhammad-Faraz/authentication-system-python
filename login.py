from os import system
from console_colors import bcolors
from database import database
import pwinput
def login():
    system("cls")
    print("Login Page")
    uname=input("Enter Username: ")
    print("Enter ",end="")
    passw=pwinput.pwinput()
    user=database.getAUser(uname,passw)

    if user["code"]=="200":
        currentUser = user["userData"]
        return currentUser
    
    else:
        err = user["error"]
        input(f"{bcolors.FAIL}{err}{bcolors.ENDC}\nPress Any Key to Continue")
        login()
        
                
    
    return -1
    

