"""Importing necessary modules"""
import sys
import os
import random
import string
from users import User
from admins import Admin
from items import Item
from orders import Order

def main(self):
    """Defining main program"""
    #Defining the user login
    if User.user_data['users'] == []:
        print('')
        print('Welcome. It appears you have no account.')
        print('Input the following information to create an account...')
        print('')
        exit_query = str(input("Enter 1 to continue or 2 to exit (administrators input 'admin'): "))
        if exit_query == str(1):
#Registering a secure user account
            print('')
            print('Firstly, set your login information...')
#Setting a password, depositing it and encrypting it
            user_password_query = input('Input a password: ')
            User.write_password_deposit(self, user_password_query)
            User.write_user_key(self)
            key = User.load_user_key(self)
            User.encrypt(self, 'encrypted_password.csv', key)
#Setting a username
            user_username_query = input('Input a username: ')
#Generating a user ID
            user_id_source = string.ascii_letters
            user_id_suffix = ''.join(random.choice(user_id_source) for i in range(10))
            user_id_query = str(user_username_query) + '.' + str(user_id_suffix)
#Setting other personal information for user account
            print('')
            print('Now, set your personal information...')
            user_name_query = input('Input your name (first and surname): ')
            user_email_address_query = input('Input your email address: ')
            user_house_number_query = input('Input your house number: ')
            user_street_query = input('Input your street: ')
            user_town_query = input('Input your town: ')
            user_country_query = input('Input your country: ')
            user_postcode_query = input('Input your postcode: ')
#Setting payment information for user account
            print('')
            print('Finally, set your payment information...')
            user_bank_name_query = input('Input your bank name: ')
            user_bank_account_name_query = input('Input your bank account name: ')
            user_bank_account_bsb_query = input('Input your bank account BSB: ')
            user_bank_account_number_query = input('Input your bank account number: ')
            print('')
            user_card_name_query = input('Input your card name: ')
            user_card_number_query = input('Input your card number: ')
            user_card_expiry_query = input('Input your card expiry: ')
            user_card_cvc_query = input('Input your card cvc: ')
#Calling create user function which commits inputted information to users.json
            User.create_user(self, user_username_query=user_username_query,
                             user_id_query=user_id_query, user_name_query=user_name_query,
                             user_email_address_query=user_email_address_query,
                             user_house_number_query=user_house_number_query,
                             user_street_query=user_street_query, user_town_query=user_town_query,
                             user_country_query=user_country_query,
                             user_postcode_query=user_postcode_query,
                             user_bank_name_query=user_bank_name_query,
                             user_bank_account_name_query=user_bank_account_name_query,
                             user_bank_account_bsb_query=user_bank_account_bsb_query,
                             user_bank_account_number_query=user_bank_account_number_query,
                             user_card_name_query=user_card_name_query,
                             user_card_number_query=user_card_number_query,
                             user_card_expiry_query=user_card_expiry_query,
                             user_card_cvc_query=user_card_cvc_query)
            print('')
            main(main)
#Defining admin menu option
        elif exit_query == str('admin'):
            if os.path.isfile("key.adminKey"):
                administrator_menu(self)
            else:
                print('')
                print('Administrator access unavailable. You exited...')
#Defining an exit option
        else:
            print('')
            print('You exited.')
            sys.exit()
#Executing a registered user account
    else:
        print('')
        print('Registered user detected. Loading login prompt...')
        print('')
        exit_query = str(input("Enter 1 to continue or 2 to exit (administrators input 'admin'): "))
#Logging in to a user's secure account
        if exit_query == str(1):
            print('')
            print('Login to your account...')
            print('')
            user_username_query = str(input('Input your username: '))
            user_password_query = str(input('Input your password: '))
#Checking inputted user credentials to validate them and authenticate the user
# to access their information and the user menu
            for i in User.user_data['users']:
#Checking username
                if i['user_username'] == user_username_query:
#Checking password by decrypting, checking then re-encrypting password
                    key = User.load_user_key(self)
                    password_verify = User.decrypt(self, "encryptedPassword.csv", key)
                    if user_password_query == str(password_verify):
                        user_menu(self)
                    else:
                        print('')
                        print('Incorrect entries. You exited...')
                        sys.exit()
#Defining an exit option
                else:
                    print('')
                    print('Incorrect entries. You exited...')
                    sys.exit()
#Defining admin menu option
        elif exit_query == str('admin'):
            if os.path.isfile("key.adminKey"):
                administrator_menu(self)
            else:
                print('')
                print('Administrator access unavailable. You exited...')
#Defining an exit option
        else:
            print('')
            print('You exited...')
            sys.exit()

#Defining the user menu
def user_menu(self):
    """Defining the user ID and username to present it in the user menu"""
    for i in User.user_data['users']:
        user_id_query = i['userID']
        user_username_query = i['userUsername']
#Defining the user menu display
    print(f'''
----------------------------------------------------------
Welcome to the shop. Please explore the following options.
          
          Your user ID is: {user_id_query}
            Your username is: {user_username_query}
          
    1. View entire item catalogue
    2. Search catalogue by item ID
    3. Search catalogue by item name
    4. Search catalogue by item price
    
    5. Order an item
    6. View your orders
    7. Search your orders by order ID
    8. Edit an order of yours
    9. Delete an order of yours
    
    10. View your user details
    11. Edit your user details
    12. Delete your user account
          
    13. Exit
----------------------------------------------------------
    ''')
#Offering the user menu choices
    user_choice = str(input('Input the corresponding number to the option you wish to choose: '))
#Defining item catalogue view function
    if user_choice == str(1):
        Item.view_item(self)
        user_menu(self)
#Defining catalogue search by item ID function & exit option
    elif user_choice == str(2):
        print('')
        item_id_query = str(input("Input the item ID you want to search\
                                  for (or input 'exit' for menu): "))
        if item_id_query == 'exit':
            user_menu(self)
        else:
            Item.search_item_id(self, item_id_query=item_id_query)
            user_menu(self)
#Defining catalogue search by item name function & exit option
    elif user_choice == str(3):
        print('')
        item_name_query = str(input("Input the item name you want to search\
                                    for (or input 'exit' for menu): "))
        if item_name_query == 'exit':
            user_menu(self)
        else:
            Item.search_item_name(self, item_name_query=item_name_query)
            user_menu(self)
#Defining catalogue search by item price function & exit option
    elif user_choice == str(4):
        print('')
        item_price_query = int(input("Input the item price you want to search\
                                     for (or input 'exit' for menu): "))
        if item_price_query == 'exit':
            user_menu(self)
        else:
            Item.search_item_price(self, item_price_query=item_price_query)
            user_menu(self)
#Defining catalogue search by item ID function & exit option
    elif user_choice == str(5):
        print('')
#Defining the order ID and username to equal the user's
        for i in User.user_data['users']:
            order_id_query = i['userID']
            order_username_query = i['userUsername']
#Requesting order information input from user
        order_name_query = str(input('Input the name for the order: '))
        order_item_query = str(input('Input the item you want to order: '))
        order_quantity_query = str(input('Input the number of the item you want to order: '))
        order_delivery_type_query = str(input('Input P for pickup OR M for mail delivery: '))
        print('')
        abort_query = str(input("To execute order input '1' or to cancel '2': "))
        if abort_query == str(1):
#Calling create order function which commits inputted information to orders.json
            Order.create_order(self, order_id_query=order_id_query,
                               order_username_query=order_username_query,
                               order_name_query=order_name_query, order_item_query=order_item_query,
                               order_quantity_query=order_quantity_query,
                               order_delivery_type_query=order_delivery_type_query)
            user_menu(self)
#Defining an exit option
        else:
            print('')
            print('Returning to menu...')
            user_menu(self)
#Defining order log view function
    elif user_choice == str(6):
        print('')
        print('Your orders:')
        Order.view_order(self)
        user_menu(self)
#Defining order log search by order ID function & exit option
    elif user_choice == str(7):
        print('')
        order_id_query = str(input("Input the order ID you want to search\
                                   for (or input 'exit' for menu): "))
        if order_id_query == 'exit':
            user_menu(self)
        else:
            Order.search_order_id(self, order_id_query=order_id_query)
            user_menu(self)
#Defining order edit function
    elif user_choice == str(8):
        print('')
#Requesting the user to define which order to edit
        order_id_query = str(input('Input the order ID of the order you wish to edit: '))
#Defining the order edit menu
        for i in Order.order_data['orders']:
            if i['orderID'] == order_id_query:
                print('''Order edit options:
                      
                1. Edit order name
                2. Edit order item & quantity
                3. Edit delivery type

                4. Return to menu
                ''')
#Offering the user menu choices
                order_edit_choice = input('Input the corresponding number\
                                          to the option you wish to choose: ')
#Defining editing of order name function & exit option
                if order_edit_choice == str(1):
                    print('')
                    new_order_name = str(input('Input the new order name: '))
                    Order.edit_order(self, order_id_query=order_id_query,
                                     order_edit_choice=order_edit_choice,
                                     new_order_name=new_order_name,
                                     new_order_item="", new_order_quantity="",
                                     new_order_delivery_type="")
                    user_menu(self)
#Defining editing of order item and quantity function & exit option
                elif order_edit_choice == str(2):
                    print('')
                    new_order_item = str(input('Input the new item: '))
                    new_order_quantity = str(input('Input the new quantity: '))
                    Order.edit_order(self, order_id_query=order_id_query,
                                     order_edit_choice=order_edit_choice, new_order_name="",
                                     new_order_item=new_order_item,
                                     new_order_quantity=new_order_quantity,
                                     new_order_delivery_type="")
                    user_menu(self)
#Defining editing of the delivery type & exit option
                elif order_edit_choice == str(3):
                    print('')
                    new_order_delivery_type = str(input('Input the new delivery type\
                                                        (P for pickup OR M for mail): '))
                    Order.edit_order(self, order_id_query=order_id_query,
                                     order_edit_choice=order_edit_choice, new_order_name="",
                                     new_order_item="", new_order_quantity="",
                                     new_order_delivery_type=new_order_delivery_type)
                    user_menu(self)
                else:
                    user_menu(self)
#Defining the exit if order ID not found
            else:
                print('')
                print('Order ID inputted doesnt exist')
                user_menu(self)
#Defining deletion of an order by ID function & exit option
    elif user_choice == str(9):
        print('')
        order_id_query = str(input("Input the order ID of the order you wish\
                                   to delete (or input 'exit' for menu): "))
        if order_id_query == 'exit':
            user_menu(self)
        else:
            Order.delete_order(self, order_id_query=order_id_query)
            user_menu(self)
#Defining user information view function
    elif user_choice == str(10):
        print('')
        print('Your user data:')
        print('')
        User.view_user(self)
        user_menu(self)
#Defining the user information edit menu
    elif user_choice == str(11):
        print('')
        for i in User.user_data['users']:
            user_id_query = i['user_id'] in User.user_data['users']
            user_edit_choice = print('''Account edit options:
                                    
                1. Edit password
                2. Edit username
                3. Edit name
                4. Edit email address
                5. Edit address
                
                6. Edit bank details
                7. Edit card details

                7. Return to menu
                ''')
#Offering the user menu choices
            user_edit_choice = str(input('Input the corresponding number to the\
                                         option you wish to choose: '))
#Defining editing of user password function & exit option
            if user_edit_choice == str(1):
                print('')
                new_user_password = str(input('Input the new password: '))
                User.edit_user(self, user_id_query=user_id_query, user_edit_choice=user_edit_choice,
                               new_user_password=new_user_password, new_user_username="",
                               new_user_name="", new_user_email_address="",
                               new_user_house_number="", new_user_street="", new_user_town="",
                               new_user_country="", new_user_postcode="", new_user_bank_name="",
                               new_user_bank_account_name="", new_user_bank_account_bsb="",
                               new_user_bank_account_number="", new_user_card_name="",
                               new_user_card_number="", new_user_card_expiry="",
                               new_user_card_cvc="")
                user_menu(self)
#Defining editing of username function & exit option
            elif user_edit_choice == str(2):
                print('')
                new_user_username = str(input('Input the new username: '))
                User.edit_user(self, user_id_query=user_id_query, user_edit_choice=user_edit_choice,
                               new_user_password="", new_user_username=new_user_username,
                               new_user_name="", new_user_email_address="",
                               new_user_house_number="", new_user_street="", new_user_town="",
                               new_user_country="", new_user_postcode="", new_user_bank_name="",
                               new_user_bank_account_name="", new_user_bank_account_bsb="",
                               new_user_bank_account_number="", new_user_card_name="",
                               new_user_card_number="", new_user_card_expiry="",
                               new_user_card_cvc="")
                user_menu(self)
#Defining editing of user name function & exit option
            elif user_edit_choice == str(3):
                print('')
                new_user_name = str(input('Input the new name (first and surname): '))
                User.edit_user(self, user_id_query=user_id_query, user_edit_choice=user_edit_choice,
                               new_user_password="", new_user_username="",
                               new_user_name=new_user_name, new_user_email_address="",
                               new_user_house_number="", new_user_street="", new_user_town="",
                               new_user_country="", new_user_postcode="", new_user_bank_name="",
                               new_user_bank_account_name="", new_user_bank_account_bsb="",
                               new_user_bank_account_number="", new_user_card_name="",
                               new_user_card_number="", new_user_card_expiry="",
                               new_user_card_cvc="")
                user_menu(self)
#Defining editing of user email address function & exit option
            elif user_edit_choice == str(4):
                print('')
                new_user_email_address = str(input('Input the new email address: '))
                User.edit_user(self, user_id_query=user_id_query, user_edit_choice=user_edit_choice,
                               new_user_password="", new_user_username="",
                               new_user_name=new_user_name, new_user_email_address="",
                               new_user_house_number="", new_user_street="", new_user_town="",
                               new_user_country="", new_user_postcode="", new_user_bank_name="",
                               new_user_bank_account_name="", new_user_bank_account_bsb="",
                               new_user_bank_account_number="", new_user_card_name="",
                               new_user_card_number="", new_user_card_expiry="",
                               new_user_card_cvc="")
                user_menu(self)
#Defining editing of user personal information function & exit option
            elif user_edit_choice == str(5):
                print('')
                new_user_house_number = str(input('Input the new house number: '))
                new_user_street = str(input('Input the new street: '))
                new_user_town = str(input('Input the new town: '))
                new_user_country = str(input('Input the new country: '))
                new_user_postcode = str(input('Input the new postcode: '))
                User.edit_user(self, user_id_query=user_id_query, user_edit_choice=user_edit_choice,
                               new_user_password="", new_user_username="",
                               new_user_name=new_user_name, new_user_email_address="",
                               new_user_house_number="", new_user_street="", new_user_town="",
                               new_user_country="", new_user_postcode="", new_user_bank_name="",
                               new_user_bank_account_name="", new_user_bank_account_bsb="",
                               new_user_bank_account_number="", new_user_card_name="",
                               new_user_card_number="", new_user_card_expiry="",
                               new_user_card_cvc="")
                user_menu(self)
#Defining editing of user banking information function & exit option
            elif user_edit_choice == str(6):
                print('')
                new_user_bank_name = str(input('Input the new bank name: '))
                new_user_bank_account_name = str(input('Input the new bank account name: '))
                new_user_bank_account_bsb = str(input('Input the new bank account BSB: '))
                new_user_bank_account_number = str(input('Input the new bank account number: '))
                User.edit_user(self, user_id_query=user_id_query, user_edit_choice=user_edit_choice,
                               new_user_password="", new_user_username="",
                               new_user_name=new_user_name, new_user_email_address="",
                               new_user_house_number="", new_user_street="", new_user_town="",
                               new_user_country="", new_user_postcode="", new_user_bank_name="",
                               new_user_bank_account_name="", new_user_bank_account_bsb="",
                               new_user_bank_account_number="", new_user_card_name="",
                               new_user_card_number="", new_user_card_expiry="",
                               new_user_card_cvc="")
                user_menu(self)
#Defining editing of user card information function & exit option
            elif user_edit_choice == str(7):
                print('')
                new_user_card_name = str(input('Input the new card name: '))
                new_user_card_number = str(input('Input the new card number: '))
                new_user_card_expiry = str(input('Input the new card expiry: '))
                new_user_card_cvc = str(input('Input the new card CVC: '))
                User.edit_user(self, user_id_query=user_id_query, user_edit_choice=user_edit_choice,
                               new_user_password="", new_user_username="",
                               new_user_name=new_user_name, new_user_email_address="",
                               new_user_house_number="", new_user_street="", new_user_town="",
                               new_user_country="", new_user_postcode="", new_user_bank_name="",
                               new_user_bank_account_name="", new_user_bank_account_bsb="",
                               new_user_bank_account_number="", new_user_card_name="",
                               new_user_card_number="", new_user_card_expiry="",
                               new_user_card_cvc="")
                user_menu(self)
            else:
                user_menu(self)
#Defining deletion of a user account by ID function & exit option
    elif user_choice == str(12):
        print('')
        user_id_query = str(input('Input your user ID to delete account: '))
        for i in User.user_data['users']:
            if user_id_query == i['userID']:
                User.delete_user(self, user_id_query=user_id_query)
            else:
                print('')
                print(f'User with ID: {user_id_query} could not be found. Returning to menu...')
                user_menu(self)
#Defining an exit option
    else:
        print('')
        print('You exited. Goodbye.')
        sys.exit()

def administrator_menu(self):
    """Defining the administrator menu"""
    print('')
    print('----------------------------------------------------------')
#Defining administrator authentication
    print('Admin authentication...')
    admin_authenticator = str(input('Input administrator key to continue: '))
    key = Admin.load_admin_key(self)
    admin_verify = User.decrypt(self, "admin_key.csv", key)
    if admin_authenticator == str(admin_verify):
        pass
    else:
        print('')
        print('Incorrect entries. You exited...')
        sys.exit()
#Defining the administrator menu display
    print('''
----------------------------------------------------------
This is an ADMINISTRATOR account view. Please exit if not an administrator.
          
          Administrator actions marked with '!!!'
          
    1. Create an item in the shop catalogue !!!
    2. View entire item catalogue
    3. Search catalogue by item ID
    4. Search catalogue by item name
    5. Search catalogue by item price
    6. Delete an item from the shop catalogue !!!

    7. View all user's orders !!!
    8. Search all user's orders by order ID !!!
    9. Delete any user's order !!!

    10. View all user's details !!!
    11. Edit any user's details !!!
    12. Delete any user's account !!!
    
    13. Edit administrator key !!!
          
    14. Exit
----------------------------------------------------------
    ''')
#Offering the user menu choices
    user_choice = str(input('Input the corresponding number to the option you wish to choose: '))
#Defining item create function
    if user_choice == str(1):
        print('')
        creation_query = str(input("To continue with item creation input '1' or to cancel '2': "))
#Requesting item information input from administrator
        if creation_query == str(1):
            item_id_query = str(input('Set an item ID for the item: '))
            item_name_query = str(input('Set a name for the item: '))
            item_price_query = str(input('Set a price for the item: '))
            item_description_query = str(input('Set a description for the item: '))
            item_stock_query = str(input('Set a stock count for the item: '))
#Calling create item function which commits inputted information to items.json
            Item.create_item(self, item_id_query=item_id_query, item_name_query=item_name_query,
                             item_price_query=item_price_query,
                             item_description_query=item_description_query,
                             item_stock_query=item_stock_query)
            administrator_menu(self)
        else:
            administrator_menu(self)
#Defining item catalogue view function
    elif user_choice == str(2):
        Item.view_item(self)
        administrator_menu(self)
#Defining catalogue search by item ID function & exit option
    elif user_choice == str(3):
        print('')
        item_id_query = str(input("Input the item ID you want to\
                                  search for (or input 'exit' for menu): "))
        if item_id_query == 'exit':
            administrator_menu(self)
        else:
            Item.search_item_id(self, item_id_query=item_id_query)
            administrator_menu(self)
#Defining catalogue search by item name function & exit option
    elif user_choice == str(4):
        print('')
        item_name_query = str(input("Input the item name you want to search for\
                                    (or input 'exit' for menu): "))
        if item_name_query == 'exit':
            administrator_menu(self)
        else:
            Item.search_item_name(self, item_name_query=item_name_query)
            administrator_menu(self)
#Defining catalogue search by item price function & exit option
    elif user_choice == str(5):
        print('')
        item_price_query = int(input("Input the item price you want to search for\
                                     (or input 'exit' for menu): "))
        if item_price_query == 'exit':
            administrator_menu(self)
        else:
            Item.search_item_price(self, item_price_query=item_price_query)
            administrator_menu(self)
#Defining catalogue search by item ID function & exit option
    elif user_choice == str(6):
        print('')
        item_id_query = str(input("Input item ID of item to be\
                                  deleted (or input 'exit' for menu): "))
        if item_id_query == 'exit':
            administrator_menu(self)
        else:
            Item.delete_item(self, item_id_query=item_id_query)
            administrator_menu(self)
#Defining user's orders view function
    elif user_choice == str(7):
        print('')
        print('All users orders:')
        Order.view_order(self)
        administrator_menu(self)
#Defining search by order ID function & exit option
    elif user_choice == str(8):
        print('')
        order_id_query = str(input("Input the order ID you want to\
                                   search for (or input 'exit' for menu): "))
        if order_id_query == 'exit':
            administrator_menu(self)
        else:
            Order.search_order_id(self, order_id_query=order_id_query)
            administrator_menu(self)
#Defining search by order ID function & exit option
    elif user_choice == str(9):
        print('')
        order_id_query = str(input("Input the order ID of the order you\
                                   wish to delete (or input 'exit' for menu): "))
        if order_id_query == 'exit':
            administrator_menu(self)
        else:
            Order.delete_order(self, order_id_query=order_id_query)
            administrator_menu(self)
#Defining view of user's function & exit option
    elif user_choice == str(10):
        print('')
        print('All user accounts:')
        User.view_user(self)
        administrator_menu(self)
#Defining edit any user by user ID function & exit option
    elif user_choice == str(11):
        print('')
        user_id_query = str(input("Input the user ID you want to change the details for: "))
#Defining user edit options menu
        for i in User.user_data['users']:
            if user_id_query == i['userID']:
                print('')
                user_edit_choice = print('''Account edit options:
                                    
                    1. Edit password
                    2. Edit username
                    3. Edit name
                    4. Edit email address
                    5. Edit address
                
                    6. Edit bank details
                    7. Edit card details

                    7. Return to menu
                    ''')
#Defining user edit options menu
                user_edit_choice = str(input('Input the corresponding number\
                                             to the option you wish to choose: '))
#Defining editing of user's password function & exit option
                if user_edit_choice == str(1):
                    print('')
                    new_user_password = str(input('Input the new password: '))
                    User.edit_user(self, user_id_query=user_id_query,
                                   user_edit_choice=user_edit_choice, new_user_password="",
                                   new_user_username="", new_user_name=new_user_name,
                                   new_user_email_address="", new_user_house_number="",
                                   new_user_street="", new_user_town="", new_user_country="",
                                   new_user_postcode="", new_user_bank_name="",
                                   new_user_bank_account_name="", new_user_bank_account_bsb="",
                                   new_user_bank_account_number="", new_user_card_name="",
                                   new_user_card_number="", new_user_card_expiry="",
                                   new_user_card_cvc="")
                    administrator_menu(self)
#Defining editing of user's username function & exit option
                if user_edit_choice == str(2):
                    print('')
                    new_user_username = str(input('Input the new username: '))
                    User.edit_user(self, user_id_query=user_id_query,
                                   user_edit_choice=user_edit_choice, new_user_password="",
                                   new_user_username="", new_user_name=new_user_name,
                                   new_user_email_address="", new_user_house_number="",
                                   new_user_street="", new_user_town="", new_user_country="",
                                   new_user_postcode="", new_user_bank_name="",
                                   new_user_bank_account_name="", new_user_bank_account_bsb="",
                                   new_user_bank_account_number="", new_user_card_name="",
                                   new_user_card_number="", new_user_card_expiry="",
                                   new_user_card_cvc="")
                    administrator_menu(self)
#Defining editing of user's name function & exit option
                elif user_edit_choice == str(3):
                    print('')
                    new_user_name = str(input('Input the new name (first and surname): '))
                    User.edit_user(self, user_id_query=user_id_query,
                                   user_edit_choice=user_edit_choice, new_user_password="",
                                   new_user_username="", new_user_name=new_user_name,
                                   new_user_email_address="", new_user_house_number="",
                                   new_user_street="", new_user_town="", new_user_country="",
                                   new_user_postcode="", new_user_bank_name="",
                                   new_user_bank_account_name="", new_user_bank_account_bsb="",
                                   new_user_bank_account_number="", new_user_card_name="",
                                   new_user_card_number="", new_user_card_expiry="",
                                   new_user_card_cvc="")
                    administrator_menu(self)
#Defining editing of user's email address function & exit option
                elif user_edit_choice == str(4):
                    print('')
                    new_user_email_address = str(input('Input the new email address: '))
                    User.edit_user(self, user_id_query=user_id_query,
                                   user_edit_choice=user_edit_choice, new_user_password="",
                                   new_user_username="", new_user_name=new_user_name,
                                   new_user_email_address="", new_user_house_number="",
                                   new_user_street="", new_user_town="", new_user_country="",
                                   new_user_postcode="", new_user_bank_name="",
                                   new_user_bank_account_name="", new_user_bank_account_bsb="",
                                   new_user_bank_account_number="", new_user_card_name="",
                                   new_user_card_number="", new_user_card_expiry="",
                                   new_user_card_cvc="")
                    administrator_menu(self)
#Defining editing of user's personal information function & exit option
                elif user_edit_choice == str(5):
                    print('')
                    new_user_house_number = str(input('Input the new house number: '))
                    new_user_street = str(input('Input the new street: '))
                    new_user_town = str(input('Input the new town: '))
                    new_user_country = str(input('Input the new country: '))
                    new_user_postcode = str(input('Input the new postcode: '))
                    User.edit_user(self, user_id_query=user_id_query,
                                   user_edit_choice=user_edit_choice, new_user_password="",
                                   new_user_username="", new_user_name=new_user_name,
                                   new_user_email_address="", new_user_house_number="",
                                   new_user_street="", new_user_town="", new_user_country="",
                                   new_user_postcode="", new_user_bank_name="",
                                   new_user_bank_account_name="", new_user_bank_account_bsb="",
                                   new_user_bank_account_number="", new_user_card_name="",
                                   new_user_card_number="", new_user_card_expiry="",
                                   new_user_card_cvc="")
                    administrator_menu(self)
#Defining editing of user's banking information function & exit option
                elif user_edit_choice == str(6):
                    print('')
                    new_user_bank_name = str(input('Input the new bank name: '))
                    new_user_bank_account_name = str(input('Input the new bank account name: '))
                    new_user_bank_account_bsb = str(input('Input the new bank account BSB: '))
                    new_user_bank_account_number = str(input('Input the new bank account number: '))
                    User.edit_user(self, user_id_query=user_id_query,
                                   user_edit_choice=user_edit_choice, new_user_password="",
                                   new_user_username="", new_user_name=new_user_name,
                                   new_user_email_address="", new_user_house_number="",
                                   new_user_street="", new_user_town="", new_user_country="",
                                   new_user_postcode="", new_user_bank_name="",
                                   new_user_bank_account_name="", new_user_bank_account_bsb="",
                                   new_user_bank_account_number="", new_user_card_name="",
                                   new_user_card_number="", new_user_card_expiry="",
                                   new_user_card_cvc="")
                    administrator_menu(self)
#Defining editing of user's card information function & exit option
                elif user_edit_choice == str(7):
                    print('')
                    new_user_card_name = str(input('Input the new card name: '))
                    new_user_card_number = str(input('Input the new card number: '))
                    new_user_card_expiry = str(input('Input the new card expiry: '))
                    new_user_card_cvc = str(input('Input the new card CVC: '))
                    User.edit_user(self, user_id_query=user_id_query,
                                   user_edit_choice=user_edit_choice, new_user_password="",
                                   new_user_username="", new_user_name=new_user_name,
                                   new_user_email_address="", new_user_house_number="",
                                   new_user_street="", new_user_town="", new_user_country="",
                                   new_user_postcode="", new_user_bank_name="",
                                   new_user_bank_account_name="", new_user_bank_account_bsb="",
                                   new_user_bank_account_number="", new_user_card_name="",
                                   new_user_card_number="", new_user_card_expiry="",
                                   new_user_card_cvc="")
                    administrator_menu(self)
                else:
                    administrator_menu(self)
#Defining user deletion by user ID function & exit option
    elif user_choice == str(12):
        print('')
        user_id_query = str(input('Input the user ID of the user\
                                  account you want to delete account: '))
        for i in User.user_data['users']:
            if user_id_query == i['userID']:
                User.delete_user(self, user_id_query=user_id_query)
            else:
                print('')
                print(f'User with ID: {user_id_query} could not be found. Returning to menu...')
                administrator_menu(self)
#Describing administrator key edit method
    elif user_choice == str(13):
        print('')
        print('Run adminCreator.py script through backend to change administrator key.')
        administrator_menu(self)
#Defining an exit option
    else:
        print('')
        print('You exited. Goodbye.')
        sys.exit()

#Run program
if __name__ == '__main__':
    main(main)
