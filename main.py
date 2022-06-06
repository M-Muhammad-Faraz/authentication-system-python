from numpy import sign
from login import login
from signup import signup
from user import user



option = {
    "login":1,
    "signup":2
}





while True:
    choice=int(input("Authorization\nPress 1: Login\nPress 2: Signup\n"))
    if(choice == option["login"]):
        
        success=login()
        if success == -1:
            print("Login Failed. Wrong Username/Password. Try Again")
        
        else:
            success.display()

    elif choice == option["signup"]:
        signup()
  

