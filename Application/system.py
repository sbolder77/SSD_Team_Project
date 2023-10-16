"""https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
https://regex-generator.olafneumann.org"""

#Importing necessary modules
import json
from datetime import datetime
import re
from cryptography.fernet import Fernet
import filelogging

#Create json readable object
FILE_NAME = 'system.json'
f = open(FILE_NAME)
data = json.load(f)

#Variables
fernet = Fernet('d35AFvCPEXATL7kNnjz6CD6r20KR9qh5q1L9nZ6bk5k=')
USER_NON_ALPHA = re.compile('[A-Z]+_[A-Z]')
ITEM_ALPHA = re.compile('[^A-Z0-9]+')
ORDER_ALPHA = re.compile('[^A-Z0-9]+')

class Settings():
    """Defining Settings() class and downstream functions"""
    def __init__(self):
        """Defining __init__"""
        for x in data:
            self.log = x['log']
            self.ssl = x['ssl']
            self.datetimeformat = x['datetimeformat']
            self.encrypt = x['encrypt']
            self.useregex = x['useregex']

    def encryptfile(self, file_name, user):
        """Defining file encryption functionality"""
        l = filelogging.LoggingDetails()
        if self.encrypt == 'TRUE':
            with open(file_name, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(file_name, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            l.write_system_log("SYSTEM", "INFO", file_name + " has been encrypted", user)
            return file_name + " has been encrypted"

    def decryptfile(self, file_name, user):
        """Defining file decryption functionality"""
        l = filelogging.LoggingDetails()
        if self.encrypt == 'TRUE':
            with open(file_name, 'rb') as enc_file:
                encrypted = enc_file.read()
            decrypted = fernet.encrypt(encrypted)
            with open(file_name, 'wb') as decrypted_file:
                decrypted_file.write(decrypted)
            l.write_system_log("SYSTEM", "INFO", file_name + " has been decrypted", user)
            return file_name + " has been decrypted"

    def regex_user(self, user):
        """Defining user regex functionality"""
        if self.useregex == 'TRUE':
            user = USER_NON_ALPHA.sub('', user.upper())
            if USER_NON_ALPHA.match(user):
                return "Valid User"
            return "Invalid User"

    def regex_item(self, item):
        """Defining item regex functionality"""
        if self.useregex == 'TRUE':
            item = USER_NON_ALPHA.sub('', item.upper())
            if USER_NON_ALPHA.match(item):
                return "Valid Item"

            return "Invalid Item"

    def regex_order(self, order):
        """Defining order regex functionality"""
        if self.useregex == 'TRUE':
            order = USER_NON_ALPHA.sub('', order.upper())
            if USER_NON_ALPHA.match(order):
                return "Valid Order"
            return "Invalid Order"

    def logging(self):
        """Defining logging functionality"""
        return self.log
