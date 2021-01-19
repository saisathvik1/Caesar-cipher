s = """

 _____                                   _       _               
/  __ \                                 (_)     | |              
| /  \/ __ _  ___  ___  __ _ _ __    ___ _ _ __ | |__   ___ _ __ 
| |    / _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
| \__/\ (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
 \____/\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                          | |                    
                                          |_|                    

"""  
print(s)
alphabet = "abcdefghijkmnopqrstuvwxyz"
l = [i.upper() for i in alphabet]
def encrypt(plaintext,key):
  ciphertext = ""
  for letter in plaintext.upper():
    p = l.index(letter)+key
    ciphertext+=l[p%25]
  print("The ciphertext is",ciphertext)

def decrypt(ciphertext,key):
  plaintext = ""
  for letter in ciphertext.upper():
    p = l.index(letter)-key
    plaintext+=l[p%25]
  print("The plaintext is",plaintext)

print("Type 'encode' for encryption and 'decode' for decryption")
op=input("Option> ")
if op.lower()=="encode":
  plaintext = input("Enter plaintext: ")
  key = int(input("Enter key: "))
  encrypt(plaintext,key)
elif op.lower()=="decode":
  ciphertext = input("Enter Ciphertext: ")
  key = int(input("Enter key used for encryption: "))
  decrypt(ciphertext,key)