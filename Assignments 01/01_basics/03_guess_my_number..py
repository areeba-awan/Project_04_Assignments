# PROJECT 4 ASSIGNMENTS 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 01

# 01_basics

# 03_guess_my_number.py

# PROBLEM STATEMENT

# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


# SOLUTION

import random

def main():
    print(f"\n 🎉 Welcome to the Number Guessing Game! 🌟")
    print("\n 🤔 I'm thinking of a number between 1 and 99. Can you guess it? 🧐\n")

    # Generate the secret number
    secret_number = random.randint(1, 99)
    
    while True:
        # Get the player's guess
        guess = int(input(f"\n 🎯 Enter your guess: "))

        # Check the guess
        if guess == secret_number:
            print(f"\n 🎊 Congrats! You guessed it right! The number was: {secret_number} 🎯")
            break
        elif abs(secret_number - guess) <= 5:
            print(f"\n 🌟 Very close! Keep going!")
        elif guess < secret_number:
            print("\n ⬆️  Your guess is too low. Try again!")
        else:
            print("\n ⬇️  Your guess is too high. Try again!")

    print(f"\n🎉 Thanks for playing the Number Guessing Game! See you next time! 🚀")

if __name__ == '__main__':
    main()

# --------------------- END OF CODE ---------------------
