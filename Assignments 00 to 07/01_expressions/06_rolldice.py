# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 01_expressions

# 06_rolldice.py

# PROBLEM STATEMENT :

# Simulate rolling two dice, and prints results of each roll as well as the total.

# SOLUTION :

"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

from random import randint
import time

def roll_dice():
    """🎲 Function to Roll Two Dice and Display the Results 🎉"""
    print("\n 🎯 Rolling the dice... 🎲✨")

    time.sleep(1)  # Adding a delay for suspense ⏳
    dice1 = randint(1, 6)  # Generate a random number for dice 1
    dice2 = randint(1, 6)  # Generate a random number for dice 2
    result = dice1 + dice2  # Calculate the total of the dice

    # Display the results
    print(f"\n 🎲 Dice 1: {dice1} 🌟, Dice 2: {dice2} 🌟 => 🏆 Total: {result} 🎉")

def main():
    """✨ Main Function to Roll Dice Multiple Times ✨"""
    print("\n 🎲 Welcome to the Dice Rolling Game! 🎉\n")
    for i in range(3):
        print(f"🔹 Roll {i + 1}: 🎲")
        roll_dice()
        print("➖" * 20)  # Separator line for readability

    print("\n🎊 Thanks for playing! Hope you enjoyed the rolls! 🎯")

if __name__ == "__main__":
    main()


# ----------------------------- END OF THE PROGRAM -----------------------------

