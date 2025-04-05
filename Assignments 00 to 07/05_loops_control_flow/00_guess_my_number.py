 # PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 05_loops_control_flow

# 00_guess_my_number.py

# PROBLEM STATEMENT

# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

# SOLUTION

import random

def guess():
    print(f"\n 🎉 Welcome to the Number Guessing Game! 🌟")
    print("\n 🤔 I am thinking of a number between 1 and 99... Can you guess it? 🧐")

    # Generate a secret number for the game
    secret_number = random.randint(1, 99)
    
    # Prompt the user for their first guess
    guess = int(input(f"\n 🎯 Enter your guess: "))
    while guess != secret_number:
        if guess < secret_number:
            print("\n 📉 Oops! Your guess is too low. Try again! ⬆️")
        else:
            print("\n 📈 Oops! Your guess is too high. Try again! ⬇️")
        
        print()  # Adds an empty line for better readability
        guess = int(input(f"\n 🔄 Enter a new guess: "))
    
    # Congratulatory message when the user guesses correctly
    print(f"\n 🎊 Congrats! 🎉 You guessed it right! The secret number was: {secret_number} 🎯")

if __name__ == "__main__":
    guess()

# ----------------------------- END OF CODE -----------------------------


