#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

# BankPIN.py

# Store the correct PIN
correct_pin = "1938"

print("WELCOME TO STA BANK!")

# Validate PIN
while True:
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("PIN accepted. You may now access your account.")
        break
    else:
        print("Incorrect PIN. Try again.")
