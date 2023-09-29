import json
from cryptography.fernet import Fernet

users_data_file = 'users.json'
j = open(users_data_file)
data_users = json.load(j)
jsonData_users = data["Users"]

class User:
    def check_user():
        pass

    def create_user():
        user_data = []
        with open (jsonData_users, "w") as f:
            temp = json.load(f)
        user_data["password"] = input("Password: ")
        
        user_data["username"] = input("Username: ")
        if username not in jsonData_users:
            pass
        else:
            print("This username is not available.")
            choice_query = input("Please input another username: ")
            if choice_query == 1:
                    continue
                else:
                    break    
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
        with open (jsonData_users, "w") as f:
            json.dump(temp, f, indent=4)

    def view_user():
        with open (jsonData_users, "r") as f:
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
        view_user()
        with open (jsonData_users, "w") as f:
            temp = json.load(f)
            choice_query = input("Input which of your user details you wish to edit (if you wish to exit, input 'exit'): ")
            if choice_query == str("Password")
                user_data["password"] = input("Password: ")
                print("Password changed.")
                continue
                
            elif choice_query == str("Username"):
                user_data["username"] = input("Username: ")
                print("Username changed.")
                continue

            elif choice_query == str("User ID"]
                print("User ID is unchangeable.")
                continue
                
            elif choice_query == str("First Name"):
                user_data["firstname"] = input("First Name: ")
                print("First Name changed.")
                continue

            elif choice_query == str("Surname"):
                user_data["surname"] = input("Surname: ")
                print("Surname changed.")
                continue

           elif choice_query == str("Email Address"):
                user_data["email_address"] = input("Email Address: ")
                print("Email Address changed.")
                continue

           elif choice_query == str("House Number"]
                user_data["house_number"] = input("House Number")
                print("House Number changed.")
                continue

           elif choice_query == str("Street"]
                user_data["street"] = input("Street")
                print("Street changed.")
                continue

           elif choice_query == str("Town"]
                user_data["town"] = input("Town")
                print("Town changed.")
                continue

           elif choice_query == str("Postcode"]
                user_data["psotcode"] = input("Postcode")
                print("Postcode changed.")
                continue

            else:
                break
                
    def delete_user():
        User.view_user()
        new_user = []
        with open (jsonData_users, "w") as f:
            temp = json.load(f)
        delete_query = input("Do you wish to delete your user account (input 'Yes' or 'No'?")
        for entry in temp:
            if delete_query == No:
                pass
            else:
                new_user.append(entry)

    def authorise_user():
        pass
