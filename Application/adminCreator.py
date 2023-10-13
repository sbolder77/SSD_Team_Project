from admins import Admin

def main(self):
    adminAuthenticator = input('Set the administrator key: ')
    Admin.write_administratorDeposit(self, adminAuthenticator)
    Admin.write_adminKey(self)
    key = Admin.load_adminKey(self)
    Admin.encrypt(self, 'adminKey.csv', key)

if __name__ == '__main__':
    main(main)
