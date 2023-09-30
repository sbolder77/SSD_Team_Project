#source of code: Codeburst
from flask import Flask
from flask_restful import Api, Resource, reqparse
import logging
import system
import csv
import users

#region objects
l = logging.LoggingDetails()
s = system.settings()
u = users()
#endregion

#region variables
user_data_file = 'users.json'
#syslog = ""
#key = Fernet.generate_key()
#fernet = Fernet(key)
#endregion
 
app = Flask(__name__)
api = Api(app)
 
users = [
    {
        "name": "James",
        "age": 30,
        "occupation": "Network Engineer"
    },
    {
        "name": "Ann",
        "age": 32,
        "occupation": "Doctor"
    },
    {
        "name": "Jason",
        "age": 22,
        "occupation": "Web Developer"
    }
]

class log(Resource):
    def get(self, user, log):
        role = 'A'
        if u.check_users(user) == role:
            if log == 'SYSTEM':
                testlog = l.download_log()
                open(testlog, "r")
                return "opened file: " + testlog, 200
            else:
                return "not authorised to open file: " + testlog, 404


class Item(Resource):
    def get(self, item):
        print('test')
 
class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404
 
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
 
        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400
 
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
 
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
 
        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201
 
    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(User, "/user/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(log, "/log/<string:user><string:log>")
 
app.run(debug=True)
