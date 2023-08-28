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
#key = Fernet.generate_key()
#fernet = Fernet(key)
#endregion

def main():
    login_option = str(input('Choose the following option - R = Register or L = Login: '))
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

def create_user(userlist):
    u.create_user(userlist)

def edit_user():
    return u.get_user

def authorise_user():
    return u.get_user

def delete_user():
    return u.get_user

def place_order():
    return u.get_user

def edit_order():
    return u.get_user

def cancel_order():
    return u.get_user

if __name__ == '__main__':
    main()