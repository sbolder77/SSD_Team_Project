import json

#orderID_query = int(input(""))
#orderUser_query = input("")
#orderItem_query = input("")
#orderQuantity_query = int(input(""))
#orderDeliveryType_query = input("")

#new_orderID = int(input(""))
#new_orderUser = input("")
#new_orderItem = input("")
#new_orderQuantity = int(input(""))
#new_orderDeliveryType = input("")

orders_data_file = 'orders.json'
f = open(orders_data_file)
order_data = json.load(f)

class Order():
    def __init__(self):
        pass

    def create_order(self, orderID_query, orderUser_query, orderItem_query, orderQuantity_query, orderDeliveryType_query):
        order = {
            "orderID": orderID_query,
            "orderUser": orderUser_query,
            "orderItem": orderItem_query,
            "orderQuantity": orderQuantity_query,
            "orderDeliveryType": orderDeliveryType_query
        }
        order_data['orders'].append(order)
        with open('orders.json', 'w') as f:
            json.dump(order_data, f, indent=4, separators=(',', ': '))
            print("Order created.")

    def view_order(self):
        for i in order_data['orders']:
            print(f"ID:{i['orderID']} | User:{i['orderUser']} | Item:{i['orderItem']} | Quantity:{i['orderQuantity']} | Delivery Type:{i['orderDeliveryType']}")

    def search_orderID(self):
        _ID = orderID_query
        finder = False
        for i in order_data['orders']:
            if i['orderID'] == _ID:
                print(f"ID:{i['orderID']} | User:{i['orderUser']} | Item:{i['orderItem']} | Quantity:{i['orderQuantity']} | Delivery Type:{i['orderDeliveryType']}")
                finder = True
                break
        if finder == False:
            print(f"{_ID} cannot be found.")

    def edit_order(self, orderID_query, orderUser_query, orderItem_query, orderQuantity_query, orderDeliveryType_query, new_orderID, new_orderUser, new_orderItem, new_orderQuantity, new_orderDeliveryType):
        for i in order_data['orders']:
            if i['orderID'] == orderID_query:
                i['orderID'] == new_orderID
            elif i['orderUser'] == orderUser_query:
                print("User allocated to order cannot be changed.")
            elif i['orderItem'] == orderItem_query:
                print("Delete order to change the item ordered.")
            elif i['orderQuantity'] == orderQuantity_query:
                i['orderQuantity'] == new_orderQuantity
            elif i['orderDeliveryType'] == orderDeliveryType_query:
                i['orderDeliveryType'] == new_orderDeliveryType
            else:
                print("Cannot be found.")
        with open('orders.json', 'w') as f:
            json.dump(order_data, f, indent=4, separators=(',', ': '))
            print(f"Update made.")

    def delete_item(self):
        _ID = orderID_query
        finder = False
        for i in order_data['orders']:
            if i['orderID'] == _ID:
                order_data['orders'].pop(order_data['orders'].index(i))
                finder = True
                print(f"{_ID} deleted.")
                break
        with open('orders.json', 'w') as f:
            json.dump(order_data, f, indent=4, separators=(',', ': '))
        if finder == False:
            print(f"{_ID} could not be found.")
