#Importing necessary modules
from admins import Admin

#Defining main program
def main(self):
#Defining administrator authentication, depositing it and encrypting it
    adminAuthenticator = input('Set the administrator key: ')
    Admin.write_administratorDeposit(self, adminAuthenticator)
    Admin.write_adminKey(self)
    key = Admin.load_adminKey(self)
    Admin.encrypt(self, 'adminKey.csv', key)

#Run program
if __name__ == '__main__':
    main(main)
