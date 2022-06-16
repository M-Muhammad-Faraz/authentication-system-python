import sys
from user import user
from cypher import encrption,decryption
class databaseModel:
    def __init__(self):
        self.users = []
        f = open("users.txt",encoding="utf-8")
        for line in f:
            try:
                obj =eval(decryption(line))
                newUser = user(obj["username"],obj["password"],obj["info"])
                self.users.append(newUser)
            except:
                raise Exception('Error: '+sys.exc_info[0]) from None
            finally:
                continue
        f.close()
        self.currentUser=-1


    def addANewUser(self,user):
        status = self.checkforExistingUser(user.username)
        if status["code"]=="400":
            return {"code":"400","error":"Username Taken"}
        else:
            data=user.dumpInfo()
            f = open("users.txt", "a",encoding="utf-8")
            encrpyted_text = encrption(str(data))
            f.write(encrpyted_text+"\n")
            f.close()
            self.users.append(user)
            return {"code":"200","user":user }

    def checkforExistingUser(self,username):
        for user in self.users:
            if user.username==username:
                return {"code":"400"}
        
        return {"code":"200"}

    
    def getAUser(self,username,password):
        for user in self.users:
            if user.username==username:
                if user.password == password:
                    self.currentUser = user
                    return {"code":"200","userData":user}
                else:
                    return{"code":"400","error":"Incorrect Password"}
        return {"code":"404","error":"User Not Found"}

database = databaseModel()


