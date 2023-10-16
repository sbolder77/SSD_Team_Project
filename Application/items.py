"""Importing necessary module"""
import json

class Item():
    """Defining Item() class and downstream functions
    Opening/creating an items.json file and loading it as 'item_data"""
    with open('items.json', encoding='utf-8') as f:
        item_data = json.load(f)

    def __init__(self):
        """#Defining __init__"""

    def create_item(self, item_id_query, item_name_query, item_price_query,
                    item_description_query, item_stock_query):
        """Defining item create function and it's variables"""
        item = {
            "itemID": item_id_query,
            "itemName": item_name_query,
            "itemPrice": item_price_query,
            "itemDescription": item_description_query,
            "itemStock": item_stock_query
        }
# Appending retrieved variables to items.json file and reporting item created
        Item.item_data['items'].append(item)
        with open('items.json', 'w', encoding='utf-8') as f:
            json.dump(Item.item_data, f, indent=4, separators=(',', ': '))
        print('')
        print("Item created.")

    def view_item(self):
        """Defining view item function & printing out objects in items.json"""
        for i in Item.item_data['items']:
            print('')
            print('Item catalogue...')
            print(f"\nID:{i['itemID']} \nName:{i['itemName']} \nPrice:{i['itemPrice']}")
            print(f"Description:{i['itemDescription']} \nStock:{i['itemStock']}")

    def search_item_id(self, item_id_query):
        """Defining item search by item ID function & printing out
        relevant object in items.json or reporting it unfound"""
        _id = item_id_query
        finder = False
        for i in Item.item_data['items']:
            if i['itemID'] == _id:
                print('')
                print('The item you searched for...')
                print(f"\nID:{i['itemID']} \nName:{i['itemName']} \nPrice:{i['itemPrice']}")
                print(f"Description:{i['itemDescription']} \nStock:{i['itemStock']}")
                finder = True
                break
        if finder is False:
            print(f"{_id} cannot be found.")

    def search_item_name(self, item_name_query):
        """Defining item search by item name function & printing out relevant object in
        items.json or reporting it unfound"""
        _name = item_name_query
        finder = False
        for i in Item.item_data['items']:
            if i['itemName'] == _name:
                print('')
                print('The item you searched for...')
                print(f"\nID:{i['itemID']} \nName:{i['itemName']} \nPrice:{i['itemPrice']}")
                print(f"Description:{i['itemDescription']} \nStock:{i['itemStock']}")
                finder = True
                break
        if finder is False:
            print(f"{_name} cannot be found.")

    def search_item_price(self, item_price_query):
        """Defining item search by item price function & printing out relevant object
        in items.json or reporting it unfound"""
        _price = item_price_query
        for i in Item.item_data['items']:
            if (i['itemPrice']) == _price:
                print('')
                print('The item you searched for...')
                print(f"\nID:{i['itemID']} \nName:{i['itemName']} \nPrice:{i['itemPrice']}")
                print(f"Description:{i['itemDescription']} \nStock:{i['itemStock']}")

    def delete_item(self, item_id_query):
        """Defining item deletion by item ID function or reporting it unfound"""
        _id = item_id_query
        finder = False
        for i in Item.item_data['items']:
            if i['itemID'] == _id:
                # Deleting (popping) relevant object from items.json
                Item.item_data['items'].pop(Item.item_data['items'].index(i))
                finder = True
                print('')
                print(f"Item with ID {_id} deleted.")
                break
        with open('items.json', 'w', encoding='utf-8') as f:
            json.dump(Item.item_data, f, indent=4, separators=(',', ': '))
        if finder is False:
            print('')
            print(f"Item with ID {_id} could not be found.")
            i=i+1
