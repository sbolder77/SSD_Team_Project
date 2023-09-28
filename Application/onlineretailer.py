import users
import roles
import orders
import logging
from cryptography.fernet import Fernet

#region objects
u = users.UserDetails()
r = roles.RoleDetails()
o = orders.OrderDetails()
l = logging.LoggingDetails()
#endregion

#region variables
loginstatus = bool
userlist = []
user_data_file = 'users.json'
product_data_file = 'product.json'
order_data_file = 'orders.py'
#key = Fernet.generate_key()
#fernet = Fernet(key)
#endregion

def main():
    login_option = str(input('Choose a following option - 'R' = Register or 'L' = Login: '))
    if login_option == 'L':
        user_name = str(input('Please enter your username: '))
        loginstatus = check_user(user_name)
    else:
        create_login = str(input('Your account does not exist - Create one now (Y or N): '))
        if create_login == 'Y':
            id = str(input('Enter an ID: '))
            firstName = str(input('Enter your first name: '))
            surname = str(input('Enter your surname: '))
            password = str(input('Enter a password: '))
            emailaddress = str(input('Enter your email address: '))
            house = str(input('Enter your house number or name: '))
            street = str(input('Enter your street: '))
            town = str(input('Enter your town: '))
            county = str(input('Enter your county: '))
            postcode = str(input('Enter your postcode: '))
            userlist = [id, firstName, surname, password, emailaddress, house, street, town, county, postcode]
            
            createlogin = create_user(userlist)

#Create User
from users.py import create_user

#Edit User
from users.py import edit_user

#Delete User
from users.py import delete_user

#Create Order
from orders.py import create_order

#Edit Order
from orders.py import edit_order

#Delete Order
from orders.py import delete_order

#Create Item
from items.py import create_item

#Edit Item
from items.py import edit_item

#Delete Item
from items.py import delete_item

if __name__ == '__main__':
    main()
