"""Importing necessary modules"""
from admins import Admin

def main(self):
    """Defining main program"""
#Defining administrator authentication, depositing it and encrypting it
    admin_authenticator = input('Set the administrator key: ')
    Admin.write_administrator_deposit(self, admin_authenticator)
    Admin.write_admin_key(self)
    key = Admin.load_admin_key(self)
    Admin.encrypt(self, 'admin_key.csv', key)

#Run program
if __name__ == '__main__':
    main(main)
