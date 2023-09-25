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

    

def check_user(user_name):
    u.get_user(user_name)
    if bool(u.get_user(user_name)) = True:
        print('Welcome back. Logging you in...')
    else:
        print('Account not found. Please register an account to log in.')
        
        
        

def create_user(userlist):
    u.create_user(userlist)

def edit_user():
    return u.get_user
    if bool(u.get_user) == True:
        edit_user_query = str(input('Do you wish to edit the details associated with your user account (Y or N)? ')
        if order_edit_query = 'Y':
            return u.get_order

def authorise_user():
    return u.get_user

def delete_user():
    return u.get_user
    if bool(u.get_user) == True:
        delete_user_query = str(input('Do you wish to delete your user account (Y or N)? ')
        if order_edit_query = 'Y':
            return u.get_order
        
def place_order():
    return u.get_user
    if bool(u.get_user) == True:
        receiving_address = str(input('Choose a following option - 'C' = Deliver to my current (registered) user address or 'N' = Deliver to a new address'))
        if receiving_address == 'C':
            id = main().id
            firstName = main().firstName
            surname = main().surname
            house = main().house
            street = main().street
            town = main().town
            county = main().county
            postcode = main().postcode

            check_address = str(input('Please confirm the address for delivery is your registered used address (Y or N): ')):
            if check_address == 'Y':
                delivery_address = [id, firstName, surname, house, street, town, county, postcode]

        else:
            id = main().id
            firstName = str(input('Enter the first name for delivery: '))
            surname = str(input('Enter the surname for delivery: '))
            house = str(input('Enter the house number or name for delivery: '))
            street = str(input('Enter the street for delivery: '))
            town = str(input('Enter the town for delivery: '))
            county = str(input('Enter the county for delivery: '))
            postcode = str(input('Enter the postcode for delivery: '))

            check_address = str(input('Please confirm this the correct address for delivery (Y or N): ')):
            if check_address == 'Y':
                delivery_address = [id, firstName, surname, house, street, town, county, postcode]
    
def edit_order():
    return u.get_user
    if bool(u.get_user) == True:
        order_edit_query = str(input('Do you wish to edit your current order (Y or N)? ')
        if order_edit_query = 'Y':
            return u.get_order

def cancel_order():
    return u.get_user
    if bool(u.get_user) == True:
        order_cancel_query = str(input('Do you wish to cancel your current order (Y or N)? ')
        if order_cancel_query = 'Y':
            return u.get_order
                             
        

if __name__ == '__main__':
    main()
