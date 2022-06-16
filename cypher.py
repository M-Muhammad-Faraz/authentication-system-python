def encrption(data):
 tmp=''
 for i in range(0,len(data)-1):
     cr = data[i]
     dr=ord(cr)
     cr = chr(dr+13)
     tmp+=cr
 return tmp;

def decryption(data):
 tmp=''
 for i in range(0,len(data)-1):
     cr = data[i];
     dr = ord(cr)
     cr = chr(dr-13)
     tmp+=cr
 return tmp;