'''Online Retailer API - written by team red as part of team project for SSD delivery using 
tutorials and references from FASTAPI'''

# Importing necessary modules
import os
import json
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import File, UploadFile

app = FastAPI()

# Constant variables
I_FILE_NAME = 'items.json'
I_FILE = open(I_FILE_NAME)
I_DATA = json.load(I_FILE)

O_FILE_NAME = 'orders.json'
O_FILE = open(O_FILE_NAME)
O_DATA = json.load(O_FILE)

SYS_LOG = 'systemlog.csv'
API_LOG = 'apilog.csv'

@app.get("/")
async def root():
    '''A simple landing page at the root of the API'''
    return {"message": "Welcome to the unsecure online retailer API"}

@app.get("/get-api-log")
def get_api_log():
    '''Gets the api log in csv'''
    filepath = os.getcwd() + "/" + API_LOG
    return FileResponse(filepath)

@app.get("/get-items")
def get_items():
    '''Gets the items json file for suppliers'''
    filepath = os.getcwd() + "/" + I_FILE_NAME
    return FileResponse(filepath)

@app.put("/add-item")
def add_items(item_id: str,
              item_name: str, item_price: str, item_description: str, item_stock: str):
    '''Adds items to the items json file'''
    I_DATA['items'].append({
        "itemID": str(item_id),
        "itemName": str(item_name),
        "itemPrice": str(item_price),
        "itemDescription": str(item_description),
        "itemStock": str(item_stock)
        })
    with open (I_FILE_NAME, 'w', encoding='utf-8') as json_file:
        json.dump(I_DATA, json_file, indent=4, separators=(',',': '))

@app.put("/update-order-qty")
def update_order_qty(order_id: str, order_quantity: str):
    '''Updates the order quantity for a specific order as an administrator'''
    for orders in O_DATA['orders']:
        if orders['orderID'] == str(order_id):
            orders['orderQuantity'] = str(order_quantity)
            with open (O_FILE_NAME, 'w', encoding='utf-8') as json_file:
                json.dump(O_DATA, json_file, indent=4, separators=(',',': '))

@app.delete("/delete-order")
def delete_order(order_id: str):
    '''Deletes individual orders from orders json as an administrator'''
    for orders in O_DATA['orders']:
        if orders['orderID'] == str(order_id):
            O_DATA['orders'].pop(O_DATA['orders'].index(orders))
            with open (O_FILE_NAME, 'w', encoding='utf-8') as json_file:
                json.dump(O_DATA, json_file, indent=4, separators=(',',': '))

@app.post("/upload-file")
async def upload(file: UploadFile = File(...)):
    """For customers to upload a file"""
    cur_dir = os.getcwd() + '/uploads'
    contents = file.file.read()
    with open(os.path.join(cur_dir, file.filename), 'wb') as f:
        f.write(contents)
    file.file.close()
