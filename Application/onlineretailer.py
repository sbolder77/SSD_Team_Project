import users
import items
import orders
import settings
import logging
from cryptography.fernet import Fernet

def user_menu():
    pass

def admin_menu():
    pass
    
def main():
    login_option = str(input('Choose a following option - 'R' = Register A User Account or 'L' = Login: '))
    if login_option == 'L':
        if authorise_user() == True:
            user_menu()

        else:
            admin_menu()
        
    else:
        create_login = str(input('Your account does not exist - Create one now (Y or N): '))
        create_user()
        if authorise_user() == True:
            user_menu()

        else:
            admin_menu()

#Create User
from users import create_user

#Edit User
from users import edit_user

#Delete User
from users import delete_user

#authorise user
from user import authorise_user

#Create Order
from orders import create_order

#View Order
from orders import view_order

#Edit Order
from orders import edit_order

#Delete Order
from orders import delete_order

#Create Item
from items import create_item

#View Item
from items import view_item

#Edit Item
from items import edit_item

#Delete Item
from items import delete_item

if __name__ == '__main__':
    main()
