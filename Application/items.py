import json
from cryptography.fernet import Fernet

items_data_file = 'items.json'
j = open(items_data_file)
data_items = json.load(j)
jsonData_items = data["Items"]

class Item:
    def create_item():
        item_data = []
        with open (jsonData_items, "r") as f:
            temp = json.load(f)
        item_data["item_id"] = input("Item ID: ")
        item_data["item_name"] = input("Item Name: ")
        item_data["item_price"] = input("Item Price: ")
        item_data["item_description"] = input("Item Description: ")
        item_data["item_stock"] = input("Item Stock: ")
        temp.append(item_data)
        with open (jsonData_items, "w") as f:
            json.dump(temp, f, indent=4)

    def view_item():
        with open (jsonData_items, "r") as f:
            temp = json.load(f)
            i = 0
            for entry in temp:
                item_id = entry["item_id"]
                item_name = entry["item_name"]
                item_price = entry["item_price"]
                item_description = entry["item_description"]
                item_stock = entry["item_stock"]
                print (f"Index Number {i}")
                print(f"Item ID: {item_id}")
                print(f"Item Name: {item_name}")
                print(f"Item Price: {item_price}")
                print(f"Item Description: {item_description}")
                print(f"Item Stock: {item_stock}")
                print("\n\n")
                i=i+1
    
    def edit_item():
        pass

    def delete_item():
        Item.view_item()
        new_item = []
        with open (jsonData_items, "r") as f:
            temp = json.load(f)
            data_length = len(temp)-1
        print("Which item do you want to delete (input it's index number)?")
        delete_option = input(f"Select a number 0-{data_length}")
        i=0
        for entry in temp:
            if i == int(delete_option):
                pass
                i=i+1
            else:
                new_item.append(entry)
                i=i+1
