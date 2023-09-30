import users
import items
import orders
import settings
import logging
    
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
