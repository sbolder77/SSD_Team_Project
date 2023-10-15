#Importing necesary module
import json

#Defining Item() class and downstream functions
class Item():
#Opening/creating an items.json file and loading it as 'item_data'
    with open('items.json', encoding='utf-8') as f:    
        item_data = json.load(f)

#Defining __init__
    def __init__(self):
        pass

#Defining item create function and it's variables
    def create_item(self, itemID_query, itemName_query, itemPrice_query, itemDescription_query, itemStock_query):
        item = {
            "itemID": itemID_query,
            "itemName": itemName_query,
            "itemPrice": itemPrice_query,
            "itemDescription": itemDescription_query,
            "itemStock": itemStock_query
        }
#Appending retrieved variables to items.json file and reporting item created
        Item.item_data['items'].append(item)
        with open('items.json', 'w', encoding='utf-8') as f:
            json.dump(Item.item_data, f, indent=4, separators=(',', ': '))
        print('')
        print("Item created.")

#Defining view item function & printing out objects in items.json
    def view_item(self):
        for i in Item.item_data['items']:
            print('')
            print('Item catalogue...')
            print(f"\nID:{i['itemID']} \nName:{i['itemName']} \nPrice:{i['itemPrice']} \nDescription:{i['itemDescription']} \nStock:{i['itemStock']}")

#Defining item search by item ID function & printing out relevant object in items.json or reporting it unfound
    def search_itemID(self, itemID_query):
        _ID = itemID_query
        finder = False
        for i in Item.item_data['items']:
            if i['itemID'] == _ID:
                print('')
                print('The item you searched for...')
                print(f"\nID:{i['itemID']} \nName:{i['itemName']} \nPrice:{i['itemPrice']} \nDescription:{i['itemDescription']} \nStock:{i['itemStock']}")
                finder = True
                break
        if finder == False:
            print(f"{_ID} cannot be found.")

#Defining item search by item name function & printing out relevant object in items.json or reporting it unfound
    def search_itemName(self, itemName_query):
        _name = itemName_query
        finder = False
        for i in Item.item_data['items']:
            if i['itemName'] == _name:
                print('')
                print('The item you searched for...')
                print(f"\nID:{i['itemID']} \nName:{i['itemName']} \nPrice:{i['itemPrice']} \nDescription:{i['itemDescription']} \nStock:{i['itemStock']}")
                finder = True
                break
        if finder == False:
            print(f"{_name} cannot be found.")

#Defining item search by item price function & printing out relevant object in items.json or reporting it unfound
    def search_itemPrice(self, itemPrice_query):
        _price = itemPrice_query
        for i in Item.item_data['items']:
            if int(i['itemPrice']) == _price:
                print('')
                print('The item you searched for...')
                print(f"\nID:{i['itemID']} \nName:{i['itemName']} \nPrice:{i['itemPrice']} \nDescription:{i['itemDescription']} \nStock:{i['itemStock']}")

#Defining item deletion by item ID function or reporting it unfound
    def delete_item(self, itemID_query):
        _ID = itemID_query
        finder = False
        for i in Item.item_data['items']:
            if i['itemID'] == _ID:
#Deleting (popping) relevant object from items.json
                Item.item_data['items'].pop(Item.item_data['items'].index(i))
                finder = True
                print('')
                print(f"Item with ID {_ID} deleted.")
                break
        with open('items.json', 'w', encoding='utf-8') as f:
            json.dump(Item.item_data, f, indent=4, separators=(',', ': '))
        if finder == False:
            print('')
            print(f"Item with ID {_ID} could not be found.")
            i=i+1
