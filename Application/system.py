import json
from cryptography.fernet import Fernet

user_data_file = 'users.json'
j = open(user_data_file)
data = json.load(j)
jsonData = data["Users"]

class UserDetails:
    def __init__(self):
        self.test = "test"

    def authorise_user(user_name):
        return self.test
