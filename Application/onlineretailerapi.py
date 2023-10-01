#source of code: Codeburst
from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
import filelogging

#region objects
l = filelogging.LoggingDetails()
#endregion

#region variables
_userfilename = 'users.json'
_userf = open(_userfilename)
_userdata = json.load(_userf)

_itemfilename = 'users.json'
_itemf = open(_itemfilename)
_itemdata = json.load(_itemf)

_orderfilename = 'users.json'
_orderf = open(_orderfilename)
_orderdata = json.load(_orderf)
#endregion
 
app = Flask(__name__)
api = Api(app)
 
class User(Resource):
    def get(self, name):
        for user in _userdata:
             if(name == user["ID"]):
                 if(user["Role"] == 'A'):
                    l.write_system_log("SYSTEM", "INFO", "queried users successfully", name)
                    return _userdata, 200
                 else:
                     l.write_system_log("SYSTEM", "WARNING", "unauthorised access", name)
                     return "User not authorised", 404


            #ID = str(user['ID'])
            #if ID == 'boldersa':
            #return ID, 200
            
        #if name == 'boldersa':
            #return _userdata, 200
        #else:
            #return "User not authorised", 404
        
api.add_resource(User, "/user/<string:name>")
 
app.run(debug=True)
