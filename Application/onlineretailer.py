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
    1. View item catalogue
    2. Search catalogue by item ID
    3. Search cataogue by item name
    4. Search catalogue by item price
    
    5. Order an item
    6. View your orders
    7. Search your orders by order ID
    8. Edit an order of yours
    9. Delete an order of yours
    
    10. Edit your user details
    11. Delete your user account''')

    choice = str(input('Input the corresponding number to the option you wish to choose: '))
    if user_choice = int(1):
        Items.view_item()
    elif user_choice == int(2):
        Items.search_itemID()
    elif user_choice == int(3):
        Items.search_itemName()
    elif user_choice == int(4):
        Items.search_itemPrice()
    elif user_choice == int(5):
        Orders.create_order()
    elif user_choice == int(6):
        Orders.view_order()
    elif user_choice == int(7):
        Orders.search_orderID()
    elif user_choice == int(8):
        print('''Order edit options...
        1. Edit order name
        2. Edit order ID
        3. Edit order item & quantity
        4. Edit order delivery type
    
        5. Return to menu''')
        edit_order_choice = str(input('Input the corresponding number to the option you wish to choose: '))
        if edit_order_choice = 1:
            orderName_query = str(input('Input the name of the order you wish to edit: '))
            new_orderName = str(input('Input the new name you wish to input: '))
            Orders.edit_order()
        elif edit_order_choice = 2:
            Orders.edit_order()
        elif edit_order_choice = 3:
            orderItem_query = str(input('Input the item in the order you wish to edit: '))
            new_orderItem = str(input('Input the new item you wish to input: '))
            
        

        else:
            user_menu()
                
            





    

        
        orderID_query = str(input('Input the ID of the order you wish to delete: '))
        Orders.edit_order()
    elif user_choice == int(9):
        orderID_query = str(input('Input the ID of the order you wish to delete: '))
        Orders.delete_order()
    elif users_choice == int(10):
        Users.edit_user()
    else:
        Users.delete_user()
        
    '''example for how you would build your arrays from inputs to pass to a function in a class'''
    #item_data = ['test', 'test1', 'test2', 'test3', 'test4']
    #i = items.Item
    #i.create_item(item_data)

if __name__ == '__main__':
    main()
