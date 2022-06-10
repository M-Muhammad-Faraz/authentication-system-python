import random as rm
import tabulate
from os import system

choice = {"choice1":1,"choice2":2}
class user:
    def __init__(self,username,password,info,id=13):
        self.id = rm.randint(1,100000000000)
        self.username=username
        self.password=password
        self.info=info
        self.encryption_pass=id

    def dumpInfo(self):
        return {"username":self.username,"password":self.password,"info":self.info,"encryption_pass":self.id ,}

    def main_menu(self):
        system("cls")
        print("Welcome " + self.username);
        ch = int(input("What would You Like to do!\nPress 1:View Your Medical Record\nPress 2: Logout"))
        if ch == choice["choice1"]:
            self.display()
        else:
            return
    
    def display(self):
        table = [
            ["Blood-group",self.info["bloodGroup"]],
            ["Tumor","Positive" if self.info["tumor"] else "Negitive"],
            ["Cancer","Positive" if self.info["cancer"] else "Negitive"],
            ["TB","Positive" if self.info["tb"] else "Negitive"],
            ["COVID-19","Positive" if self.info["covid"] else "Negitive"],
            ["Heart-Attack","Positive" if self.info["heartAttack"] else "Negitive"],
        ]
        print(tabulate.tabulate(table));
        input("Press any key to go back...\n")
        self.main_menu()
    
    
     