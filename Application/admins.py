from cryptography.fernet import Fernet

class Admin():
    """Defining Admin() class and it's downstream functions"""
    def write_administrator_deposit(self, admin_authenticator):
        """Defining writing administrator authentication deposit file"""
        with open("admin_key.csv", "w", encoding='utf-8') as file:
            file.write(admin_authenticator)

    def write_admin_key(self):
        """Defining generating of administrator key and writing it to a file"""
        key = Fernet.generate_key()
        with open ("key.admin_key", "wb") as key_file:
            key_file.write(key)

    def load_admin_key(self):
        """Defining loading of admin key"""
        return open("key.admin_key", "rb").read()

    def encrypt(self, filename, key):
        """Defining of encrypting input from user, writing it to a file & returning it"""
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_password = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_password)
        return encrypted_password

    def decrypt(self, filename, key):
        """Defining of decrypting input from user, writing it to a file & returning it"""
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_password = file.read()
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password
