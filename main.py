from os import system
from login import login
from signup import signup



option = {
    "login":1,
    "signup":2,
    "exit":3
}
def home_page():
    system("cls")
    choice=int(input("Authorization\nPress 1: Login\nPress 2: Signup\n"))
    if(choice == option["login"]):
        
        success=login()
        if success == -1:
            print("Login Failed. Wrong Username/Password. Try Again")
        
        else:
            success.main_menu()

    elif choice == option["signup"]:
        signup()
    elif choice == option["exit"]:
        exit;
    else:
        input("Wrong Option Selected...\nPress Any Key To Continue...\n")
        system("cls")    






while True:
    home_page()
    
  

