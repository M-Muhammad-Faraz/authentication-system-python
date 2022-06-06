import random as rm
import tabulate

class user:
    def __init__(self,username,password,info):
        self.id = rm.randint(1,100000000000)
        self.username=username
        self.password=password
        self.info=info

    def main_menu(self):
        print("Welcome " + self.username);
        
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
        input()
    
    
     