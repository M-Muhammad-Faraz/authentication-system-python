def encrption(data):
 tmp=''

 for i in range(0,len(data)):
     
     cr = data[i]
     dr=ord(cr)
     if dr<13:
        cr=dr
     else:
        cr = chr(ord(cr)+13)
     
     tmp+=cr
 return tmp;

def decryption(data):
 tmp=''
 for i in range(0,len(data)-1):
     
     cr = data[i];
     dr = ord(cr)
     if dr<13:
        cr=dr
     else:
        cr = chr(dr-13)
     tmp+=cr
 return tmp;


