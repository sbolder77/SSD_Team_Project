#https://dev.to/rajshirolkar/fastapi-over-https-for-development-on-windows-2p7d
'''Online Retailer API'''

import os
import json
from datetime import datetime
from typing import Union
from pydantic import BaseModel
from typing_extensions import Annotated
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#from fastapi import FastAPI, Response

#region database
API_USERS_DB = {
    "simonbolder": {
        "username": "bolders", "full_name": "Simon Bolder",
        "hashed_password": "hashedpassword",
        "disabled": False, "role": "A",
    },
    "liamwillson": {
        "username": "willsonl", "full_name": "Liam Willson",
        "hashed_password": "hashedpassword",
        "disabled": True, "role": "A",
    },
    "fergusnugent": {
        "username": "nugentf", "full_name": "Fergus Nugent",
        "hashed_password": "hashedpassword",
        "disabled": False, "role": "A",
    },
    "customer1": {
        "username": "customer1", "full_name": "A Customer",
        "hashed_password": "hashedpassword",
        "disabled": False, "role": "C",
    },
    "supplier1": {
        "username": "supplier1", "full_name": "A Supplier",
        "hashed_password": "hashedpassword",
        "disabled": False, "role": "S",
    },
}
#endregion

app = FastAPI()

#region constant variables
U_FILE_NAME = 'users.json'
U_FILE = open(U_FILE_NAME)
U_DATA = json.load(U_FILE)

I_FILE_NAME = 'items.json'
I_FILE = open(I_FILE_NAME)
I_DATA = json.load(I_FILE)

O_FILE_NAME = 'users.json'
O_FILE = open(O_FILE_NAME)
O_DATA = json.load(O_FILE)

SYS_LOG = 'systemlog.csv'
API_LOG = 'apilog.csv'
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")
LOG = 'TRUE'
AUTHENTICATION = 'TRUE'
#endregion

#region classes
class User(BaseModel):
    '''user data'''
    username: str
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    role: Union[str, None] = None

class UserInDB(User):
    '''user in db'''
    hashed_password: str
#endregion

#region functions
def fake_hash_password(password: str):
    '''password'''
    return "hashed" + password

def write_api_log(type, level, date_time, message, response):
    '''write log'''
    if (LOG == 'TRUE'):
        file_object = open('apilog.csv', 'a')
        file_object.write(type + ',' + level + ',' + date_time + ','
                          + message + ',' + response + '\n')
        file_object.close()
        #return "log file updated"

def get_user(data_base, username: str):
    '''get user'''
    if username in data_base:
        user_dict = data_base[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    '''decode'''
    user = get_user(API_USERS_DB, token)
    return user

async def get_current_user(token: Annotated[str, Depends(OAUTH2_SCHEME)]):
    '''get current user'''
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
    '''get active user'''
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Inactive user")
    return current_user

#async def get_date():
    #'''get data'''
    #date_now = datetime.now()
    #date_str = date_now.strftime("%d/%m/%Y %H:%M:%S")
    #return date_str
#endregion

#region apiendpoints

@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    '''login'''
    date_now = datetime.now()
    date_str = date_now.strftime("%d/%m/%Y %H:%M:%S")
    #date_time = get_date()
    user_dict = API_USERS_DB.get(form_data.username)
    if not user_dict:
        write_api_log('LOGIN', 'WARNING', date_str,
                      'Incorrect username or password in db - getting token', '400')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        write_api_log('LOGIN', 'WARNING', date_str,
                      'Incorrect hashed password - getting token', '400')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")
    write_api_log('LOGIN', 'INFO', date_str,
                  'Authentication susccessful - access_token: '
                  + user.username + ' & token_type: bearer', '200')
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/get-system-log")
def get_system_log(token: Annotated[str, Depends(OAUTH2_SCHEME)], username: str):
    '''get system log'''
    #date_time = get_date()
    date_now = datetime.now()
    date_str = date_now.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = API_USERS_DB.get(username)
    user = UserInDB(**user_dict)
    if user.disabled is False:
        if user.role == 'A':
            write_api_log('GETSYSTEMLOG', 'INFO', date_str,
                          'Retrieved system log - ' + user.username  , '200')
            file_path = os.getcwd() + "/" + SYS_LOG
            return FileResponse(file_path)
        else:
            write_api_log('GETSYSTEMLOG', 'ERROR', date_str,
                          'Not authorised to access system log - ' + user.username  , '400')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Not authorised to access system log")
    if user.disabled is True:
        write_api_log('GETSYSTEMLOG', 'ERROR', date_str,
                      'Account is disabled - ' + user.username  , '400')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Account is disabled")

@app.get("/get-api-log")
def get_api_log(token: Annotated[str, Depends(OAUTH2_SCHEME)], username: str):
    '''get api log'''
    #date_time = get_date()
    date_now = datetime.now()
    date_str = date_now.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = API_USERS_DB.get(username)
    user = UserInDB(**user_dict)
    if user.disabled is False:
        if user.role == 'A':
            write_api_log('GETAPILOG', 'INFO', date_str,
                          'Retrieved API log - ' + user.username  , '200')
            filepath = os.getcwd() + "/" + API_LOG
            return FileResponse(filepath)
        else:
            write_api_log('GETAPILOG', 'ERROR', date_str,
                          'Not authorised to access API log - ' + user.username  , '400')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Not authorised to access API log")
    if user.disabled is True:
        write_api_log('GETAPILOG', 'ERROR', date_str,
                      'Account is disabled - ' + user.username  , '400')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Account is disabled")

@app.get("/get-items")
def get_items(token: Annotated[str, Depends(OAUTH2_SCHEME)], username: str):
    '''get items'''
    #date_time = get_date()
    date_now = datetime.now()
    date_str = date_now.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = API_USERS_DB.get(username)
    user = UserInDB(**user_dict)
    if user.disabled is False:
        if user.role in ('A', 'S'):
            write_api_log('GETITEMS', 'INFO', date_str, 'Retrieved items - '
                          + user.username , '200')
            filepath = os.getcwd() + "/" + I_FILE_NAME
            return FileResponse(filepath)
        else:
            write_api_log('GETITEMS', 'ERROR', date_str,
                          'Customers not authorised to access items - '
                          + user.username  , '400')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Customers not authorised to access items")
    if user.disabled is True:
        write_api_log('GETITEMS', 'ERROR', date_str, 'Account is disabled - '
                      + user.username  , '400')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Account is disabled")

#endregion