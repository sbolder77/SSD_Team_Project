import json
from cryptography.fernet import Fernet

users_data_file = 'users.json'
j = open(users_data_file)
data = json.load(j)
jsonData = data["Users"]

class User:
    def check_user(user):
        with open (jsonData, "r") as f:
            temp = json.load(f)
            for x in temp:
                if user == x['ID']:
                    return True
                else:
                    return "user does not exist"

    def create_user():
        user_data = []
        with open (jsonData, "r") as f:
            temp = json.load(f)
        user_data["password"] = input("Password: ")
        user_data["username"] = input("Username: ")
        user_data["user_id"] = input("User ID: ")
        user_data["firstName"] = input("First Name: ")
        user_data["surname"] = input("Surname: ")
        user_data["email_address"] = input("Email Address: ")
        user_data["house_number"] = input("House Number: ")    
        user_data["street"] = input("Street: ")    
        user_data["town"] = input("Town: ")
        user_data["country"] = input("Country: ")
        user_data["Postcode"] = input("Postcode: ")
        temp.append(user_data)
        with open (jsonData, "w") as f:
            json.dump(temp, f, indent=4)

    def view_user():
        with open (jsonData, "r") as f:
            temp = json.load(f)
            for entry in temp:
                password = entry["password"]
                username = entry["username"]
                user_id = entry["user_id"]
                firstname = entry["firstname"]
                surname = entry["surname"]
                email_address = entry["email_address"]
                house_number = entry["house_number"]
                street = entry["street"]
                town = entry["town"]
                postcode = entry["postcode"]
                print (f"Index Number {i}")
                print(f"Password: {password}")
                print(f"Username: {username}")
                print(f"User ID: {user_id}")
                print(f"First Name: {firstname}")
                print(f"Surname: {surname}")
                print(f"Email Address: {email_address}")
                print(f"House Number: {house_number}")
                print(f"Street: {street}")
                print(f"Town: {town}")
                print(f"Postcode: {postcode}")
                print("\n\n")
    
    def edit_user():
        pass

    def delete_user():
        User.view_user()
        new_user = []
        with open (jsonData, "r") as f:
            temp = json.load(f)
        delete_query = input("Do you wish to delete your user account (input 'Yes' or 'No'?")
        for entry in temp:
            if delete_query == No:
                pass
            else:
                new_user.append(entry)

    def authorise_user():
        pass
