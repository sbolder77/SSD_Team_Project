import json
from cryptography.fernet import Fernet

import items

orders_data_file = 'orders.json'
j = open(orders_data_file)
data_orders = json.load(j)
jsonData_orders = data["Orders"]

class Order:
    def create_order():
        order_data = []
        with open (jsonData_orders, "r") as f:
            temp = json.load(f)
        order_data["user"] = input("Username: ")
        order_data["order_id"] = input("Order ID: ")
        order_data["order_item"] = input("Item: ")
        while True:
            if order_item not in jsonData_items:
                print("It doesn't appear that this item exists in our inventory.")
                choice_query = input("Enter 1 to try again or 2 to exit: ")
                if choice_query == 1:
                    continue
                else:
                    break    
            else:
                pass
        order_data["order_itemQuantity"] = input("Item Quantity: ")
        while True:
            if order_itemQuantity > item_stock in jsonData_items:
                print("The quantity you have specified is not available.")
                choice_query = input("Enter 1 to try again or 2 to exit: ")
                if choice_query == 1:
                    continue
                else:
                    break    
            else:
                pass
        order_data["order_deliveryType"] = input("Delivery Type (input 'Mail' or 'Pickup'): ")
        while True:
            if order_deliveryType != 'Mail' or 'Pickup':
                print("The delivry method you have specified is not available or is invalid.")
                choice_query = input("Enter 1 to try again or 2 to exit: ")
                if choice_query == 1:
                    continue
                else:
                    break    
            else:
                pass
                
        temp.append(order_data)
        with open (jsonData_orders, "w") as f:
            json.dump(temp, f, indent=4)

    def view_order():
        with open (jsonData_orders, "r") as f:
            temp = json.load(f)
            i = 0
            for entry in temp:
                user = entry["user"]
                order_id = entry["order_id"]
                order_item = entry["order_item"]
                order_itemQuantity = entry["order_itemQuantity"]
                order_deliveryType = entry["order_deliveryType"]
                print (f"Index Number {i}")
                print(f"Username: {user}")
                print(f"Order ID: {order_id}")
                print(f"Item: {order_item}")
                print(f"Item Quantity: {order_itemQuantity}")
                print(f"Delivery Type: {order_deliveryType}")
                print("\n\n")
                i=i+1
    
    def edit_order():
        pass

    def delete_order():
        Order.view_order()
        new_order = []
        with open (jsonData_orders, "r") as f:
            temp = json.load(f)
            data_length = len(temp)-1
        print("Which order do you want to delete (input it's index number)?")
        delete_option = input(f"Select a number 0-{data_length}")
        i=0
        for entry in temp:
            if i == int(delete_option):
                pass
                i=i+1
            else:
                new_order.append(entry)
                i=i+1
