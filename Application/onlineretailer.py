from users import User
from items import Item
from orders import Order
#import system
#import filelogging
import string

def main(self):
    login = str(input('Welcome. Input a following option - R (Register an account) or L (Login to an account): '))
    print('')
    if login == str('L'):
        userUsername_query = str(input('Input your username: '))
        userPassword_query = str(input('Input your password: '))
        user_menu(self)
        #authorise = False
        #User.authorise_user(self, authorise=authorise, userUsername_query=userUsername_query, userPassword_query=userPassword_query)
        #if authorise == True:
            #user_menu(self)
        #else:
            #print('Account not found. Register an account.')
            #main(main)
    else:
        print('Great. Welcome. Input the following information to create an account...')
        print('')
        userPassword_query = input('Input a password: ')
        userUsername_query = input('Input a username: ')
        userID_query = string.hexdigits
        userName_query = input('Input your name (first and surname): ')
        userEmailAddress_query = input('Input your email address: ')
        userHouseNumber_query = int(input('Input your house number: '))
        userStreet_query = input('Input your street: ')
        userTown_query = input('Input your town: ')
        userCountry_query = input('Input your country: ')
        userPostcode_query = int(input('Input your postcode: '))
        userBankName_query = input('Input your bank name: ')
        userBankAccountName_query = input('Input your bank account name: ')
        userBankAccountBSB_query = int(input('Input your bank account BSB: '))
        userBankAccountNumber_query = int(input('Input your bank account number: '))
        userCardName_query = input('Input your card name: ')
        userCardNumber_query = int(input('Input your card number: '))
        userCardExpiry_query = int(input('Input your card expiry: '))
        userCardCVC_query = int(input('Input your card cvc: '))
        User.create_user(self, userPassword_query=userPassword_query, userUsername_query=userUsername_query, userID_query=userID_query, userName_query=userName_query, userEmailAddress_query=userEmailAddress_query, userHouseNumber_query=userHouseNumber_query, userStreet_query=userStreet_query, userTown_query=userTown_query, userCountry_query=userCountry_query, userPostcode_query=userPostcode_query, userBankName_query=userBankName_query, userBankAccountName_query=userBankAccountName_query, userBankAccountBSB_query=userBankAccountBSB_query, userBankAccountNumber_query=userBankAccountNumber_query, userCardName_query=userCardName_query, userCardNumber_query=userCardNumber_query, userCardExpiry_query=userCardExpiry_query, userCardCVC_query=userCardCVC_query)
        user_menu(self)

def user_menu(self):
    print('''
----------------------------------------------------------
Welcome to the shop. Please explore the following options.
          
    1. View entire item catalogue
    2. Search catalogue by item ID
    3. Search cataogue by item name
    4. Search catalogue by item price
    
    5. Order an item
    6. View your orders
    7. Search your orders by order ID
    8. Edit an order of yours
    9. Delete an order of yours
    
    10. View your user details
    11. Edit your user details
    12. Delete your user account
    ''')
    user_choice = str(input('Input the corresponding number to the option you wish to choose: '))
    if user_choice == str(1):
        Item.view_item(self)
        user_menu(self)
    elif user_choice == str(2):
        print('')
        itemID_query = str(input('Input the item ID you want to search for: '))
        Item.search_itemID(self, itemID_query=itemID_query)
        user_menu(self)
    elif user_choice == str(3):
        print('')
        itemName_query = str(input('Input the item name you want to search for: '))
        Item.search_itemName(self, itemName_query=itemName_query)
        user_menu(self)
    elif user_choice == str(4):
        print('')
        itemPrice_query = int(input('Input the item price you want to search for: '))
        Item.search_itemPrice(self, itemPrice_query=itemPrice_query)
        user_menu(self)
    elif user_choice == str(5):
        print('')
        orderID_query = string.hexdigits
        orderUsername_query = str(input('Input your username: '))
        orderName_query = str(input('Input the name for the order: '))
        orderItem_query = str(input('Input the item you want to order: '))
        orderQuantity_query = str(input('Input the number of the item you want to order: '))
        orderDeliveryType_query = str(input('Input P for pickup OR M for mail delivery: '))
        Order.create_order(self, orderID_query=orderID_query, orderUsername_query=orderUsername_query, orderName_query=orderName_query, orderItem_query=orderItem_query, orderQuantity_query=orderQuantity_query, orderDeliveryType_query=orderDeliveryType_query)
        user_menu(self)
    elif user_choice == str(6):
        print('')
        print('Your orders:')
        Order.view_order(self)
        user_menu(self)
    elif user_choice == str(7):
        print('')
        orderID_query = str(input('Input the order ID you want to search for: '))
        Order.search_orderID(self, orderID_query=orderID_query)
        user_menu(self)
    elif user_choice == str(8):
        print('')
        orderID_query = str(input('Input the order ID of the order you wish to edit: '))
        for i in Order.order_data['orders']:
            if i['orderID'] == orderID_query:
                print('''Order edit options:
                      
                1. Edit order name
                2. Edit order item & quantity
                3. Edit delivery type

                4. Return to menu
                ''')
                orderEdit_choice = input('Input the corresponding number to the option you wish to choose: ')
                if orderEdit_choice == str(1):
                    print('')
                    new_orderName = str(input('Input the new order name: '))
                    Order.edit_order(self, orderID_query=orderID_query, orderEdit_choice=orderEdit_choice, new_orderName=new_orderName, new_orderItem="", new_orderQuantity="", new_orderDeliveryType="")
                    user_menu(self)
                elif orderEdit_choice == str(2):
                    print('')
                    new_orderItem = str(input('Input the new item: '))
                    new_orderQuantity = str(input('Input the new quantity: '))
                    Order.edit_order(self, orderID_query=orderID_query, orderEdit_choice=orderEdit_choice, new_orderName="", new_orderItem=new_orderItem, new_orderQuantity=new_orderQuantity, new_orderDeliveryType="")
                    user_menu(self)
                elif orderEdit_choice == str(3):
                    print('')
                    new_orderDeliveryType = str(input('Input the new delivery type (P for pickup OR M for mail): '))
                    Order.edit_order(self, orderID_query=orderID_query, orderEdit_choice=orderEdit_choice, new_orderName="", new_orderItem="", new_orderQuantity="", new_orderDeliveryType=new_orderDeliveryType)
                    user_menu(self)
                else:
                    user_menu(self)
            else:
                print('Order ID inputted doesnt exist')
                user_menu(self)
    elif user_choice == str(9):
        print('')
        orderID_query = str(input('Input the order ID of the order you wish to delete: '))
        Order.delete_order(self, orderID_query=orderID_query)
        user_menu(self)
    elif user_choice == str(10):
        print('')
        print('Your user data:')
        print('')
        User.view_user(self)
        user_menu(self)
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
            userEdit_choice = str(input('Input the corresponding number to the option you wish to choose: '))
            if userEdit_choice == str(1):
                print('')
                new_userPassword = str(input('Input the new password: '))
                User.edit_user(self, userID_query=userID_query, userEdit_choice=userEdit_choice, new_userPassword=new_userPassword, new_userUsername="", new_userName="", new_userEmailAddress="", new_userHouseNumber="", new_userStreet="", new_userTown="", new_userCountry="", new_userPostcode="", new_userBankName="", new_userBankAccountName="", new_userBankAccountBSB="", new_userBankAccountNumber="", new_userCardName="", new_userCardNumber="", new_userCardExpiry="", new_userCardCVC="")
                user_menu(self)
            elif userEdit_choice == str(2):
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
    else:
        print('')
        userID_query = str(input("Input your user ID to delete account: "))
        User.delete_user(self, userID_query=userID_query)
        user_menu(self)

if __name__ == '__main__':
    main(main)
