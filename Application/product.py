class ProductDetails:
  def __init__(self, product_id, product_name, product_description, unit_price, stock_quantity):
    self.product_id = product_id
    self.product_name = product_name
    self.product_description = product_description
    self.unit_price = unit_price
    self.stock_quantity = stock_quantity
    self.is_available = True
      
  def create_product(self, new_product_id):
    # Create an ID for the product.
    self.product = new_product_id

  def update_product_price(self, new_price):
    # Update the price of the product units.
    self.unit_price = new_price

  def get_product(self, product_id):
    # Retrieve the ID of the product.
    self.product_id = product_id

  def update_product_stock(self, quantity):
    # Update the stock of the product.
    self.stock_quantity += quantity

  def delete_product(self, quantity):
    # Remove stock from the product.
    if self.stock_quantity >= quantity:
      self.stock_quantity -= quantity
    else:
      print("Insufficient stock")

  def update_product_status(self, status):
    # Update the status of the product.
    self.product_status = status

  def update_product_description(self, new_description):
    # Update the description of the product.
    self.description = new_description
          
  def mark_as_unavailable(self):
    # Mark the product as unavailable for purchase.
    self.is_available = False

  def mark_as_available(self):
    # Mark the product as available for purchase.
    self.is_available = True
  


  def get_product_info(self):
    # Get information about the product.
    product_info = f"Product ID: {self.product_id}\n"
    product_info += f"Name: {self.product_name}\n"
    product_info += f"Description: {self.product_description}\n"
    product_info += f"Price: £{self.unit_price:.2f}\n"
    product_info += f"Stock Quantity: {self.stock_quantity}\n"
    product_info += f"Availability: {'Available' if self.is_available else 'Unavailable'}\n"
    return product_info


# Example usage:
if __name__ == "__main__":
    # Create a sample product
    product1 = ProductDetails(product_id=1, product_name="Small plant pot", product_description="A small plant pot", unit_price=5, stock_quantity=100)

    # Update product information
    product1.update_product_price(5.50)
    product1.update_product_description("A small brown plant pot")

    # Add and remove stock
    product1.update_product_stock(50)
    product1.delete_product(25)

    # Mark product as avaiable
    product1.mark_as_available()

    # Get product information
    print(product1.get_product_info())
