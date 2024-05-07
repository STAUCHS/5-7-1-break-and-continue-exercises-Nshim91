#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

# UsernamePassword.py

# Define correct username and password
correct_username = "StAugustineCHS"
correct_password = "Coding123!"

# Prompt user for username and password
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if username and password are correct
    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    elif username != correct_username and password != correct_password:
        print("Username and password incorrect.")
    elif username != correct_username:
        print("Username incorrect.")
    else:
        print("Password incorrect.")
