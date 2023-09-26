import json
from cryptography.fernet import Fernet

user_data_file = 'users.json'
j = open(user_data_file)
data = json.load(j)
jsonData = data["Users"]

class UserDetails:
    def __init__(self):
        self.test = "test"
        
    def get_user(self, user_name):
        #fernet = Fernet(key)
        #with open(user_data_file, 'rb') as f:
            #data = f.read()
        #decrypted = fernet.decrypt(data)
        #with open(user_data_file, 'wb') as f:
            #f.write(decrypted)
        for v in jsonData:
            values = list(v.values())[0]
            print(values)
            if values == user_name:
                return True
            else:
                return False
        #with open(user_data_file, 'rb') as f:
            #data = f.read()
        #encrypted = fernet.encrypt(data)
        #with open(user_data_file, 'wb') as f:
            #f.write(encrypted)
        #return 'User created'
    
    def create_user(self, userlist):
        #fernet = Fernet(key)
        #with open(user_data_file, 'rb') as f:
            #data = f.read()
        #decrypted = fernet.decrypt(data)
        #with open(user_data_file, 'wb') as f:
            #f.write(decrypted)
        self.id = userlist[0]
        self.firstName = userlist[1]
        self.surname = userlist[2]
        self.password = userlist[3]
        self.emailaddress = userlist[4]
        self.house = userlist[5]
        self.street = userlist[6]
        self.town = userlist[7]
        self.county = userlist[8]
        self.postcode = userlist[9]
        jsonData.append({
            "ID": self.id,
            "Role": 'U',
            "FirstName": self.firstName,
            "Surname": self.surname,
            "Password": self.password,
            "EmailAddress": self.emailaddress,
            "House": self.house,
            "Street": self.street,
            "Town": self.town,
            "County": self.county,
            "Postcode": self.postcode
        })
        with open (user_data_file, 'w') as users.json:
            json.dump(data, json_file, indent=4, separators=(',',': '))
        #with open(user_data_file, 'rb') as f:
            #data = f.read()
        #encrypted = fernet.encrypt(data)
        #with open(user_data_file, 'wb') as f:
            #f.write(encrypted)
        #return 'User created'
    
    def edit_user(self, userlist):
        return u.get_user(user_name)
        if u.get_user(user_name) == True:

            self.id = userlist[0]
            self.firstName = userlist[1]
            self.surname = userlist[2]
            self.password = userlist[3]
            self.emailaddress = userlist[4]
            self.house = userlist[5]
            self.street = userlist[6]
            self.town = userlist[7]
            self.county = userlist[8]
            self.postcode = userlist[9]
            jsonData.append({
                "ID": self.id,
                "Role": 'U',
                "FirstName": self.firstName,
                "Surname": self.surname,
                "Password": self.password,
                "EmailAddress": self.emailaddress,
                "House": self.house,
                "Street": self.street,
                "Town": self.town,
                "County": self.county,
                "Postcode": self.postcode
            })
            with open (user_data_file, 'w') as users.json:
                json.dump(data, json_file, indent=4, separators=(',',': '))

    def check_user(self, user_name):
        if bool(u.get_user(user_name)) = True:
            print('Welcome back. Logging you in...')
        else:
            print('Account not found. Please register an account to log in.')

    def authorise_user(user_name):
        return self.test

    def delete_user(self):
        with open (user_data_file, 'w') as users.json:
            json.delete(data, json_file)
