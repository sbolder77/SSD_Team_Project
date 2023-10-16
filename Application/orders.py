"""Importing necesary module"""
import json

class Order():
    """Defining Order() class and downstream functions"""
#Opening/creating an orders.json file and loading it as 'order_data'
    with open('orders.json', encoding='utf-8') as f:
        order_data = json.load(f)

    def __init__(self):
        """Defining __init__"""

    def create_order(self, order_id_query, order_username_query, order_name_query, order_item_query,
                     order_quantity_query, order_delivery_type_query):
        """Defining order create function and it's variables"""
        order = {
            "order_id": order_id_query,
            "order_username": order_username_query,
            "order_name": order_name_query,
            "order_item": order_item_query,
            "order_quantity": order_quantity_query,
            "order_delivery_type": order_delivery_type_query
        }
#Appending retrieved variables to orders.json file and reporting order created
        Order.order_data['orders'].append(order)
        with open('orders.json', 'w', encoding='utf-8') as f:
            json.dump(Order.order_data, f, indent=4, separators=(',', ': '))
            print ('')
            print("Order created.")

    def view_order(self):
        """Defining view order function & printing out objects in orders.json"""
        for i in Order.order_data['orders']:
            print(f"\nID:{i['orderID']} \nUsername:{i['orderUsername']} \nName:{i['orderName']}")
            print(f"\nItem:{i['orderItem']} \nQuantity:{i['orderQuantity']}")
            print(f"\nDelivery Type:{i['orderDeliveryType']}")

    def search_order_id(self, order_id_query):
        """Defining order search by order ID function & printing out relevant object in 
        orders.json or reporting it unfound"""
        _ID = order_id_query
        finder = False
        for i in Order.order_data['orders']:
            if i['orderID'] == _ID:
                print('')
                print('The order you searched for:')
                print(f"\nID:{i['orderID']} \nUsername:{i['orderUsername']}")
                print(f"\nItem:{i['orderItem']} \nQuantity:{i['orderQuantity']}")
                print(f"\nDelivery Type:{i['orderDeliveryType']}")
                finder = True
                break
        if finder is False:
            print(f"{_ID} order cannot be found.")

    def edit_order(self, order_id_query, order_edit_choice, new_order_name, new_order_item,
                   new_order_quantity, new_order_delivery_type):
        """Defining conditional execution for each user choice & witing edit to file
        Defining item edit function"""
        for i in Order.order_data['orders']:
            if order_edit_choice == str(1):
                if i['order_id'] == order_id_query:
                    i['order_name'] = new_order_name
            elif order_edit_choice == str(2):
                if i['order_id'] == order_id_query:
                    i['order_item'] = new_order_item
                    i['order_quantity'] = new_order_quantity
            else:
                if i['order_id'] == order_id_query:
                    i['order_delivery_type'] = new_order_delivery_type
        with open('orders.json', 'w', encoding='utf-8') as f:
            json.dump(Order.order_data, f, indent=4, separators=(',', ': '))
            print('')
            print('Update made.')

    def delete_order(self, order_id_query):
        """Defining item deletion by item ID function or reporting it unfound"""
        _order_id = order_id_query
        finder = False
        for i in Order.order_data['orders']:
            if i['order_id'] == _order_id:
#Deleting (popping) relevant object from orders.json
                Order.order_data['orders'].pop(Order.order_data['orders'].index(i))
                finder = True
                print('')
                print(f"Order with ID '{_order_id}' was deleted.")
                break
        with open('orders.json', 'w', encoding='utf-8') as f:
            json.dump(Order.order_data, f, indent=4, separators=(',', ': '))
        if finder is False:
            print('')
            print(f"Order with ID '{_order_id}' could not be found.")
