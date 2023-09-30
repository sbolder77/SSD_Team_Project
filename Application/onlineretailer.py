from users import create_user
from users import edit_user
from users import delete_user
from user import authorise_user
from user import load_user

from orders import create_order
from orders import view_order
from orders import edit_order
from orders import delete_order

from items import create_item
from items import view_item
from items import edit_item
from items import delete_item
    
def main():
    login_option = str(input('Choose a following option - 'R' = Register A User Account or 'L' = Login: '))
    if login_option == 'L':
        authorise_user()
        load_user()
        
    else:
        create_login = input("Your account does not exist - Create one now (Y or N): ")
        create_user()
        authorise_user()
        load_user()

if __name__ == '__main__':
    main()
