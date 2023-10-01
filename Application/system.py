#https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/
#https://regex-generator.olafneumann.org

import json
from cryptography.fernet import Fernet
#import filelogging
from datetime import datetime
import re

# create json readable object
filename = 'system.json'
f = open(filename)
data = json.load(f)

#region variables
fernet = Fernet('d35AFvCPEXATL7kNnjz6CD6r20KR9qh5q1L9nZ6bk5k=')
#l = filelogging.LoggingDetails()
USER_NON_ALPHA = re.compile('[A-Z]+_[A-Z]')
ITEM_ALPHA = re.compile('[^A-Z0-9]+')
ORDER_ALPHA = re.compile('[^A-Z0-9]+')
#endregion

class settings:
    def __init__(self):
        for x in data:
            self.log = x['log']
            self.ssl = x['ssl']
            self.datetimeformat = x['datetimeformat']
            self.encrypt = x['encrypt']
            self.useregex = x['useregex']

    def encryptfile(self, filename, user):
        if self.encrypt == 'TRUE':
            with open(filename, 'rb') as file:
                original = file.read()
            encrypted = fernet.encrypt(original)
            with open(filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
            return filename + " has been encrypted"
        #l.write_system_log("SYSTEM", "INFO", filename + " has been encrypted", user)

    def decryptfile(self, filename, user):
        if self.encrypt == 'TRUE':
            with open(filename, 'rb') as enc_file:
                encrypted = enc_file.read()
            decrypted = fernet.encrypt(encrypted)
            with open(filename, 'wb') as decrypted_file:
                decrypted_file.write(decrypted)
            return filename + " has been decrypted"
        #l.write_system_log("SYSTEM", "INFO", filename + " has been decrypted", user)

    def regex_user(self, user):
        if self.useregex == 'TRUE':
            user = USER_NON_ALPHA.sub('', user.upper())
            if USER_NON_ALPHA.match(user):
                return "Valid User"
            else:
                return "Invalid User"
            
    def regex_item(self, item):
        if self.useregex == 'TRUE':
            item = USER_NON_ALPHA.sub('', item.upper())
            if USER_NON_ALPHA.match(item):
                return "Valid Item"
            else:
                return "Invalid Item"
            
    def regex_order(self, order):
        if self.useregex == 'TRUE':
            order = USER_NON_ALPHA.sub('', order.upper())
            if USER_NON_ALPHA.match(order):
                return "Valid Order"
            else:
                return "Invalid Order"
                
    def logging(self):
        return self.log