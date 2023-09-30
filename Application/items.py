import json

#from cryptography.fernet import Fernet
#key - Fernet.generate_key()

file = "./items.json"

class Item():
    def __init__(self, item_data):
        self.item_data = item_data[item_data]

    def create_item(self):
        item_data = []
        with open (file, "r") as f:
            temp = json.load(f)
        item_data["item_id"] = input("Item ID: ")
        item_data["item_name"] = input("Item Name: ")
        item_data["item_price"] = input("Item Price: ")
        item_data["item_description"] = input("Item Description: ")
        item_data["item_stock"] = input("Item Stock: ")
        temp.append(item_data)
        with open (file, "w") as f:
            json.dump(temp, f, indent=4)

    def view_item(self):
        with open (file, "r") as f:
            temp = json.load(f)
            i = 0
            for entry in temp:
                item_id = entry["item_id"]
                item_name = entry["item_name"]
                item_price = entry["item_price"]
                item_description = entry["item_description"]
                item_stock = entry["item_stock"]
                print(f"Index Number {i}")
                print(f"Item ID: {item_id}")
                print(f"Item Name: {item_name}")
                print(f"Item Price: {item_price}")
                print(f"Item Description: {item_description}")
                print(f"Item Stock: {item_stock}")
                print("\n\n")
                i=i+1
    
    def edit_item(self):
        Item.view_item(self)
        with open (file, "r") as f:
            temp = json.load(f)

            while True:
                choice_query = input("Input which item you wish to edit (if you wish to exit, input 'exit'): ")
                if choice_query == str("Item ID"):
                    item_data["item_id"] = input("Item ID: ")
                    print("Item ID changed.")
                    continue
                
                elif choice_query == str("Item Name"):
                    item_data["item_name"] = input("Item Name: ")
                    print("Item Name changed.")
                    continue

                elif choice_query == str("Item Description"):
                    item_data["item_description"] = input("Item Description: ")
                    print("Item Description changed.")
                    continue
                
                elif choice_query == str("Item Stock"):
                    user_data["item_stock"] = input("Item Stock: ")
                    print("Item Stock changed.")
                    continue
                
                else:
                    break

    def delete_item(self):
        Item.view_item(self)
        new_item = []
        with open (file, "r") as f:
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
