#Importing necesary module
import json

#Defining Order() class and downstream functions
class Order():
#Opening/creating an orders.json file and loading it as 'order_data'
    with open('orders.json', encoding='utf-8') as f:    
        order_data = json.load(f)

#Defining __init__
    def __init__(self):
        pass

#Defining order create function and it's variables
    def create_order(self, orderID_query, orderUsername_query, orderName_query, orderItem_query, orderQuantity_query, orderDeliveryType_query):
        order = {
            "orderID": orderID_query,
            "orderUsername": orderUsername_query,
            "orderName": orderName_query,
            "orderItem": orderItem_query,
            "orderQuantity": orderQuantity_query,
            "orderDeliveryType": orderDeliveryType_query
        }
#Appending retrieved variables to orders.json file and reporting order created
        Order.order_data['orders'].append(order)
        with open('orders.json', 'w', encoding='utf-8') as f:
            json.dump(Order.order_data, f, indent=4, separators=(',', ': '))
            print ('')
            print("Order created.")

#Defining view order function & printing out objects in orders.json
    def view_order(self):
        for i in Order.order_data['orders']:
            print(f"\nID:{i['orderID']} \nUsername:{i['orderUsername']} \nName:{i['orderName']} \nItem:{i['orderItem']} \nQuantity:{i['orderQuantity']} \nDelivery Type:{i['orderDeliveryType']}")

#Defining order search by order ID function & printing out relevant object in orders.json or reporting it unfound
    def search_orderID(self, orderID_query):
        _ID = orderID_query
        finder = False
        for i in Order.order_data['orders']:
            if i['orderID'] == _ID:
                print('')
                print('The order you searched for:')
                print(f"\nID:{i['orderID']} \nUsername:{i['orderUsername']} \nItem:{i['orderItem']} \nQuantity:{i['orderQuantity']} \nDelivery Type:{i['orderDeliveryType']}")
                finder = True
                break
        if finder == False:
            print(f"{_ID} order cannot be found.")

#Defining item edit function
    def edit_order(self, orderID_query, orderEdit_choice, new_orderName, new_orderItem, new_orderQuantity, new_orderDeliveryType):
#Defining conditional execution for each user choice & witing edit to file
        for i in Order.order_data['orders']:
            if orderEdit_choice == str(1):
                if i['orderID'] == orderID_query:
                    i['orderName'] = new_orderName
            elif orderEdit_choice == str(2):
                if i['orderID'] == orderID_query:
                    i['orderItem'] = new_orderItem
                    i['orderQuantity'] = new_orderQuantity
            else:
                if i['orderID'] == orderID_query:
                    i['orderDeliveryType'] = new_orderDeliveryType
        with open('orders.json', 'w', encoding='utf-8') as f:
            json.dump(Order.order_data, f, indent=4, separators=(',', ': '))
            print('')
            print('Update made.')
            
#Defining item deletion by item ID function or reporting it unfound
    def delete_order(self, orderID_query):
        _orderID = orderID_query
        finder = False
        for i in Order.order_data['orders']:
            if i['orderID'] == _orderID:
#Deleting (popping) relevant object from orders.json
                Order.order_data['orders'].pop(Order.order_data['orders'].index(i))
                finder = True
                print('')
                print(f"Order with ID '{_orderID}' was deleted.")
                break
        with open('orders.json', 'w', encoding='utf-8') as f:
            json.dump(Order.order_data, f, indent=4, separators=(',', ': '))
        if finder == False:
            print('')
            print(f"Order with ID '{_orderID}' could not be found.")
