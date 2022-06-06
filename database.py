from user import user 

class databaseModel:
    def __init__(self):
        self.users = []
        self.currentUser=-1
    def addANewUser(self,user):
        self.users.append(user)
        return user
    def getAUser(self,username,password):
        for user in self.users:
            if user.username==username and user.password == password:
                self.currentUser = user
                return {"code":"200","userData":user}
        return {"code":"400","error":"User Not Found"}
    
    def getCurrentUser(self):
        return self.currentUser    

    def removeAUser(self,user):
        self.users.popitem(user)

database = databaseModel()


