from cryptography.fernet import Fernet
import sys
import json
import filelogging

#region objects
#l = filelogging.LoggingDetails()
#endregion

class User():
    with open('users.json', encoding='utf-8') as f:    
        user_data = json.load(f)
    
    def __init__(self):
        pass

    def create_user(self, userUsername_query, userID_query, userName_query, userEmailAddress_query, userHouseNumber_query, userStreet_query, userTown_query, userCountry_query, userPostcode_query, userBankName_query, userBankAccountName_query, userBankAccountBSB_query, userBankAccountNumber_query, userCardName_query, userCardNumber_query, userCardExpiry_query, userCardCVC_query):
        user = {
            "userUsername": userUsername_query,
            "userID": userID_query,
            "userName": userName_query,
            "userEmailAddress": userEmailAddress_query,
            "userHouseNumber": userHouseNumber_query,
            "userStreet": userStreet_query,
            "userTown": userTown_query,
            "userCountry": userCountry_query,
            "userPostcode": userPostcode_query,
            "userBankName": userBankName_query,
            "userBankAccountName": userBankAccountName_query,
            "userBankAccountBSB": userBankAccountBSB_query,
            "userBankAccountNumber": userBankAccountNumber_query,
            "userCardName": userCardName_query,
            "userCardNumber": userCardNumber_query,
            "userCardExpiry": userCardExpiry_query,
            "userCardCVC": userCardCVC_query
        }
        User.user_data['users'].append(user)
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(User.user_data, f, indent=4, separators=(',', ': '))
            print('')
            print('User created.')
            print('----------------------------------------------------------')
        #l.write_system_log('USER', 'INFO', userID_query + ' - created', userName_query)

    def view_user(self):
        for i in User.user_data['users']:
            print(f"Username:{i['userUsername']} \nID:{i['userID']} \nName:{i['userName']} \nEmail Address:{i['userEmailAddress']} \nHouse Number:{i['userHouseNumber']} \nStreet:{i['userStreet']} \nTown:{i['userTown']} \nCountry:{i['userCountry']} \nPostcode:{i['userPostcode']} \nBank Name:{i['userBankName']} \nBank Account Name:{i['userBankAccountName']} \nBank Account BSB:{i['userBankAccountBSB']} \nBank Account Number:{i['userBankAccountNumber']} \nCard Name:{i['userCardName']} \nCard Number:{i['userCardNumber']} \nCard Expiry{i['userCardExpiry']} \nCard CVC:{i['userCardCVC']}")

    def search_userUsername(self, userUsername_query):
        _username = userUsername_query
        finder = False
        for i in User.user_data['users']:
            if i['userUsername'] == _username:
                print(f"Username:{i['userUsername']} | ID:{i['userID']} | Name:{i['userName']} | Email Address:{i['userEmailAddress']} | House Number:{i['userHouseNumber']} | Street:{i['userstreet']} | Town:{i['userTown']} | Country:{i['userCountry']} | Postcode:{i['userPostcode']} | Bank Name:{i['userBankName']} | Bank Account Name:{i['userBankAccountName']} | Bank Account BSB:{i['userBankAccountBSB']} | Bank Account Number:{i['userBankAccountNumber']} | Card Name:{i['userCardName']} | Card Number:{i['userCardNumber']} | Card Expiry{i['userCardExpiry']} | Card CVC:{i['userCardCVC']}")
                finder = True
                break
        if finder == False:
            print(f"{_username} cannot be found.")

    def search_userID(self, userID_query):
        _ID = userID_query
        finder = False
        for i in User.user_data['users']:
            if i['userID'] == _ID:
                print(f"Username:{i['userUsername']} | ID:{i['userID']} | Name:{i['userName']} | Email Address:{i['userEmailAddress']} | House Number:{i['userHouseNumber']} | Street:{i['userstreet']} | Town:{i['userTown']} | Country:{i['userCountry']} | Postcode:{i['userPostcode']} | Bank Name:{i['userBankName']} | Bank Account Name:{i['userBankAccountName']} | Bank Account BSB:{i['userBankAccountBSB']} | Bank Account Number:{i['userBankAccountNumber']} | Card Name:{i['userCardName']} | Card Number:{i['userCardNumber']} | Card Expiry{i['userCardExpiry']} | Card CVC:{i['userCardCVC']}")
                finder = True
                break
        if finder == False:
            print(f'{_ID} cannot be found.')

    def edit_user(self, userID_query, userEdit_choice, new_userPassword, new_userUsername, new_userName, new_userEmailAddress, new_userHouseNumber, new_userStreet, new_userTown, new_userCountry, new_userPostcode, new_userBankName, new_userBankAccountName, new_userBankAccountBSB, new_userBankAccountNumber, new_userCardName, new_userCardNumber, new_userCardExpiry, new_userCardCVC):
        if userEdit_choice == str(1):
            User.write_passwordDeposit(self, new_userPassword)
            User.write_userKey(self)
            key = User.load_userKey(self)
            User.encrypt(self, 'encryptedPassword.csv', key)
        for i in User.user_data['users']:
            if userEdit_choice == str(2):
                if i['userID'] == userID_query:
                    i['userUsername'] = new_userUsername
            elif userEdit_choice == str(3):
                if i['userID'] == userID_query:
                    i['userName'] = new_userName
            elif userEdit_choice == str(4):
                if i['userID'] == userID_query:
                    i['userEmailAddress'] = new_userEmailAddress
            elif userEdit_choice == str(5):
                if i['userID'] == userID_query:
                    i['userHouseNumber'] = new_userHouseNumber
                    i['userStreet'] = new_userStreet
                    i['userTown'] = new_userTown
                    i['userCountry'] = new_userCountry
                    i['userPostcode'] = new_userPostcode
                    i['userHouseNumber'] = new_userHouseNumber
            elif userEdit_choice == str(6):
                if i['userID'] == userID_query:
                    i['userBankName'] = new_userBankName
                    i['userBankAccountName'] = new_userBankAccountName
                    i['userBankAccountBSB'] = new_userBankAccountBSB
                    i['userBankAccountNumber'] = new_userBankAccountNumber
            else:
                if i['userID'] == userID_query:
                    i['userCardName'] = new_userCardName
                    i['userCardNumber'] = new_userCardNumber
                    i['userCardExpiry'] = new_userCardExpiry
                    i['userCardCVC'] = new_userCardCVC
        with open('users.json', 'w', encoding='utf-8') as f:
            json.dump(User.user_data, f, indent=4, separators=(',', ': '))
            print('')
            print('Update made.')

    def delete_user(self, userID_query):
        _userID = userID_query
        for i in User.user_data['users']:
            if i['userID'] == _userID:
                User.user_data['users'].pop(User.user_data['users'].index(i))
                print('')
                print(f"Your account with ID '{_userID}' was deleted.")
                with open('users.json', 'w', encoding='utf-8') as f:
                    json.dump(User.user_data, f, indent=4, separators=(',', ': '))
                print('')
                print('You exited.')
                sys.exit()
            else:
                pass

    def write_passwordDeposit(self, userPassword_query):
        with open("encryptedPassword.csv", "w", encoding='utf-8') as file:
            file.write(userPassword_query)

    def write_userKey(self):
        key = Fernet.generate_key()
        with open ("key.userKey", "wb") as key_file:
            key_file.write(key)

    def load_userKey(self):
        return open("key.userKey", "rb").read()

    def encrypt(self, filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_password = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_password)
        return encrypted_password

    def decrypt(self, filename, key):
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_password = file.read()
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password
