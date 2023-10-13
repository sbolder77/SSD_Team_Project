import json

class Order():
    with open('orders.json', encoding='utf-8') as f:    
        order_data = json.load(f)
    
    def __init__(self):
        pass

    def create_order(self, orderID_query, orderUsername_query, orderName_query, orderItem_query, orderQuantity_query, orderDeliveryType_query):
        order = {
            "orderID": orderID_query,
            "orderUsername": orderUsername_query,
            "orderName": orderName_query,
            "orderItem": orderItem_query,
            "orderQuantity": orderQuantity_query,
            "orderDeliveryType": orderDeliveryType_query
        }
        Order.order_data['orders'].append(order)
        with open('orders.json', 'w', encoding='utf-8') as f:
            json.dump(Order.order_data, f, indent=4, separators=(',', ': '))
            print ('')
            print("Order created.")

    def view_order(self):
        for i in Order.order_data['orders']:
            print(f"\nID:{i['orderID']} \nUsername:{i['orderUsername']} \nName:{i['orderName']} \nItem:{i['orderItem']} \nQuantity:{i['orderQuantity']} \nDelivery Type:{i['orderDeliveryType']}")

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

    def edit_order(self, orderID_query, orderEdit_choice, new_orderName, new_orderItem, new_orderQuantity, new_orderDeliveryType):
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

    def delete_order(self, orderID_query):
        _orderID = orderID_query
        finder = False
        for i in Order.order_data['orders']:
            if i['orderID'] == _orderID:
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
