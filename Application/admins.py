#Importing necessary modules
from cryptography.fernet import Fernet

class Admin():
    def write_administratorDeposit(self, adminAuthenticator_1):
        with open("adminKey.csv", "w", encoding='utf-8') as file:
            file.write(adminAuthenticator_1)
    
    def write_adminKey(self):
        key = Fernet.generate_key()
        with open ("key.adminKey", "wb") as key_file:
            key_file.write(key)
    
    def load_adminKey(self):
        return open("key.adminKey", "rb").read()

    def encrypt(self, filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_password = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_password)
        return encrypted_password

    def decrypt(self, filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_password = file.read()
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password
