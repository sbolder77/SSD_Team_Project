#Importing necessary modules
from cryptography.fernet import Fernet

#Defining Admin() class and it's downstream functions
class Admin():
#Defining writing administrator authentication deposit file
    def write_administratorDeposit(self, adminAuthenticator):
        with open("adminKey.csv", "w", encoding='utf-8') as file:
            file.write(adminAuthenticator)
            
#Defining generating of administrator key and writing it to a file
    def write_adminKey(self):
        key = Fernet.generate_key()
        with open ("key.adminKey", "wb") as key_file:
            key_file.write(key)

#Defining loading of admin key
    def load_adminKey(self):
        return open("key.adminKey", "rb").read()

#Defining of encrypting input from user, writing it to a file & returning it
    def encrypt(self, filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_password = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_password)
        return encrypted_password

#Defining of decrypting input from user, writing it to a file & returning it
    def decrypt(self, filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_password = file.read()
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password
