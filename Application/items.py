import json

#itemID_query = int(input(""))
#itemName_query = input("")
#itemPrice_query = int(input(""))
#itemDescription_query = input("")
#itemStock_query = int(input(""))

#new_itemID = int(input(""))
#new_itemName = input("")
#new_itemPrice = int(input(""))
#new_itemDescription = input("")
#new_itemStock = int(input(""))

items_data_file = 'items.json'
f = open(items_data_file)
item_data = json.load(f)

class Item():
    def __init__(self):
        pass

    def create_item(self, itemID_query, itemName_query, itemPrice_query, itemDescription_query, itemStock_query):
        item = {
            "itemID": itemID_query,
            "itemName": itemName_query,
            "itemPrice": itemPrice_query,
            "itemDescription": itemDescription_query,
            "itemStock": itemStock_query
        }
        item_data['items'].append(item)
        with open('items.json', 'w') as f:
            json.dump(item_data, f, indent=4, separators=(',', ': '))
            print("Item created.")

    def view_item(self):
        for i in item_data['items']:
            print(f"ID:{i['itemID']} | Name:{i['itemName']} | Price:{i['itemPrice']} | Description:{i['itemDescription']} | Stock:{i['itemStock']}")

    def search_itemID(self):
        _ID = itemID_query
        finder = False
        for i in item_data['items']:
            if i['itemID'] == _ID:
                print(f"ID:{i['itemID']} \nName:{i['itemName']} \nPrice:{i['itemPrice']} \nDescription:{i['itemDescription']} \n Stock:{i['itemStock']}")
                finder = True
                break
        if finder == False:
            print(f"{_ID} cannot be found.")

    def search_itemName(self):
        _name = itemName_query
        finder = False
        for i in item_data['items']:
            if i['itemName'] == _name:
                print(f"ID:{i['itemID']} \nName:{i['itemName']} \nPrice:{i['itemPrice']} \nDescription:{i['itemDescription']} \n Stock:{i['itemStock']}")
                finder = True
                break
        if finder == False:
            print(f"{_name} cannot be found.")

    def search_itemPrice(self):
        _price = itemPrice_query
        for i in item_data['items']:
            if i['itemPrice'] <= _price:
                print(
                    f"ID:{i['itemID']} | Name:{i['itemName']} | Price:{i['itemPrice']} | Description:{i['itemDescription']} | Stock:{i['itemStock']}")

    def edit_item(self):
        for i in item_data['items']:
            if i['itemID'] == itemID_query:
                i['itemID'] == new_itemID
            elif i['itemName'] == itemName_query:
                i['itemName'] == new_itemName
            elif i['itemPrice'] == itemPrice_query:
                i['itemPrice'] == new_itemPrice
            elif i['itemDescription'] == itemDescription_query:
                i['itemID'] == new_itemDescription
            elif i['itemStock'] == itemStock_query:
                i['itemStock'] == new_itemStock
            else:
                print("Cannot be found.")
        with open('items.json', 'w') as f:
            json.dump(item_data, f, indent=4, separators=(',', ': '))
            print(f"Update made.")

    def delete_item(self):
        _ID = itemID_query
        finder = False
        for i in item_data['items']:
            if i['itemID'] == _ID:
                item_data['items'].pop(item_data['items'].index(i))
                finder = True
                print(f"{_ID} deleted.")
                break
        with open('items.json', 'w') as f:
            json.dump(item_data, f, indent=4, separators=(',', ': '))
        if finder == False:
            print(f"{_ID} could not be found.")
                i=i+1
