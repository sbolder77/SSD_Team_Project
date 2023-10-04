import json
import onlineretailer

#userPassword_query = input("")
#userUsername_query = int(input(""))
#userID_query = int(input(""))
#userFirstname_query = input("")
#userLastname_query = input("")
#userEmailAddress_query = input("")
#userHouseNumber_query = int(input(""))
#userStreet_query = input("")
#userTown_query = input("")
#userCountry_query = input("")
#userPostcode_query = int(input(""))
#userBankName_query = input("")
#userBankAccountName_query = input("")
#userBankAccountBSB_query = int(input(""))
#userBankAccountNumber_query = int(input(""))
#userCardName_query = input("")
#userCardNumber_query = int(input(""))
#userCardExpiry_query = int(input(""))
#userCardCVC_query = int(input(""))

#new_userPassword = input("")
#new_userUsername = int(input(""))
#new_userID = int(input(""))
#new_userFirstname = input("")
#new_userLastname = input("")
#new_userEmailAddress = input("")
#new_userHouseNumber = int(input(""))
#new_userStreet = input("")
#new_userTown = input("")
#new_userCountry = input("")
#new_userPostcode =int(input(""))
#new_userBankName = input("")
#new_userBankAccountName = input("")
#new_userBankAccountBSB = int(input(""))
#new_userBankAccountNumber = int(input(""))
#new_userCardName = input("")
#new_userCardNumber = int(input(""))
#new_userCardExpiry = int(input(""))
#new_userCardCVC = int(input(""))

users_data_file = 'users.json'
f = open(users_data_file)
user_data = json.load(f)

class Users():
    def __init__(self):
        pass

    def create_user(self, userPassword_query, userUsername_query, userID_query, userFirstName_query, userLastName_query, userEmailAddress_query, userHouseNumber_query, userStreet_query, userTown_query, userCountry_query, userPostcode_query, userBankName_query, userBankAccountName_query, userBankAccountBSB_query, userBankAccountNumber_query, userCardName_query, userCardNumber_query, userCardExpiry_query, userCardCVC_query):
        user = {
            "userPassword": userPassword_query,
            "userUsername": userUsername_query,
            "userID": userID_query,
            "userFirstName": userFirstname_query,
            "userLastName": userLastname_query,
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
        user_data['users'].append(user)
        with open('users.json', 'w') as f:
            json.dump(user_data, f, indent=4, separators=(',', ': '))
            print("User created.")

    def view_user(self):
        for i in user_data['users']:
            print(f"Password:{i['userPassword']} | Username:{i['userUsername']} | ID:{i['userID']} | First Name:{i['userFirstName']} | Last Name:{i['userLastName']} | Email Address:{i['userEmailAddress']} | House Number:{i['userHouseNumber']} | Street:{i['userstreet']} | Town:{i['userTown']} | Country:{i['userCountry']} | Postcode:{i['userPostcode']} | Bank Name:{i['userBankName']} | Bank Account Name:{i['userBankAccountName']} | Bank Account BSB:{i['userBankAccountBSB']} | Bank Account Number:{i['userBankAccountNumber']} | Card Name:{i['userCardName']} | Card Number:{i['userCardNumber']} | Card Expiry{i['userCardExpiry']} | Card CVC:{i['userCardCVC']}")

    def search_userUsername(self):
        _username = userUsername_query
        finder = False
        for i in user_data['users']:
            if i['userUsername'] == _username:
                print(f"Password:{i['userPassword']} | Username:{i['userUsername']} | ID:{i['userID']} | First Name:{i['userFirstName']} | Last Name:{i['userLastName']} | Email Address:{i['userEmailAddress']} | House Number:{i['userHouseNumber']} | Street:{i['userstreet']} | Town:{i['userTown']} | Country:{i['userCountry']} | Postcode:{i['userPostcode']} | Bank Name:{i['userBankName']} | Bank Account Name:{i['userBankAccountName']} | Bank Account BSB:{i['userBankAccountBSB']} | Bank Account Number:{i['userBankAccountNumber']} | Card Name:{i['userCardName']} | Card Number:{i['userCardNumber']} | Card Expiry{i['userCardExpiry']} | Card CVC:{i['userCardCVC']}")
                finder = True
                break
        if finder == False:
            print(f"{_username} cannot be found.")

    def search_userID(self):
        _ID = userID_query
        finder = False
        for i in user_data['users']:
            if i['userID'] == _ID:
                print(f"Password:{i['userPassword']} | Username:{i['userUsername']} | ID:{i['userID']} | First Name:{i['userFirstName']} | Last Name:{i['userLastName']} | Email Address:{i['userEmailAddress']} | House Number:{i['userHouseNumber']} | Street:{i['userstreet']} | Town:{i['userTown']} | Country:{i['userCountry']} | Postcode:{i['userPostcode']} | Bank Name:{i['userBankName']} | Bank Account Name:{i['userBankAccountName']} | Bank Account BSB:{i['userBankAccountBSB']} | Bank Account Number:{i['userBankAccountNumber']} | Card Name:{i['userCardName']} | Card Number:{i['userCardNumber']} | Card Expiry{i['userCardExpiry']} | Card CVC:{i['userCardCVC']}")
                finder = True
                break
        if finder == False:
            print(f"{_ID} cannot be found.")

    def edit_user(self, userPassword_query, userUsername_query, userID_query, userFirstName_query, userLastName_query, userEmailAddress_query, userHouseNumber_query, userStreet_query, userTown_query, userCountry_query, userPostcode_query, userBankName_query, userBankAccountName_query, userBankAccountBSB_query, userBankAccountNumber_query, userCardName_query, userCardNumber_query, userCardExpiry_query, userCardCVC_query):
        for i in user_data['users']:
            if i['userID'] == userID_query:
                if userEdit_choice == 1:
                    i['userPassword'] == new_userPassword
                elif userEdit_choice == 2:
                    i['userUsername'] == new_userUsername
                elif userEdit_choice == 3:
                    i['userFirstName'] == new_userFirstName
                    i['userLastName'] == new_userLastName
                elif userEdit_choice == 4:
                    i['userEmailAddress'] == new_userEmailAddress
                elif userEdit_choice == 5:
                    i['userHouseNumber'] == new_userHouseNumber
                    i['userStreet'] == new_userStreet
                    i['userTown'] == new_userTown
                    i['userCountry'] == new_userCountry
                    i['userPostcode'] == new_userPostcode
                    i['userHouseNumber'] == new_userHouseNumber
                elif userEdit_choice == 6:
                    i['userBankName'] = new_userBankName
                    i['userBankAccountName'] = new_userBankAccountName
                    i['userBankAccountBSB'] = new_userBankAccountBSB
                    i['userBankAccountNumber'] = new_userBankAccountNumber
                elif userEdit_choice == 7:
                    i['userCardName'] = new_userCardName
                    i['userCardNumber'] = new_userCardNumber
                    i['userCardExpiry'] = new_userCardExpiry
                    i['userCardCVC'] = new_userCardCVC
                else:
                    pass
            else:
                pass
        with open('users.json', 'w') as f:
            json.dump(user_data, f, indent=4, separators=(',', ': '))
            print(f"Update made.")

    def delete_user(self):
        _ID = userID_query
        finder = False
        for i in user_data['users']:
            if i['userID'] == _ID:
                user_data['users'].pop(user_data['users'].index(i))
                finder = True
                print(f"{_ID} deleted.")
                break
        with open('users.json', 'w') as f:
            json.dump(user_data, f, indent=4, separators=(',', ': '))
        if finder == False:
            print(f"{_ID} could not be found.")

    def authorise_user(self, userPassword_query, userUsername_query):
        _Password = userPassword_query
        _Username = userUsername_query
        authorise = False
        valid_user = False
        finder = False
        for i in user_data['users']:
            if i['userPassword'] == _Password and i['userUsername'] == _Username:
                authorise = True
                if authorise == True:
                    valid_user = True
                    user_menu()
                else:
                    pass
            else:
                authorise = False
                if authorise = False:
                    valid_user = False
                else:
                    pass
