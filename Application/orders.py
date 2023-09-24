class OrderDetails:
    def __init__(self, user, order_id, order_items, delivery_type, order_status, basket):
        self.user = user
        self.order_id = order_id
        self.order_items = []
        self.delivery_type = delivery_type
        self.order_status = order_status
        self.basket = []
      
    def user(self, username):
      self.user = username
    
    def create_order(user, order_id, order_items, delivery_type):
        order = OrderDetails(user, order_id, delivery_type)
        # Add order items to the order.
        for product, quantity in order_items:
            order.add_item(product, quantity)
        return

    def add_item(self, product, quantity):
        self.order_items.append({"product": product, "quantity": quantity})



# Example usage:
if __name__ == "__main__":
    OrderDetails.user = "Johnny Dee"
    OrderDetails.order_id = "12345"
    OrderDetails.order_items = "5"
    OrderDetails.delivery_type = "Standard Shipping"
    OrderDetails.order_status = "Item(s) sent for shipping"
    

    # Print order details:
    print(f"Username: {OrderDetails.user}")
    print(f"Order ID: {int(OrderDetails.order_id)}")
    print(f"Number of items in order: {int(OrderDetails.order_items)}")
    print(f"Delivery Type: {OrderDetails.delivery_type}")
    print(f"Order Status: {OrderDetails.order_status}")
