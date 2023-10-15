#Importing necessary modules
import sys
import os
from users import User
from admins import Admin
from items import Item
from orders import Order
import random
import string

#Defining main program
def main(self):
#Defining the user login
    if User.user_data['users'] == []:
        print('')
        print('Welcome. It appears you have no account. Input the following information to create an account...')
        print('')
        exit_query = str(input("Enter 1 to continue or 2 to exit (administrators input 'admin'): "))
        if exit_query == str(1):
#Registering a secure user account
            print('')
            print('Firstly, set your login information...')
#Setting a password, depositing it and encrypting it
            userPassword_query = input('Input a password: ')
            User.write_passwordDeposit(self, userPassword_query)
            User.write_userKey(self)
            key = User.load_userKey(self)
            User.encrypt(self, 'encryptedPassword.csv', key)
#Setting a username
            userUsername_query = input('Input a username: ')
#Generating a user ID
            userID_source = string.ascii_letters
            userID_suffix = ''.join(random.choice(userID_source) for i in range(10))
            userID_query = str(userUsername_query) + '.' + str(userID_suffix)
#Setting other personal information for user account
            print('')
            print('Now, set your personal information...')
            userName_query = input('Input your name (first and surname): ')
            userEmailAddress_query = input('Input your email address: ')
            userHouseNumber_query = input('Input your house number: ')
            userStreet_query = input('Input your street: ')
            userTown_query = input('Input your town: ')
            userCountry_query = input('Input your country: ')
            userPostcode_query = input('Input your postcode: ')
#Setting payment information for user account
            print('')
            print('Finally, set your payment information...')
            userBankName_query = input('Input your bank name: ')
            userBankAccountName_query = input('Input your bank account name: ')
            userBankAccountBSB_query = input('Input your bank account BSB: ')
            userBankAccountNumber_query = input('Input your bank account number: ')
            print('')
            userCardName_query = input('Input your card name: ')
            userCardNumber_query = input('Input your card number: ')
            userCardExpiry_query = input('Input your card expiry: ')
            userCardCVC_query = input('Input your card cvc: ')
#Calling create user function which commits inputted information to users.json
            User.create_user(self, userUsername_query=userUsername_query, userID_query=userID_query, userName_query=userName_query, userEmailAddress_query=userEmailAddress_query, userHouseNumber_query=userHouseNumber_query, userStreet_query=userStreet_query, userTown_query=userTown_query, userCountry_query=userCountry_query, userPostcode_query=userPostcode_query, userBankName_query=userBankName_query, userBankAccountName_query=userBankAccountName_query, userBankAccountBSB_query=userBankAccountBSB_query, userBankAccountNumber_query=userBankAccountNumber_query, userCardName_query=userCardName_query, userCardNumber_query=userCardNumber_query, userCardExpiry_query=userCardExpiry_query, userCardCVC_query=userCardCVC_query)
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
            userUsername_query = str(input('Input your username: '))
            userPassword_query = str(input('Input your password: '))
#Checking inputted user credentials to validate them and authenticate the user to access their information and the user menu
            for i in User.user_data['users']:
#Checking username
                if i['userUsername'] == userUsername_query:
#Checking password by decrypting, checking then re-encrypting password
                    key = User.load_userKey(self)
                    passwordVerify = User.decrypt(self, "encryptedPassword.csv", key)
                    if userPassword_query == str(passwordVerify):
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
#Defining the user ID and username to present it in the user menu
    for i in User.user_data['users']:
        userID_query = i['userID']
        userUsername_query = i['userUsername']
#Defining the user menu display
    print(f'''
----------------------------------------------------------
Welcome to the shop. Please explore the following options.
          
          Your user ID is: {userID_query}
            Your username is: {userUsername_query}
          
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
        itemID_query = str(input("Input the item ID you want to search for (or input 'exit' for menu): "))
        if itemID_query == 'exit':
            user_menu(self)
        else: 
            Item.search_itemID(self, itemID_query=itemID_query)
            user_menu(self)
#Defining catalogue search by item name function & exit option
    elif user_choice == str(3):
        print('')
        itemName_query = str(input("Input the item name you want to search for (or input 'exit' for menu): "))
        if itemName_query == 'exit':
            user_menu(self)
        else: 
            Item.search_itemName(self, itemName_query=itemName_query)
            user_menu(self)
#Defining catalogue search by item price function & exit option
    elif user_choice == str(4):
        print('')
        itemPrice_query = int(input("Input the item price you want to search for (or input 'exit' for menu): "))
        if itemPrice_query == 'exit':
            user_menu(self)
        else: 
            Item.search_itemPrice(self, itemPrice_query=itemPrice_query)
            user_menu(self)
#Defining catalogue search by item ID function & exit option
    elif user_choice == str(5):
        print('')
#Defining the order ID and username to equal the user's
        for i in User.user_data['users']:
            orderID_query = i['userID']
            orderUsername_query = i['userUsername']
#Requesting order information input from user
        orderName_query = str(input('Input the name for the order: '))
        orderItem_query = str(input('Input the item you want to order: '))
        orderQuantity_query = str(input('Input the number of the item you want to order: '))
        orderDeliveryType_query = str(input('Input P for pickup OR M for mail delivery: '))
        print('')
        abort_query = str(input("To execute order input '1' or to cancel '2': "))
        if abort_query == str(1):
#Calling create order function which commits inputted information to orders.json
            Order.create_order(self, orderID_query=orderID_query, orderUsername_query=orderUsername_query, orderName_query=orderName_query, orderItem_query=orderItem_query, orderQuantity_query=orderQuantity_query, orderDeliveryType_query=orderDeliveryType_query)
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
        orderID_query = str(input("Input the order ID you want to search for (or input 'exit' for menu): "))
        if orderID_query == 'exit':
            user_menu(self)
        else: 
            Order.search_orderID(self, orderID_query=orderID_query)
            user_menu(self)
#Defining order edit function
    elif user_choice == str(8):
        print('')
#Requesting the user to define which order to edit
        orderID_query = str(input('Input the order ID of the order you wish to edit: '))
#Defining the order edit menu
        for i in Order.order_data['orders']:
            if i['orderID'] == orderID_query:
                print('''Order edit options:
                      
                1. Edit order name
                2. Edit order item & quantity
                3. Edit delivery type

                4. Return to menu
                ''')
#Offering the user menu choices
                orderEdit_choice = input('Input the corresponding number to the option you wish to choose: ')
#Defining editing of order name function & exit option
                if orderEdit_choice == str(1):
                    print('')
                    new_orderName = str(input('Input the new order name: '))
                    Order.edit_order(self, orderID_query=orderID_query, orderEdit_choice=orderEdit_choice, new_orderName=new_orderName, new_orderItem="", new_orderQuantity="", new_orderDeliveryType="")
                    user_menu(self)
#Defining editing of order item and quantity function & exit option
                elif orderEdit_choice == str(2):
                    print('')
                    new_orderItem = str(input('Input the new item: '))
                    new_orderQuantity = str(input('Input the new quantity: '))
                    Order.edit_order(self, orderID_query=orderID_query, orderEdit_choice=orderEdit_choice, new_orderName="", new_orderItem=new_orderItem, new_orderQuantity=new_orderQuantity, new_orderDeliveryType="")
                    user_menu(self)
#Defining editing of the delivery type & exit option
                elif orderEdit_choice == str(3):
                    print('')
                    new_orderDeliveryType = str(input('Input the new delivery type (P for pickup OR M for mail): '))
                    Order.edit_order(self, orderID_query=orderID_query, orderEdit_choice=orderEdit_choice, new_orderName="", new_orderItem="", new_orderQuantity="", new_orderDeliveryType=new_orderDeliveryType)
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
        orderID_query = str(input("Input the order ID of the order you wish to delete (or input 'exit' for menu): "))
        if orderID_query == 'exit':
            user_menu(self)
        else: 
            Order.delete_order(self, orderID_query=orderID_query)
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
            userID_query = i['userID'] in User.user_data['users']
            userEdit_choice = print('''Account edit options:
                                    
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
            userEdit_choice = str(input('Input the corresponding number to the option you wish to choose: '))
#Defining editing of user password function & exit option
            if userEdit_choice == str(1):
                print('')
                new_userPassword = str(input('Input the new password: '))
                User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword=new_userPassword, new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                user_menu(self)
#Defining editing of username function & exit option
            elif userEdit_choice == str(2):
                print('')
                new_userUsername = str(input('Input the new username: '))
                User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername=new_userUsername, new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                user_menu(self)
#Defining editing of user name function & exit option
            elif userEdit_choice == str(3):
                print('')
                new_userName = str(input('Input the new name (first and surname): '))
                User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName=new_userName, new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                user_menu(self)
#Defining editing of user email address function & exit option
            elif userEdit_choice == str(4):
                print('')
                new_userEmailAddress = str(input('Input the new email address: '))
                User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress=new_userEmailAddress, new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                user_menu(self)
#Defining editing of user personal information function & exit option
            elif userEdit_choice == str(5):
                print('')
                new_userHouseNumber = str(input('Input the new house number: '))
                new_userStreet = str(input('Input the new street: '))
                new_userTown = str(input('Input the new town: '))
                new_userCountry = str(input('Input the new country: '))
                new_userPostcode = str(input('Input the new postcode: '))
                User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber=new_userHouseNumber, new_userStreet=new_userStreet, new_userTown=new_userTown, new_userCountry=new_userCountry, new_userPostcode=new_userPostcode, new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                user_menu(self)
#Defining editing of user banking information function & exit option
            elif userEdit_choice == str(6):
                print('')
                new_userBankName = str(input('Input the new bank name: '))
                new_userBankAccountName = str(input('Input the new bank account name: '))
                new_userBankAccountBSB = str(input('Input the new bank account BSB: '))
                new_userBankAccountNumber = str(input('Input the new bank account number: '))
                User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName=new_userBankName, new_userBankAccountName=new_userBankAccountName, new_userBankAccountBSB=new_userBankAccountBSB, new_userBankAccountNumber=new_userBankAccountNumber, new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                user_menu(self)
#Defining editing of user card information function & exit option
            elif userEdit_choice == str(7):
                print('')
                new_userCardName = str(input('Input the new card name: '))
                new_userCardNumber = str(input('Input the new card number: '))
                new_userCardExpiry = str(input('Input the new card expiry: '))
                new_userCardCVC = str(input('Input the new card CVC: '))
                User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName=new_userCardName, new_userCardNumber=new_userCardNumber, new_userCardExpiry=new_userCardExpiry, new_userCardCVC=new_userCardCVC)
                user_menu(self)
            else:
                user_menu(self)
#Defining deletion of a user account by ID function & exit option
    elif user_choice == str(12):
        print('')
        userID_query = str(input('Input your user ID to delete account: '))
        for i in User.user_data['users']:
            if userID_query == i['userID']:
                User.delete_user(self, userID_query=userID_query)
            else:
                print('')
                print(f'User with ID: {userID_query} could not be found. Returning to menu...')
                user_menu(self)
#Defining an exit option
    else:
        print('')
        print('You exited. Goodbye.')
        sys.exit()


#Defining the administrator menu
def administrator_menu(self):
    print('')
    print('----------------------------------------------------------')
#Defining administrator authentication
    print('Admin authentication...')
    adminAuthenticator = str(input('Input administrator key to continue: '))
    key = Admin.load_adminKey(self)
    adminVerify = User.decrypt(self, "adminKey.csv", key)
    if adminAuthenticator == str(adminVerify):
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
    
    13. View your administrator details !!!
    14. Edit your administrator details !!!
    15. Delete your administrator account !!!
          
    16. Exit
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
            itemID_query = str(input('Set an item ID for the item: '))
            itemName_query = str(input('Set a name for the item: '))
            itemPrice_query = str(input('Set a price for the item: '))
            itemDescription_query = str(input('Set a description for the item: '))
            itemStock_query = str(input('Set a stock count for the item: '))
#Calling create item function which commits inputted information to items.json
            Item.create_item(self, itemID_query=itemID_query, itemName_query=itemName_query, itemPrice_query=itemPrice_query, itemDescription_query=itemDescription_query, itemStock_query=itemStock_query)
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
        itemID_query = str(input("Input the item ID you want to search for (or input 'exit' for menu): "))
        if itemID_query == 'exit':
            administrator_menu(self)
        else: 
            Item.search_itemID(self, itemID_query=itemID_query)
            administrator_menu(self)
#Defining catalogue search by item name function & exit option
    elif user_choice == str(4):
        print('')
        itemName_query = str(input("Input the item name you want to search for (or input 'exit' for menu): "))
        if itemName_query == 'exit':
            administrator_menu(self)
        else: 
            Item.search_itemName(self, itemName_query=itemName_query)
            administrator_menu(self)
#Defining catalogue search by item price function & exit option
    elif user_choice == str(5):
        print('')
        itemPrice_query = int(input("Input the item price you want to search for (or input 'exit' for menu): "))
        if itemPrice_query == 'exit':
            administrator_menu(self)
        else: 
            Item.search_itemPrice(self, itemPrice_query=itemPrice_query)
            administrator_menu(self)
#Defining catalogue search by item ID function & exit option
    elif user_choice == str(6):
        print('')
        itemID_query = str(input("Input item ID of item to be deleted (or input 'exit' for menu): "))
        if itemID_query == 'exit':
            administrator_menu(self)
        else:
            Item.delete_item(self, itemID_query=itemID_query)
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
        orderID_query = str(input("Input the order ID you want to search for (or input 'exit' for menu): "))
        if orderID_query == 'exit':
            administrator_menu(self)
        else: 
            Order.search_orderID(self, orderID_query=orderID_query)
            administrator_menu(self)
#Defining search by order ID function & exit option
    elif user_choice == str(9):
        print('')
        orderID_query = str(input("Input the order ID of the order you wish to delete (or input 'exit' for menu): "))
        if orderID_query == 'exit':
            user_menu(self)
        else:
            Order.delete_order(self, orderID_query=orderID_query)
            user_menu(self)
    elif user_choice == str(10):
        print('')
        print('All user accounts:')
        User.view_user(self)
        administrator_menu(self)
    elif user_choice == str(11):
        print('')
        userID_query = str(input("Input the user ID you want to change the details for: "))
        for i in User.user_data['users']:
            if userID_query == i['userID']:
                print('')
                userEdit_choice = print('''Account edit options:
                                    
                    1. Edit password
                    2. Edit username
                    3. Edit name
                    4. Edit email address
                    5. Edit address
                
                    6. Edit bank details
                    7. Edit card details

                    7. Return to menu
                    ''')
                userEdit_choice = str(input('Input the corresponding number to the option you wish to choose: '))
                if userEdit_choice == str(1):
                    print('')
                    new_userPassword = str(input('Input the new password: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword=new_userPassword, new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                if userEdit_choice == str(2):
                    print('')
                    new_userUsername = str(input('Input the new username: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername=new_userUsername, new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                elif userEdit_choice == str(3):
                    print('')
                    new_userName = str(input('Input the new name (first and surname): '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName=new_userName, new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                elif userEdit_choice == str(4):
                    print('')
                    new_userEmailAddress = str(input('Input the new email address: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress=new_userEmailAddress, new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                elif userEdit_choice == str(5):
                    print('')
                    new_userHouseNumber = str(input('Input the new house number: '))
                    new_userStreet = str(input('Input the new street: '))
                    new_userTown = str(input('Input the new town: '))
                    new_userCountry = str(input('Input the new country: '))
                    new_userPostcode = str(input('Input the new postcode: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber=new_userHouseNumber, new_userStreet=new_userStreet, new_userTown=new_userTown, new_userCountry=new_userCountry, new_userPostcode=new_userPostcode, new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                elif userEdit_choice == str(6):
                    print('')
                    new_userBankName = str(input('Input the new bank name: '))
                    new_userBankAccountName = str(input('Input the new bank account name: '))
                    new_userBankAccountBSB = str(input('Input the new bank account BSB: '))
                    new_userBankAccountNumber = str(input('Input the new bank account number: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName=new_userBankName, new_userBankAccountName=new_userBankAccountName, new_userBankAccountBSB=new_userBankAccountBSB, new_userBankAccountNumber=new_userBankAccountNumber, new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                elif userEdit_choice == str(7):
                    print('')
                    new_userCardName = str(input('Input the new card name: '))
                    new_userCardNumber = str(input('Input the new card number: '))
                    new_userCardExpiry = str(input('Input the new card expiry: '))
                    new_userCardCVC = str(input('Input the new card CVC: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName=new_userCardName, new_userCardNumber=new_userCardNumber, new_userCardExpiry=new_userCardExpiry, new_userCardCVC=new_userCardCVC)
                    user_menu(self)
                else:
                    user_menu(self)
    elif user_choice == str(12):
        print('')
        userID_query = str(input('Input the user ID of the user account you want to delete account: '))
        for i in User.user_data['users']:
            if userID_query == i['userID']:
                User.delete_user(self, userID_query=userID_query)
            else:
                print('')
                print(f'User with ID: {userID_query} could not be found. Returning to menu...')
                user_menu(self)
    elif user_choice == str(13):
        print('')
        userID_query = str(input('Input the administrator ID to view the administrator account details: '))
        if userID_query == 'exit':
            user_menu(self)
        else:
            User.search_userID(self, userID_query=userID_query)
            user_menu(self)
    elif user_choice == str(14):
        print('')
        userID_query = str(input("Input your administrator ID you want to change the details for: "))
        for i in User.user_data['users']:
            if userID_query == i['userID']:
                print('')
                userEdit_choice = print('''Account edit options:
                                    
                    1. Edit password
                    2. Edit username
                    3. Edit name
                    4. Edit email address
                    5. Edit address
                
                    6. Edit bank details
                    7. Edit card details

                    7. Return to menu
                    ''')
                userEdit_choice = str(input('Input the corresponding number to the option you wish to choose: '))
                if userEdit_choice == str(1):
                    print('')
                    new_userPassword = str(input('Input the new password: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword=new_userPassword, new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                if userEdit_choice == str(2):
                    print('')
                    new_userUsername = str(input('Input the new username: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername=new_userUsername, new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                elif userEdit_choice == str(3):
                    print('')
                    new_userName = str(input('Input the new name (first and surname): '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName=new_userName, new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                elif userEdit_choice == str(4):
                    print('')
                    new_userEmailAddress = str(input('Input the new email address: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress=new_userEmailAddress, new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                elif userEdit_choice == str(5):
                    print('')
                    new_userHouseNumber = str(input('Input the new house number: '))
                    new_userStreet = str(input('Input the new street: '))
                    new_userTown = str(input('Input the new town: '))
                    new_userCountry = str(input('Input the new country: '))
                    new_userPostcode = str(input('Input the new postcode: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber=new_userHouseNumber, new_userStreet=new_userStreet, new_userTown=new_userTown, new_userCountry=new_userCountry, new_userPostcode=new_userPostcode, new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                elif userEdit_choice == str(6):
                    print('')
                    new_userBankName = str(input('Input the new bank name: '))
                    new_userBankAccountName = str(input('Input the new bank account name: '))
                    new_userBankAccountBSB = str(input('Input the new bank account BSB: '))
                    new_userBankAccountNumber = str(input('Input the new bank account number: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName=new_userBankName, new_userBankAccountName=new_userBankAccountName, new_userBankAccountBSB=new_userBankAccountBSB, new_userBankAccountNumber=new_userBankAccountNumber, new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                    user_menu(self)
                elif userEdit_choice == str(7):
                    print('')
                    new_userCardName = str(input('Input the new card name: '))
                    new_userCardNumber = str(input('Input the new card number: '))
                    new_userCardExpiry = str(input('Input the new card expiry: '))
                    new_userCardCVC = str(input('Input the new card CVC: '))
                    User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword="", new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName=new_userCardName, new_userCardNumber=new_userCardNumber, new_userCardExpiry=new_userCardExpiry, new_userCardCVC=new_userCardCVC)
                    user_menu(self)
                else:
                    user_menu(self)
    elif user_choice == str(15):
        print('')
        userID_query = str(input('WARNING: This action can only be restored manually through the back-end. Input your administrator ID to delete your account: '))
        for i in User.user_data['users']:
            if userID_query == i['userID']:
                User.delete_user(self, userID_query=userID_query)
            else:
                print('')
                print(f'User with ID: {userID_query} could not be found. Returning to menu...')
                user_menu(self)
    else:
        print('')
        print('You exited. Goodbye.')
        sys.exit()

if __name__ == '__main__':
    main(main)
