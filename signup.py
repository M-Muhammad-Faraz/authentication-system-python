from os import system
import re
from user import user
from database import database;



def verifyInput(inp):
  if inp == 'p'or inp == 'P'or inp == 'n'or inp == 'N':
    return True
  else:
    return False

def signup():
    system("cls")
    print("SIGNUP PAGE\n")
    username=input("Enter Username: ")
    passwordNowVerified = False 
    input_now_verified = False
    while not passwordNowVerified:
        password=input("Enter Password: ")
        confirmPassword=input("Enter Password again: ")
        if password==confirmPassword:
          passwordNowVerified=True
        else:
            print("Password Dont Match Try Again\n")
        
    input_now_verified = False
    while not input_now_verified:
      answer = input("Heart Attack... Press 'P' for positive. Press 'N' for Negitive : ")
      if verifyInput(answer):
        input_now_verified=True
        heart_attack = True if (answer=='p' or answer=='P') else False
      else:
        print("Wrong Input Try Again\n")
    
    input_now_verified = False
    while not input_now_verified:
      answer = input("Tumor... Press 'P' for positive. Press 'N' for Negitive : ")
      if verifyInput(answer):
        input_now_verified=True
        tumor = True if (answer=='p' or answer=='P') else False
      else:
        print("Wrong Input Try Again\n")

    input_now_verified = False
    while not input_now_verified:
      answer = input("Cancer... Press 'P' for positive. Press 'N' for Negitive : ")
      if verifyInput(answer):
        input_now_verified=True
        cancer = True if (answer=='p' or answer=='P') else False
      else:
        print("Wrong Input Try Again\n")

    input_now_verified = False
    while not input_now_verified:
      answer = input("COVID... Press 'P' for positive. Press 'N' for Negitive : ")
      if verifyInput(answer):
        input_now_verified=True
        covid = True if (answer=='p' or answer=='P') else False
      else:
        print("Wrong Input Try Again\n")


    input_now_verified = False
    while not input_now_verified:
      answer = input("TB... Press 'P' for positive. Press 'N' for Negitive : ")
      if verifyInput(answer):
        input_now_verified=True
        tb = True if (answer=='p' or answer=='P') else False
      else:
        print("Wrong Input Try Again\n")
    

    input_now_verified = False
    while not input_now_verified:

      bloodgroup = input("Enter You bloodgroup : ")

      if re.match("(A|B|AB|O)[+-]",bloodgroup):
        input_now_verified=True
      else:
        input("Incorrect Bloodgroup, Please try again...\n")

    newUser= user(username,password,{"heartAttack":heart_attack,"tumor":tumor,"cancer":cancer,"covid":covid,"tb":tb,"bloodGroup":bloodgroup})
    database.addANewUser(newUser)
    
    input("Account Created!\nPress any key to continue..")




