import json

class User():
    with open('users.json') as f:    
        user_data = json.load(f)
    
    def __init__(self):
        pass

    def create_user(self, userPassword_query, userUsername_query, userID_query, userName_query, userEmailAddress_query, userHouseNumber_query, userStreet_query, userTown_query, userCountry_query, userPostcode_query, userBankName_query, userBankAccountName_query, userBankAccountBSB_query, userBankAccountNumber_query, userCardName_query, userCardNumber_query, userCardExpiry_query, userCardCVC_query):
        user = {
            "userPassword": userPassword_query,
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
        with open('users.json', 'w') as f:
            json.dump(User.user_data, f, indent=4, separators=(',', ': '))
            print("User created.")

    def view_user(self):
        for i in User.user_data['users']:
            print(f"Password:{i['userPassword']} | Username:{i['userUsername']} | ID:{i['userID']} | Name:{i['userName']} | Email Address:{i['userEmailAddress']} | House Number:{i['userHouseNumber']} | Street:{i['userstreet']} | Town:{i['userTown']} | Country:{i['userCountry']} | Postcode:{i['userPostcode']} | Bank Name:{i['userBankName']} | Bank Account Name:{i['userBankAccountName']} | Bank Account BSB:{i['userBankAccountBSB']} | Bank Account Number:{i['userBankAccountNumber']} | Card Name:{i['userCardName']} | Card Number:{i['userCardNumber']} | Card Expiry{i['userCardExpiry']} | Card CVC:{i['userCardCVC']}")

    def search_userUsername(self, userUsername_query):
        _username = userUsername_query
        finder = False
        for i in User.user_data['users']:
            if i['userUsername'] == _username:
                print(f"Password:{i['userPassword']} | Username:{i['userUsername']} | ID:{i['userID']} | Name:{i['userName']} | Email Address:{i['userEmailAddress']} | House Number:{i['userHouseNumber']} | Street:{i['userstreet']} | Town:{i['userTown']} | Country:{i['userCountry']} | Postcode:{i['userPostcode']} | Bank Name:{i['userBankName']} | Bank Account Name:{i['userBankAccountName']} | Bank Account BSB:{i['userBankAccountBSB']} | Bank Account Number:{i['userBankAccountNumber']} | Card Name:{i['userCardName']} | Card Number:{i['userCardNumber']} | Card Expiry{i['userCardExpiry']} | Card CVC:{i['userCardCVC']}")
                finder = True
                break
        if finder == False:
            print(f"{_username} cannot be found.")

    def search_userID(self, userID_query):
        _ID = userID_query
        finder = False
        for i in User.user_data['users']:
            if i['userID'] == _ID:
                print(f"Password:{i['userPassword']} | Username:{i['userUsername']} | ID:{i['userID']} | Name:{i['userName']} | Email Address:{i['userEmailAddress']} | House Number:{i['userHouseNumber']} | Street:{i['userstreet']} | Town:{i['userTown']} | Country:{i['userCountry']} | Postcode:{i['userPostcode']} | Bank Name:{i['userBankName']} | Bank Account Name:{i['userBankAccountName']} | Bank Account BSB:{i['userBankAccountBSB']} | Bank Account Number:{i['userBankAccountNumber']} | Card Name:{i['userCardName']} | Card Number:{i['userCardNumber']} | Card Expiry{i['userCardExpiry']} | Card CVC:{i['userCardCVC']}")
                finder = True
                break
        if finder == False:
            print(f"{_ID} cannot be found.")

    def edit_user(self, userID_query, userEdit_choice, new_userPassword, new_userUsername, new_userName, new_userEmailAddress, new_userHouseNumber, new_userStreet, new_userTown, new_userCountry, new_userPostcode, new_userBankName, new_userBankAccountName, new_userBankAccountBSB, new_userBankAccountNumber, new_userCardName, new_userCardNumber, new_userCardExpiry, new_userCardCVC):
        for i in User.user_data['users']:
            if i['userID'] == userID_query:
                if userEdit_choice == 1:
                    i['userPassword'] == new_userPassword
                elif userEdit_choice == 2:
                    i['userUsername'] == new_userUsername
                elif userEdit_choice == 3:
                    i['userName'] == new_userName
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
            json.dump(User.user_data, f, indent=4, separators=(',', ': '))
            print(f"Update made.")

    def delete_user(self, userID_query):
        _ID = userID_query
        finder = False
        for i in User.user_data['users']:
            if i['userID'] == _ID:
                User.user_data['users'].pop(User.user_data['users'].index(i))
                finder = True
                print(f"{_ID} deleted.")
                break
        with open('users.json', 'w') as f:
            json.dump(User.user_data, f, indent=4, separators=(',', ': '))
        if finder == False:
            print(f"{_ID} could not be found.")

    def authorise_user(self, authorise, userPassword_query, userUsername_query):
        authorise = authorise
        _Password = userPassword_query
        _Username = userUsername_query
        for i in User.user_data['users']:
            if i['userPassword'] == _Password and i['userUsername'] == _Username:
                authorise = True
            else:
                authorise = False
