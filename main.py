from os import system
import sys
from time import sleep

from login import login
from signup import signup

PROGRAM_END = False
option = {
    "login":"1",
    "signup":"2",
    "exit":"3"
}
def home_page():
    system("cls")
    choice=input("Authorization\nPress 1: Login\nPress 2: Signup\nPress 3: Exit\n")
    if(choice == option["login"]):
        success=login()
        if success == -1:
            print("Login Failed. Wrong Username/Password. Try Again")
        else:
            success.main_menu()
    elif choice == option["signup"]:
        signup()
    elif choice == option["exit"]:
        global PROGRAM_END
        
        words = "GOOD BYE! Hope You Enjoy!!!\r                           \rOur Authentication Project "
        for char in words:
            sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        PROGRAM_END=True
    else:
        input("Wrong Option Selected...\nPress Any Key To Retry..\n")
        system("cls")    

while not PROGRAM_END:
    home_page()
    
  

