from user import user
from database import database;


def signup():
    username=input("Enter Username: ")
    passwordNowVerified = False 

    while not passwordNowVerified:
        password=input("Enter Password: ")
        confirmPassword=input("Enter Password again: ")

        if password==confirmPassword:
          passwordNowVerified=True
        else:
            print("Password Dont Match Try Again\n")
        

    answer = input("Heart Attack... Press 'P' for positive. Press 'N' for Negitive")
    heart_attack = True if (answer=='p' or answer=='P') else False
    
    answer = input("Tumor... Press 'P' for positive. Press 'N' for Negitive")
    tumor = True if (answer=='p' or answer=='P') else False
    
    answer = input("Cancer... Press 'P' for positive. Press 'N' for Negitive")
    cancer = True if (answer=='p' or answer=='P') else False
    
    answer = input("COVID... Press 'P' for positive. Press 'N' for Negitive")
    covid = True if (answer=='p' or answer=='P') else False
    
    answer = input("TB... Press 'P' for positive. Press 'N' for Negitive")
    tb = True if (answer=='p' or answer=='P') else False
    
    bloodgroup = input("Enter You bloodgroup")

    newUser= user(username,password,{"heartAttack":heart_attack,"tumor":tumor,"cancer":cancer,"covid":covid,"tb":tb,"bloodGroup":bloodgroup})
    database.addANewUser(newUser)



