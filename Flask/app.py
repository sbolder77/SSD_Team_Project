import json
from flask import Flask
from flask_restful import Api, Resource, reqparse
import os
import sys

cwd = os.getcwd()
# Get the parent directory
app_dir = str(os.path.abspath(os.path.join(cwd, os.pardir)) + '\Application')

# Add the parent directory to sys.path
sys.path.insert(0, app_dir)

ujsonfile = 'users.json'
rjsonfile = 'roles.json'
ojsonfile = 'orders.json'

userjson = os.path.join(app_dir, ujsonfile)
rolejson = os.path.join(app_dir, rjsonfile)
orderjson = os.path.join(app_dir, ojsonfile)



f = open(userjson)
data = json.load(f)



app = Flask(__name__)

@app.route("/")
def home():
    #return "Hello, Simon again!"
    return str(data)

