#main.py
#pip install fastapi
#pip install uvicorn
#run cmd and cd to directory of onlineretailerapi.py and then run uvicorn onlineretailerapi:app --reload
from fastapi import FastAPI
import json
import filelogging
from datetime import datetime
from cryptography.fernet import Fernet
from fastapi.responses import FileResponse
import os

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

secretkey = 'd35AFvCPEXATL7kNnjz6CD6r20KR9qh5q1L9nZ6bk5k='

syslog = 'systemlog.csv'
#endregion

app = FastAPI()

@app.get("/get-user")
def getuser(name: str, key: str):
    DT_NOW = datetime.now()
    DT_STR = DT_NOW.strftime("%d/%m/%Y %H:%M:%S")
    if key != secretkey:
        return "authentication key is invalid", 404
    else:
        for user in _userdata:
            if((name == user["ID"]) and (key == secretkey)):
                if(user["Role"] == 'A'):
                    l.write_system_log("SYSTEM", "INFO", DT_STR, "queried users successfully", name)
                    return _userdata, 200
                else:
                    l.write_system_log("SYSTEM", "WARNING", DT_STR, "unauthorised access", name)
                    return "User not authorised", 404
                
@app.get("/get-system-log")
def getsystemlog(key: str):
    if key != secretkey:
        return "authentication key is invalid", 404
    else:
        filepath = os.getcwd() + "/" + syslog
        return FileResponse('systemlog.csv')