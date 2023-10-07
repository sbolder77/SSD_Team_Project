#https://dev.to/rajshirolkar/fastapi-over-https-for-development-on-windows-2p7d

from fastapi import FastAPI
from datetime import datetime
import os
from fastapi.responses import FileResponse
import json
from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing_extensions import Annotated
from fastapi import FastAPI, Response

log = 'TRUE'
authentication = 'TRUE'

api_users_db = {
    "simonbolder": {
        "username": "bolders",
        "full_name": "Simon Bolder",
        "email": "simon.bolder@email.com",
        "hashed_password": "hashedpassword",
        "disabled": False,
        "role": "A",
    },
    "liamwillson": {
        "username": "willsonl",
        "full_name": "Liam Willson",
        "email": "liam.willson@email.com",
        "hashed_password": "hashedpassword",
        "disabled": True,
        "role": "A",
    },
    "fergusnugent": {
        "username": "nugentf",
        "full_name": "Fergus Nugent",
        "email": "fergus.nugent@email.com",
        "hashed_password": "hashedpassword",
        "disabled": False,
        "role": "A",
    },
    "customer1": {
        "username": "customer1",
        "full_name": "A Customer",
        "email": "customer1@email.com",
        "hashed_password": "hashedpassword",
        "disabled": False,
        "role": "C",
    },
    "supplier1": {
        "username": "supplier1",
        "full_name": "A Supplier",
        "email": "supplier1@email.com",
        "hashed_password": "hashedpassword",
        "disabled": False,
        "role": "S",
    },
}

app = FastAPI()

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

syslog = 'systemlog.csv'
apilog = 'apilog.csv'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#endregion

#region classes
class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    role: Union[str, None] = None

class UserInDB(User):
    hashed_password: str
#endregion

#region functions
def fake_hash_password(password: str):
    return "hashed" + password

def write_api_log(type, level, dt, message, response):
    if (log == 'TRUE'):
        file_object = open('apilog.csv', 'a')
        file_object.write(type + ',' + level + ',' + dt + ',' + message + ',' + response + '\n')
        file_object.close()
        return "log file updated"
    
def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    user = get_user(api_users_db, token)
    return user

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
    ):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
#endregion

#region apiendpoints

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    DT_NOW = datetime.now()
    DT_STR = DT_NOW.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = api_users_db.get(form_data.username)
    if not user_dict:
        write_api_log('LOGIN', 'WARNING', DT_STR, 'Incorrect username or password in db - getting token', '400')
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        write_api_log('LOGIN', 'WARNING', DT_STR, 'Incorrect hashed password - getting token', '400')
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    write_api_log('LOGIN', 'INFO', DT_STR, 'Authentication susccessful - access_token: '+ user.username + ' & token_type: bearer', '200')
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/get-system-log")
def getsystemlog(token: Annotated[str, Depends(oauth2_scheme)], username: str):
    DT_NOW = datetime.now()
    DT_STR = DT_NOW.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = api_users_db.get(username)
    user = UserInDB(**user_dict)
    if user.disabled == False:
        if user.role == 'A':
            write_api_log('GETSYSTEMLOG', 'INFO', DT_STR, 'Retrieved system log - ' + user.username  , '200')
            filepath = os.getcwd() + "/" + syslog
            return FileResponse(filepath)
        else:
            write_api_log('GETSYSTEMLOG', 'ERROR', DT_STR, 'Not authorised to access system log - ' + user.username  , '400')
            raise HTTPException(status_code=400, detail="Not authorised to access system log")
    if user.disabled == True:
        write_api_log('GETSYSTEMLOG', 'ERROR', DT_STR, 'Account is disabled - ' + user.username  , '400')
        raise HTTPException(status_code=400, detail="Account is disabled")

@app.get("/get-api-log")
def getapilog(token: Annotated[str, Depends(oauth2_scheme)], username: str):
    DT_NOW = datetime.now()
    DT_STR = DT_NOW.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = api_users_db.get(username)
    user = UserInDB(**user_dict)
    if user.disabled == False:
        if user.role == 'A':
            write_api_log('GETAPILOG', 'INFO', DT_STR, 'Retrieved API log - ' + user.username  , '200')
            filepath = os.getcwd() + "/" + apilog
            return FileResponse(filepath)
        else:
            write_api_log('GETAPILOG', 'ERROR', DT_STR, 'Not authorised to access API log - ' + user.username  , '400')
            raise HTTPException(status_code=400, detail="Not authorised to access API log")
    if user.disabled == True:
        write_api_log('GETAPILOG', 'ERROR', DT_STR, 'Account is disabled - ' + user.username  , '400')
        raise HTTPException(status_code=400, detail="Account is disabled")
        
@app.get("/get-items")
def getitems(token: Annotated[str, Depends(oauth2_scheme)], username: str):
    DT_NOW = datetime.now()
    DT_STR = DT_NOW.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = api_users_db.get(username)
    user = UserInDB(**user_dict)
    if user.disabled == False:
        if (user.role == 'A' or user.role == 'S'):
            write_api_log('GETITEMS', 'INFO', DT_STR, 'Retrieved items - ' + user.username  , '200')
            filepath = os.getcwd() + "/" + _itemfilename
            return FileResponse(filepath)
        else:
            write_api_log('GETITEMS', 'ERROR', DT_STR, 'Customers not authorised to access items - ' + user.username  , '400')
            raise HTTPException(status_code=400, detail="Customers not authorised to access items")
    if user.disabled == True:
        write_api_log('GETITEMS', 'ERROR', DT_STR, 'Account is disabled - ' + user.username  , '400')
        raise HTTPException(status_code=400, detail="Account is disabled")
        
#endregion
