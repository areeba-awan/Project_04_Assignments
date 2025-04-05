# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 01_expressions

# 01_dicesimulator.py

# PROBLEM STATEMENT :

# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how 
# variable scope works.

# SOLUTION :
 
"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

from random import randint

def roll_dice():
    """🎲 Function to roll two dice and show the result 🎲"""
    dice1 = randint(1, 6)  # Generate a random number for dice 1 🎲
    dice2 = randint(1, 6)  # Generate a random number for dice 2 🎲
    result = dice1 + dice2  # Calculate the total of both dice 🌟
    print(f"🎯 Die 1: {dice1} 🎲, Die 2: {dice2} 🎲 → Total: {result} 🎉")

def main():
    """✨ Main function to roll dice three times ✨"""
    print("\n 🎲 Welcome to the Areeba's Dice Rolling Game! 🎉\n")
    for i in range(3):
        print(f"🔹 Roll {i+1}:")
        roll_dice()
        print("—" * 20)  # Separator for better readability ✨

    print("🎊 Thanks for playing! 🎊")

if __name__ == "__main__":
    main()

# ----------------------------- END OF THE PROGRAM -----------------------------

