#https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
#https://regex-generator.olafneumann.org

#Importing necessary modules
import json
from cryptography.fernet import Fernet
import filelogging
from datetime import datetime
import re

#Create json readable object
filename = 'system.json'
f = open(filename)
data = json.load(f)

#Variables
fernet = Fernet('d35AFvCPEXATL7kNnjz6CD6r20KR9qh5q1L9nZ6bk5k=')
USER_NON_ALPHA = re.compile('[A-Z]+_[A-Z]')
ITEM_ALPHA = re.compile('[^A-Z0-9]+')
ORDER_ALPHA = re.compile('[^A-Z0-9]+')

#Defining Settings() class and downstream functions
class Settings():
#Defining __init__
    def __init__(self):
        for x in data:
            self.log = x['log']
            self.ssl = x['ssl']
            self.datetimeformat = x['datetimeformat']
            self.encrypt = x['encrypt']
            self.useregex = x['useregex']

#Defining file encryption functionality
    def encryptfile(self, filename, user):
        l = filelogging.LoggingDetails()
        if self.encrypt == 'TRUE':
            with open(filename, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            l.write_system_log("SYSTEM", "INFO", filename + " has been encrypted", user)
            return filename + " has been encrypted"

#Defining file decryption functionality
    def decryptfile(self, filename, user):
        l = filelogging.LoggingDetails()
        if self.encrypt == 'TRUE':
            with open(filename, 'rb') as enc_file:
                encrypted = enc_file.read()
            decrypted = fernet.encrypt(encrypted)
            with open(filename, 'wb') as decrypted_file:
                decrypted_file.write(decrypted)
            l.write_system_log("SYSTEM", "INFO", filename + " has been decrypted", user)
            return filename + " has been decrypted"

#Defining user regex functionality
    def regex_user(self, user):
        if self.useregex == 'TRUE':
            user = USER_NON_ALPHA.sub('', user.upper())
            if USER_NON_ALPHA.match(user):
                return "Valid User"
            else:
                return "Invalid User"

#Defining item regex functionality
    def regex_item(self, item):
        if self.useregex == 'TRUE':
            item = USER_NON_ALPHA.sub('', item.upper())
            if USER_NON_ALPHA.match(item):
                return "Valid Item"
            else:
                return "Invalid Item"

#Defining order regex functionality
    def regex_order(self, order):
        if self.useregex == 'TRUE':
            order = USER_NON_ALPHA.sub('', order.upper())
            if USER_NON_ALPHA.match(order):
                return "Valid Order"
            else:
                return "Invalid Order"

#Defining logging functionality
    def logging(self):
        return self.log
