import users
import items
import orders
import system
import filelogging
import string

def main():
    login = str(input('Welcome. Input a following option - R (Register an account) or L (Login to an account): '))
    if login == str('L'):
        userUsername_query = str(input('Please input your username: '))
        userPassword_query = str(input('Please input your password: '))
        Users.authorise_user()
        user_menu()
    else:
        print('Great. Welcome. Please input the following information to create an account...')
        userPassword_query = input('Input a password: ')
        userUsername_query = int(input('Input a username: '))
        userID_query = string.hexdigits
        userFirstname_query = input('Input your first name: ')
        userLastname_query = input('Input your last name: ')
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
        Users.create_user
        user_menu()

def user_menu():
    user_choices = print('''Welcome to the shop. Please explore the following options.
    1. View entire item catalogue
    2. Search catalogue by item ID
    3. Search cataogue by item name
    4. Search catalogue by item price
    
    5. Order an item
    6. View your orders
    7. Search your orders by order ID
    8. Edit an order of yours
    9. Delete an order of yours
    
    10. Edit your user details
    11. Delete your user account
    
    12. Return to menu
    ''')
    choice = str(input('Input the corresponding number to the option you wish to choose: '))
    if user_choice == int(1):
        Items.view_item()
    elif user_choice == int(2):
        itemID_query = str(input('Input the item ID you want to search for: '))
        Items.search_itemID()
    elif user_choice == int(3):
        itemName_query = str(input('Input the item name you want to search for: '))
        Items.search_itemName()
    elif user_choice == int(4):
        itemPrice = str(input('Input the item price you want to search for: '))
        Items.search_itemPrice()
    elif user_choice == int(5):
        orderID_query = string.hexdigits
        orderUser_query = Users.userUsername
        orderItem_query = str(input('Input the item you want to order: '))
        orderQuantity_query = str(input('Input the number of the item you want to order: '))
        orderDeliveryType_query = str(input('Input P for pickup OR M for mail delivery: '))
        Orders.create_order()
    elif user_choice == int(6):
        Orders.view_order()
    elif user_choice == int(7):
        orderID_query = str(input('Input the order ID you want to search for: '))
        Orders.search_orderID()
    elif user_choice == int(8):
        orderID_query = str(input('Input the order ID of the order you wish to edit: '))
        i['orderId'] = orderID_query
        for i in order_data['orders']:
            if i['orderID'] == orderID_query:
                orderedit_choice = print('''Input the corresponding number to the option you wish to choose:
                1. Edit order name
                2. Edit order item & quantity
                3. Edit delivery type

                4. Return to menu
                ''')
                if orderEdit_choice == 1:
                    orderEdit_choice == 1
                    new_orderName = str(input('Input the new order name: '))
                    Orders.edit_order()
                elif orderEdit_choice == 2:
                    orderEdit_choice = 2
                    new_orderItem = str(input('Input the new last name: '))
                    Orders.edit_order()
                elif orderEdit_choice == 3:
                    orderEdit_choice = 3
                    new_orderDeliveryType = str(input('Input the new delivery type (P for pickup OR M for mail): '))
                    Orders.edit_order()
                else:
                    user_menu()
    elif user_choice == int(9):
        Orders.delete_order()
    elif user_choice == int(10):
        userID_query = i['userID'] in user_data['users']
        for i in users_data['users']:
            userEdit_choice = print('''Input the corresponding number to the option you want to choose:
                1. Edit password
                2. Edit username
                3. Edit name
                4. Edit email address
                5. Edit address
                
                6. Edit bank details
                7. Edit card details

                7. Return to menu
                ''')
            if userEdit_choice == 1:
                userEdit_choice == 1
                new_userPassword = str(input('Input the new password: '))
                Users.edit_user()
            elif userEdit_choice == 2:
                userEdit_choice = 2
                new_userUsername = str(input('Input the new username: '))
                Users.edit_user()
            elif userEdit_choice == 3:
                userEdit_choice = 3
                new_userFirstName = str(input('Input the new first name: '))
                new_userLastName = str(input('Input the new last name: '))
                Users.edit_user()
            elif userEdit_choice == 4:
                userEdit_choice = 4
                new_userEmailAddress = str(input('Input the new email address: '))
                Users.edit_user()
            elif userEdit_choice == 5:
                userEdit_choice = 5
                new_userHouseNumber = str(input('Input the new house number: '))
                new_userStreet = str(input('Input the new street: '))
                new_userTown = str(input('Input the new town: '))
                new_userCountry = str(input('Input the new country: '))
                new_userPostcode = str(input('Input the new postcode: '))
                Users.edit_user()
            elif userEdit_choice == 6:
                userEdit_choice == 6
                new_userBankName = str(input('Input the new bank name: '))
                new_userBankAccountName = str(input('Input the new bank account name: '))
                new_userBankAccountBSB = str(input('Input the new bank account BSB: '))
                new_userBankAccountNumber = str(input('Input the new bank account number: '))
                Users.edit_user()
            elif userEdit_choice == 7:
                userEdit_choice == 7
                new_userCardName = str(input('Input the new card name: '))
                new_userCardNumber = str(input('Input the new card number: '))
                new_userCardExpiry = str(input('Input the new card expiry: '))
                new_userCardCVC = str(input('Input the new card CVC: '))
                Users.edit_user()
            else:
                user_menu()
    elif user_choice == int(11):
        Users.delete_user()
    else:
        user_menu()
        
    '''example for how you would build your arrays from inputs to pass to a function in a class'''
    #item_data = ['test', 'test1', 'test2', 'test3', 'test4']
    #i = items.Item
    #i.create_item(item_data)

if __name__ == '__main__':
    main()
