"""Importing necessary modules"""
import json
from cryptography.fernet import Fernet

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
            "userUsername": user_username_query,
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
            print(f"Username:{i['userUsername']} \nID:{i['userID']} \nName:{i['userName']}")
            print(f"Email Address:{i['userEmailAddress']}")
            print(f"House Number:{i['userHouseNumber']}")
            print(f"Street:{i['userStreet']} \nTown:{i['userTown']}")
            print(f"Country:{i['userCountry']}")
            print(f"Postcode:{i['userPostcode']}") 
            print(f"\nBank Name:{i['userBankName']}")
            print(f"Bank Account Name:{i['userBankAccountName']}")
            print(f"Bank Account BSB:{i['userBankAccountBSB']}")
            print(f"Bank Account Number:{i['userBankAccountNumber']}")
            print(f"\nCard Name:{i['userCardName']} \nCard Number:{i['userCardNumber']}")
            print(f"Card Expiry{i['userCardExpiry']} \nCard CVC:{i['userCardCVC']}")

    def search_user_username(self, user_username_query):
        """#Defining user search by username function & printing out relevant object in users.json 
        or reporting it unfound"""
        _username = user_username_query
        finder = False
        for i in User.user_data['users']:
            if i['userUsername'] == _username:
                print(f"Username:{i['userUsername']} \nID:{i['userID']} \nName:{i['userName']}")
                print(f"Email Address:{i['userEmailAddress']}")
                print(f"House Number:{i['userHouseNumber']} \nStreet:{i['userStreet']}")
                print(f"Town:{i['userTown']} \nCountry:{i['userCountry']}")
                print(f"Postcode:{i['userPostcode']}")
                print(f"\nBank Name:{i['userBankName']}")
                print(f"Bank Account Name:{i['userBankAccountName']}")
                print(f"Bank Account BSB:{i['userBankAccountBSB']}")
                print(f"Bank Account Number:{i['userBankAccountNumber']}")
                print(f"\nCard Name:{i['userCardName']} \nCard Number:{i['userCardNumber']}")
                print(f"Card Expiry{i['userCardExpiry']} \nCard CVC:{i['userCardCVC']}")
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
            if i['userID'] == _ID:
                print(f"Username:{i['userUsername']} \nID:{i['userID']} \nName:{i['userName']}")
                print(f"Email Address:{i['userEmailAddress']}")
                print(f"House Number:{i['userHouseNumber']} \nStreet:{i['userStreet']}")
                print(f"Town:{i['userTown']} \nCountry:{i['userCountry']}")
                print(f"Postcode:{i['userPostcode']}")
                print(f"\nBank Name:{i['userBankName']}")
                print(f"Bank Account Name:{i['userBankAccountName']}")
                print(f"Bank Account BSB:{i['userBankAccountBSB']}")
                print(f"Bank Account Number:{i['userBankAccountNumber']}")
                print(f"\nCard Name:{i['userCardName']} \nCard Number:{i['userCardNumber']}")
                print(f"Card Expiry{i['userCardExpiry']} \nCard CVC:{i['userCardCVC']}")
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
                if i['userID'] == user_id_query:
                    i['userUsername'] = new_user_username
            elif user_edit_choice == str(3):
                if i['userID'] == user_id_query:
                    i['userName'] = new_user_name
            elif user_edit_choice == str(4):
                if i['userID'] == user_id_query:
                    i['userEmailAddress'] = new_user_email_address
            elif user_edit_choice == str(5):
                if i['userID'] == user_id_query:
                    i['userHouseNumber'] = new_user_house_number
                    i['userStreet'] = new_user_street
                    i['userTown'] = new_user_town
                    i['userCountry'] = new_user_country
                    i['userPostcode'] = new_user_postcode
                    i['userHouseNumber'] = new_user_house_number
            elif user_edit_choice == str(6):
                if i['userID'] == user_id_query:
                    i['userBankName'] = new_user_bank_name
                    i['userBankAccountName'] = new_user_bank_account_name
                    i['userBankAccountBSB'] = new_user_bank_account_bsb
                    i['userBankAccountNumber'] = new_user_bank_account_number
            else:
                if i['userID'] == user_id_query:
                    i['userCardName'] = new_user_card_name
                    i['userCardNumber'] = new_user_card_number
                    i['userCardExpiry'] = new_user_card_expiry
                    i['userCardCVC'] = new_user_card_cvc
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(User.user_data, f, indent=4, separators=(',', ': '))
            print('')
            print('Update made.')

    def delete_user(self, user_id_query):
        """#Defining item deletion by item ID function or reporting it unfound"""
        _user_id = user_id_query
        for i in User.user_data['users']:
            if i['userID'] == _user_id:
#Deleting (popping) relevant object from orders.json
                User.user_data['users'].pop(User.user_data['users'].index(i))
                with open('users.json', 'w', encoding='utf-8') as f:
                    json.dump(User.user_data, f, indent=4, separators=(',', ': '))
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
