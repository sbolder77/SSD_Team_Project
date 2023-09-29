import json
from cryptography.fernet import Fernet

# create json readable object
filename = 'system.json'
f = open(filename)
data = json.load(f)

class settings:
    def __init__(self):
        for x in data:
            self.log = x['log']
            self.ssl = x['ssl']
            self.datetimeformat = x['datetimeformat']

    def encryptfile(filename):

    def decryptfile(filename):

    def regexuser():

    def regexorder():

    def regexproduct():



    def authorise_user(user_name):
        return self.test
