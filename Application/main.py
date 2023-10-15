'''Online Retailer API - written by team red as part of team project for SSD delivery using tutorials and references from FASTAPI'''

#Importing necessary modules
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
import items

#Quick reference credentials
'''simonbolder - aJ708/F0M*'''
'''liamwillson - hd2_rR3~7g'''
'''fergusnugent - {L9C4\Pz8u'''
'''cathrynpeoples - 30{Ey2@m`S'''
'''customer1 - 99KVC.9Nom'''
'''supplier1 - £mq6|Xd08v'''

#API database
API_USERS_DB = {
    "simonbolder": {
        "username": "bolders", "full_name": "Simon Bolder",
        "hashed_password": "ff7d7a3c8fcc797f6ce23dc2f8c1db57f0a543f4bb79255f028b3e3d78c7dbe1aJ708/F0M*",
        "disabled": False, "role": "A",
    },
    "liamwillson": {
        "username": "willsonl", "full_name": "Liam Willson",
        "hashed_password": "ff7d7a3c8fcc797f6ce23dc2f8c1db57f0a543f4bb79255f028b3e3d78c7dbe1password",
        "disabled": True, "role": "A",
    },
    "fergusnugent": {
        "username": "nugentf", "full_name": "Fergus Nugent",
        "hashed_password": "ff7d7a3c8fcc797f6ce23dc2f8c1db57f0a543f4bb79255f028b3e3d78c7dbe1password",
        "disabled": False, "role": "A",
    },
    "cathrynpeoples": {
        "username": "peoplesc", "full_name": "Cathryn Peoples",
        "hashed_password": "ff7d7a3c8fcc797f6ce23dc2f8c1db57f0a543f4bb79255f028b3e3d78c7dbe1password",
        "disabled": False, "role": "A",
    },
    "customer1": {
        "username": "customer1", "full_name": "A Customer",
        "hashed_password": "ff7d7a3c8fcc797f6ce23dc2f8c1db57f0a543f4bb79255f028b3e3d78c7dbe1password",
        "disabled": False, "role": "C",
    },
    "supplier1": {
        "username": "supplier1", "full_name": "A Supplier",
        "hashed_password": "ff7d7a3c8fcc797f6ce23dc2f8c1db57f0a543f4bb79255f028b3e3d78c7dbe1password",
        "disabled": False, "role": "S",
    },
}

app = FastAPI()

#Constant variables
I_FILE_NAME = 'items.json'
I_FILE = open(I_FILE_NAME)
I_DATA = json.load(I_FILE)

O_FILE_NAME = 'orders.json'
O_FILE = open(O_FILE_NAME)
O_DATA = json.load(O_FILE)

SYS_LOG = 'systemlog.csv'
API_LOG = 'apilog.csv'
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")
HASH_KEY = 'ff7d7a3c8fcc797f6ce23dc2f8c1db57f0a543f4bb79255f028b3e3d78c7dbe1'
LOG = 'TRUE'
AUTHENTICATION = 'TRUE'
SECURE_API = 'TRUE'

#For creating an instance of a user
class User(BaseModel):
    username: str
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None
    role: Union[str, None] = None

#Uses password to check user in API_USERS_DB
class UserInDB(User):
    hashed_password: str

#Checks the password in the db matches the HASH_KEY and entered password
def fake_hash_password(password: str):
    return HASH_KEY + password

#For writing to the API log
def write_api_log(type, level, date_time, message, response):
    if (LOG == 'TRUE'):
        file_object = open('apilog.csv', 'a')
        file_object.write(type + ',' + level + ',' + date_time + ','
                          + message + ',' + response + '\n')
        file_object.close()
        #return "log file updated"

#Used for returning the user from teh db
def get_user(data_base, username: str):
    if username in data_base:
        user_dict = data_base[username]
        return UserInDB(**user_dict)

#Temp solution for generating a token
def fake_decode_token(token):
    user = get_user(API_USERS_DB, token)
    return user

#Gets current user
async def get_current_user(token: Annotated[str, Depends(OAUTH2_SCHEME)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},)
    return user

#Gets current active user
async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Inactive user")
    return current_user

#A simple landing page at the root of the API
@app.get("/")
async def root():
    return {"message": "Welcome to the online retailer API"}

#Used for initial login session and generating a token
@app.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    date_now = datetime.now()
    date_str = date_now.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = API_USERS_DB.get(form_data.username)
    user = UserInDB(**user_dict)
    if not user_dict:
        write_api_log('LOGIN', 'WARNING', date_str,
                      'User does not exist - ' + user.username, '404')
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User does not exist - " + user.username)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        write_api_log('LOGIN', 'WARNING', date_str,
                      'Incorrect password - ' + user.username, '401')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect password - " + user.username)
    write_api_log('LOGIN', 'INFO', date_str,
                  'Authentication susccessful: '
                  + user.username + ' & token_type: bearer', '200')
    return {"access_token": user.username, "token_type": "bearer"}

#Gets the system log csv file for administrators
@app.get("/get-system-log")
def get_system_log(token: Annotated[str, Depends(OAUTH2_SCHEME)], username: str):
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
                          'Not authorised to access system log - ' + user.username  , '401')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Not authorised to access system log - " + user.username)
    if user.disabled is True:
        write_api_log('GETSYSTEMLOG', 'ERROR', date_str,
                      'Account is disabled - ' + user.username  , '401')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Account is disabled - " + user.username)

#Gets the api log in csv for administrators
@app.get("/get-api-log")
def get_api_log(token: Annotated[str, Depends(OAUTH2_SCHEME)], username: str):
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
                          'Not authorised to access API log - ' + user.username  , '401')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Not authorised to access API log - " + user.username)
    if user.disabled is True:
        write_api_log('GETAPILOG', 'ERROR', date_str,
                      'Account is disabled - ' + user.username  , '401')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Account is disabled - " + user.username)

#Gets the items json file for suppliers
@app.get("/get-items")
def get_items(token: Annotated[str, Depends(OAUTH2_SCHEME)], username: str):
    I_FILE_NAME = 'items.json'
    date_now = datetime.now()
    date_str = date_now.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = API_USERS_DB.get(username)
    user = UserInDB(**user_dict)
    if user.disabled is False:
        if user.role == 'S':
            write_api_log('GETITEMS', 'INFO', date_str, 'Retrieved items - '
                          + user.username , '200')
            filepath = os.getcwd() + I_FILE_NAME
            return FileResponse(filepath)
        else:
            write_api_log('GETITEMS', 'ERROR', date_str,
                          'Customers not authorised to access items - '
                          + user.username  , '401')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Customers not authorised to access items - " + user.username)
    if user.disabled is True:
        write_api_log('GETITEMS', 'ERROR', date_str, 'Account is disabled - '
                      + user.username  , '401')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Account is disabled - " + user.username)

#Adds items to the items josn file as a supplier
@app.put("/add-item")
def add_items(token: Annotated[str, Depends(OAUTH2_SCHEME)], username: str, itemID: str, itemName: str, itemPrice: str, itemDescription: str, itemStock: str):
    date_now = datetime.now()
    date_str = date_now.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = API_USERS_DB.get(username)
    user = UserInDB(**user_dict)
    existing_items = []
    if user.disabled is False:
        if user.role == 'S':
            for item in I_DATA['items']:
                existing_items.append(item['itemID'])
            if itemID in existing_items:
                write_api_log('ADDITEMS', 'ERROR', date_str,
                                'Item already exists in db - '
                                + user.username  , '409')
                raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Item already exists")
            else:
                I_DATA['items'].append({
                    "itemID": str(itemID),
                    "itemName": str(itemName),
                    "itemPrice": str(itemPrice),
                    "itemDescription": str(itemDescription),
                    "itemStock": str(itemStock)
                    })
                with open (I_FILE_NAME, 'w') as json_file:
                    json.dump(I_DATA, json_file, indent=4, separators=(',',': '))
                write_api_log('ADDITEMS', 'INFO', date_str,
                                'Item written to db - '
                                + user.username, '201')
                raise HTTPException(status_code=status.HTTP_201_CREATED,
                            detail="Item written to db - " + user.username)
        else:
            write_api_log('ADDITEMS', 'ERROR', date_str,
                          'User not authorised to add items - '
                          + user.username  , '401')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="User not authorised to add items - " + user.username)
    if user.disabled is True:
        write_api_log('ADDITEMS', 'ERROR', date_str, 'Account is disabled - '
                      + user.username  , '401')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Account is disabled - " + user.username)

#Updates the order qty for a specific order as an administrator
@app.put("/update-order-qty")
def update_order_qty(token: Annotated[str, Depends(OAUTH2_SCHEME)], username: str, orderID: str, orderQuantity: str):
    date_now = datetime.now()
    date_str = date_now.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = API_USERS_DB.get(username)
    user = UserInDB(**user_dict)
    if user.disabled is False:
        if user.role == 'A':
            for orders in O_DATA['orders']:
                if orders['orderID'] == str(orderID):
                    current_qty = orders['orderQuantity']
                    orders['orderQuantity'] = str(orderQuantity)
                    with open (O_FILE_NAME, 'w') as json_file:
                        json.dump(O_DATA, json_file, indent=4, separators=(',',': '))
                    write_api_log('UPDATEITEMS', 'INFO', date_str,
                                  'Order ID ' + orders['orderID'] + ' qty updated from - ' + current_qty + ' to '
                                  + orderQuantity + ' - ' + user.username, '202')
                    raise HTTPException(status_code=status.HTTP_202_ACCEPTED,
                                        detail="Order ID " + orders['orderID'] + " qty updated from - " + current_qty + " to "
                                        + orderQuantity + " - " + user.username)
        else:
            write_api_log('UPDATEITEMS', 'ERROR', date_str,
                          'User not authorised to update items - '
                          + user.username  , '401')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="User not authorised to update items - " + user.username)
    if user.disabled is True:
        write_api_log('UPDATEITEMS', 'ERROR', date_str, 'Account is disabled - '
                      + user.username  , '401')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Account is disabled - " + user.username)

#Deletes individual orders from orders json as an administrator
@app.delete("/delete-order")
def delete_order(token: Annotated[str, Depends(OAUTH2_SCHEME)], username: str, orderID: str):
    date_now = datetime.now()
    date_str = date_now.strftime("%d/%m/%Y %H:%M:%S")
    user_dict = API_USERS_DB.get(username)
    user = UserInDB(**user_dict)
    if user.disabled is False:
        if user.role == 'A':
            for orders in O_DATA['orders']:
                if orders['orderID'] == str(orderID):
                    O_DATA['orders'].pop(O_DATA['orders'].index(orders))
                    with open (O_FILE_NAME, 'w') as json_file:
                        json.dump(O_DATA, json_file, indent=4, separators=(',',': '))
                    write_api_log('DELETEITEMS', 'INFO', date_str,
                                  'Order ID ' + orders['orderID'] + ' deleted by - '
                                  + user.username, '202')
                    raise HTTPException(status_code=status.HTTP_202_ACCEPTED,
                                        detail="Order ID " + orders['orderID'] + " deleted by - "
                                  + user.username)
        else:
            write_api_log('DELETEITEMS', 'ERROR', date_str,
                          'User not authorised to delete order - ' + orderID + ' - '
                          + user.username  , '401')
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="User not authorised to delete order - " + orderID + ' - ' + user.username)
    if user.disabled is True:
        write_api_log('DELETEITEMS', 'ERROR', date_str, 'Account is disabled - '
                      + user.username  , '401')
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Account is disabled - " + user.username)
