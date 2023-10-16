"""Importing necessary modules"""
import sys
import json
from cryptography.fernet import Fernet
#import filelogging

#region objects
#l = filelogging.LoggingDetails()
#endregion

class User():
    """Defining User() class and downstream functions"""
#Opening/creating an users.json file and loading it as 'user_data'
    with open('users.json', encoding='utf-8') as f:
        user_data = json.load(f)

#Defining __init__
    def __init__(self):
        pass

    def create_user(self, user_username_query, user_id_query, user_name_query,
                    user_email_address_query, user_house_number_query, user_street_query,
                    user_town_query, user_country_query, user_postcode_query,
                    user_bank_name_query, user_bank_account_name_query, user_bank_account_bsb_query,
                    user_bank_account_number_query, user_card_name_query, user_card_number_query,
                    user_card_expiry_query, user_card_cvc_query):
        """Defining user create function and it's variables"""
        user = {
            "user_username": user_username_query,
            "userID": user_id_query,
            "userName": user_name_query,
            "userEmailAddress": user_email_address_query,
            "userHouseNumber": user_house_number_query,
            "userStreet": user_street_query,
            "userTown": user_town_query,
            "userCountry": user_country_query,
            "userPostcode": user_postcode_query,
            "userBankName": user_bank_name_query,
            "userBankAccountName": user_bank_account_name_query,
            "userBankAccountBSB": user_bank_account_bsb_query,
            "userBankAccountNumber": user_bank_account_number_query,
            "userCardName": user_card_name_query,
            "userCardNumber": user_card_number_query,
            "userCardExpiry": user_card_expiry_query,
            "userCardCVC": user_card_cvc_query
        }
#Appending retrieved variables to users.json file and reporting item created
        User.user_data['users'].append(user)
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(User.user_data, f, indent=4, separators=(',', ': '))
            print('')
            print('User created.')
            print('----------------------------------------------------------')
        #l.write_system_log('USER', 'INFO', userID_query + ' - created', userName_query)

    def view_user(self):
        """Defining view user function & printing out objects in users.json"""
        for i in User.user_data['users']:
            print(f"Username:{i['user_username']} \nID:{i['user_id']} \nName:{i['user_name']}")
            print(f"\nEmail Address:{i['user_email_address']}")
            print(f"\nHouse Number:{i['user_house_number']}")
            print(f"\nStreet:{i['user_street']} \nTown:{i['user_town']}")
            print(f"\nCountry:{i['user_country']}")
            print(f"\nPostcode:{i['user_postcode']} \nBank Name:{i['user_bank_name']}")
            print(f"\nBank Account Name:{i['user_bank_account_name']}")
            print(f"\nBank Account BSB:{i['user_bank_account_bsb']}")
            print(f"\nBank Account Number:{i['userBank_cccount_number']}")
            print(f"\nCard Name:{i['user_card_name']} \nCard Number:{i['user_card_number']}")
            print(f"\nCard Expiry{i['user_card_expiry']} \nCard CVC:{i['user_card_cvc']}")

    def search_user_username(self, user_username_query):
        """#Defining user search by username function & printing out relevant object in users.json 
        or reporting it unfound"""
        _username = user_username_query
        finder = False
        for i in User.user_data['users']:
            if i['userUsername'] == _username:
                print(f"Username:{i['user_username']} \nID:{i['user_id']} \nName:{i['user_name']}")
                print(f"\nEmail Address:{i['user_email_address']}")
                print(f"\nHouse Number:{i['user_house_number']} \nStreet:{i['user_street']}")
                print(f"\nTown:{i['user_town']} \nCountry:{i['user_country']}")
                print(f"\nPostcode:{i['user_postcode']} \nBank Name:{i['user_bank_name']}")
                print(f"\nBank Account Name:{i['user_bank_account_name']}")
                print(f"\nBank Account BSB:{i['user_bank_account_bsb']}")
                print(f"\nBank Account Number:{i['userBank_cccount_number']}")
                print(f"\nCard Name:{i['user_card_name']} \nCard Number:{i['user_card_number']}")
                print(f"\nCard Expiry{i['user_card_expiry']} \nCard CVC:{i['user_card_cvc']}")
                finder = True
                break
        if finder is False:
            print(f"{_username} cannot be found.")

    def search_user_id(self, user_id_query):
        """Defining user search by user ID function & printing out relevant object in users.json or 
        reporting it unfound"""
        _ID = user_id_query
        finder = False
        for i in User.user_data['users']:
            if i['user_id'] == _ID:
                print(f"Username:{i['user_username']} \nID:{i['user_id']} \nName:{i['user_name']}")
                print(f"\nEmail Address:{i['user_email_address']}")
                print(f"\nHouse Number:{i['user_house_number']} \nStreet:{i['user_street']}")
                print(f"\nTown:{i['user_town']} \nCountry:{i['user_country']}")
                print(f"\nPostcode:{i['user_postcode']} \nBank Name:{i['user_bank_name']}")
                print(f"\nBank Account Name:{i['user_bank_account_name']}")
                print(f"\nBank Account BSB:{i['user_bank_account_bsb']}")
                print(f"\nBank Account Number:{i['userBank_cccount_number']}")
                print(f"\nCard Name:{i['user_card_name']} \nCard Number:{i['user_card_number']}")
                print(f"\nCard Expiry{i['user_card_expiry']} \nCard CVC:{i['user_card_cvc']}")
                finder = True
                break
        if finder is False:
            print(f'{_ID} cannot be found.')

    def edit_user(self, user_id_query, user_edit_choice, new_user_password, new_user_username,
                  new_user_name, new_user_email_address, new_user_house_number, new_user_street,
                  new_user_town, new_user_country, new_user_postcode,
                  new_user_bank_name, new_user_bank_account_name, new_user_bank_account_bsb,
                  new_user_bank_account_number, new_user_card_name, new_user_card_number,
                  new_user_card_expiry, new_user_card_cvc):
        """Defining user edit function"""
#Defining conditional execution for each user choice & witing edit to file
        if user_edit_choice == str(1):
            User.write_password_deposit(self, new_user_password)
            User.write_user_key(self)
            key = User.load_user_key(self)
            User.encrypt(self, 'encrypted_password.csv', key)
        for i in User.user_data['users']:
            if user_edit_choice == str(2):
                if i['user_id'] == user_id_query:
                    i['user_username'] = new_user_username
            elif user_edit_choice == str(3):
                if i['user_id'] == user_id_query:
                    i['user_name'] = new_user_name
            elif user_edit_choice == str(4):
                if i['user_id'] == user_id_query:
                    i['user_email_address'] = new_user_email_address
            elif user_edit_choice == str(5):
                if i['userID'] == user_id_query:
                    i['user_house_number'] = new_user_house_number
                    i['user_street'] = new_user_street
                    i['user_town'] = new_user_town
                    i['user_country'] = new_user_country
                    i['user_postcode'] = new_user_postcode
                    i['user_house_number'] = new_user_house_number
            elif user_edit_choice == str(6):
                if i['user_id'] == user_id_query:
                    i['user_bank_name'] = new_user_bank_name
                    i['user_bank_account_name'] = new_user_bank_account_name
                    i['user_bank_account_bsb'] = new_user_bank_account_bsb
                    i['user_bank_account_number'] = new_user_bank_account_number
            else:
                if i['user_id'] == user_id_query:
                    i['user_card_name'] = new_user_card_name
                    i['user_card_number'] = new_user_card_number
                    i['user_card_expiry'] = new_user_card_expiry
                    i['user_card_cvc'] = new_user_card_cvc
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(User.user_data, f, indent=4, separators=(',', ': '))
            print('')
            print('Update made.')

    def delete_user(self, user_id_query):
        """#Defining item deletion by item ID function or reporting it unfound"""
        _user_id = user_id_query
        for i in User.user_data['users']:
            if i['user_id'] == _user_id:
#Deleting (popping) relevant object from orders.json
                User.user_data['users'].pop(User.user_data['users'].index(i))
                print('')
                print(f"Your account with ID '{_user_id}' was deleted.")
                with open('users.json', 'w', encoding='utf-8') as f:
                    json.dump(User.user_data, f, indent=4, separators=(',', ': '))
                print('')
                print('You exited.')
                sys.exit()
            else:
                pass

    def write_password_deposit(self, user_password_query):
        """Defining writing of user password deposit to a file"""
        with open("encrypted_password.csv", "w", encoding='utf-8') as file:
            file.write(user_password_query)

    def write_user_key(self):
        """Defining generating of a user key & writing it to a file"""
        key = Fernet.generate_key()
        with open ("key.user_key", "wb") as key_file:
            key_file.write(key)

    def load_user_key(self):
        """Defining loading of key"""
        return open("key.user_key", "rb").read()

    def encrypt(self, filename, key):
        """Defining of encrypting user password & writing it to a file"""
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_password = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_password)
        return encrypted_password

    def decrypt(self, filename, key):
        """Defining of decrypting user password, re-encrypting it & writing it to a file"""
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_password = file.read()
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password
