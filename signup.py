from os import system
import re

from database import database;
from user import user
from console_colors import bcolors

import pwinput


def verifyInput(inp):
  if inp == 'p'or inp == 'P'or inp == 'n'or inp == 'N':
    return True
  else:
    return False

def signup():
    OPTION = {"option1":"1","option2":"2"}
    system("cls")
    print("SIGNUP PAGE\n")
    userNameNowVerified = False
    while not userNameNowVerified:
      username=input("Enter Username: ")
      if len(username)<3:
          print(f"{bcolors.WARNING}Username Length should be 3 or greater{bcolors.ENDC}\n")
          continue 
      s_code = database.checkforExistingUser(username)
      if s_code["code"] == "400":
        print(f"{bcolors.FAIL}Error! Username Already Taken! Try Again\n{bcolors.ENDC}")
      else:
        userNameNowVerified=True

    passwordNowVerified = False 
    input_now_verified = False
    while not passwordNowVerified:
        print("Enter ",end="")
        password=pwinput.pwinput()
        if len(password)<8:
          print(f"{bcolors.WARNING}Password Length should be 8 or greater{bcolors.ENDC}\n")
          continue  
        print("Confirm ",end="")
        confirmPassword=pwinput.pwinput()
        if password==confirmPassword:
          passwordNowVerified=True
        else:
            print(f"{bcolors.WARNING}Password Dont Match Try Again{bcolors.ENDC}\n")
        
    input_now_verified = False
    while not input_now_verified:
      answer = input("Heart Attack... Press 'P' for positive. Press 'N' for Negitive : ")
      if verifyInput(answer):
        input_now_verified=True
        heart_attack = True if (answer=='p' or answer=='P') else False
      else:
        print(f"{bcolors.WARNING}Wrong Input Try Again{bcolors.ENDC}\n")
    
    input_now_verified = False
    while not input_now_verified:
      answer = input("Tumor... Press 'P' for positive. Press 'N' for Negitive : ")
      if verifyInput(answer):
        input_now_verified=True
        tumor = True if (answer=='p' or answer=='P') else False
      else:
        print(f"{bcolors.WARNING}Wrong Input Try Again{bcolors.ENDC}\n")

    input_now_verified = False
    while not input_now_verified:
      answer = input("Cancer... Press 'P' for positive. Press 'N' for Negitive : ")
      if verifyInput(answer):
        input_now_verified=True
        cancer = True if (answer=='p' or answer=='P') else False
      else:
        print(f"{bcolors.WARNING}Wrong Input Try Again{bcolors.ENDC}\n")

    input_now_verified = False
    while not input_now_verified:
      answer = input("COVID... Press 'P' for positive. Press 'N' for Negitive : ")
      if verifyInput(answer):
        input_now_verified=True
        covid = True if (answer=='p' or answer=='P') else False
      else:
        print(f"{bcolors.WARNING}Wrong Input Try Again{bcolors.ENDC}\n")


    input_now_verified = False
    while not input_now_verified:
      answer = input("TB... Press 'P' for positive. Press 'N' for Negitive : ")
      if verifyInput(answer):
        input_now_verified=True
        tb = True if (answer=='p' or answer=='P') else False
      else:
        print(f"{bcolors.WARNING}Wrong Input Try Again{bcolors.ENDC}\n")
    

    input_now_verified = False
    while not input_now_verified:

      bloodgroup = input("Enter You bloodgroup : ")

      if re.match("(A|B|AB|O)[+-]",bloodgroup):
        input_now_verified=True
      else:
        input(f"{bcolors.WARNING}Incorrect Bloodgroup, Please try again...{bcolors.ENDC}\n")

    newUser= user(username,password,{"heartAttack":heart_attack,"tumor":tumor,"cancer":cancer,"covid":covid,"tb":tb,"bloodGroup":bloodgroup})
    status=database.addANewUser(newUser)
    if status["code"] == "400":
      choice = input(f"{bcolors.FAIL}Error! Username Already Taken!{bcolors.ENDC}\nPress 1: Try again!\nPress 2: Go Back\n")
      if choice == OPTION["option1"]:
        signup()
      else:
        return
    else:
      input(f"{bcolors.OKGREEN}Account Created!{bcolors.ENDC}\nPress any key to continue..")




