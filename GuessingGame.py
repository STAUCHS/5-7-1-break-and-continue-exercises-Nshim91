#-------------------------------------------------------------------------
# Name:
# Purpose:
# Author:     Last Name. First Initial
# Created:    dd/mm/yyyy
#-------------------------------------------------------------------------

# GuessingGame.py

import random

print("*** Guess the Number ***")
print("Welcome to the guess the number game.")
print("You have 5 chances to guess the number between 1 and 100.")

# Generate random number
number = random.randint(1, 100)

# Initialize guess count
guess_count = 0

# Limit the number of tries to 5
while guess_count < 5:
    guess = int(input("Enter a number between 1 and 100: "))
    guess_count += 1
    
    if guess < number:
        print("Too low, guess again")
    elif guess > number:
        print("Too high, guess again")
    else:
        print("Congratulations! You've guessed correctly.")
        break
else:
    print(f"Sorry, you've guessed incorrectly, the number is {number}.")
