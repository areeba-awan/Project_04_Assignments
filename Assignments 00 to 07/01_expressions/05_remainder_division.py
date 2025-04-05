# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 01_expressions

# 05_remainder_division.py

# PROBLEM STATEMENT :

# Problem Statement
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the
#  second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2


# SOLUTION :

def main():
    """🔢 Division Program with Remainder 🎉"""

    # Prompt the user to enter the numbers 🧮
    num1 = int(input("\n ✨ Please enter an integer to be divided: ➡️  "))
    num2 = int(input("\n 🌟 Please enter an integer to divide by: ➡️  "))

    # Calculate the result of the division 🔄
    result = num1 // num2

    # Calculate the remainder of the division ✨
    remainder = num1 % num2

    # Print the result and remainder 🎉
    print("\n📏 Division Results 🏆")
    print(f"\n🔹 Result: {result}")
    print(f"\n🔹 Remainder: {remainder} 🌟")

if __name__ == "__main__":
    main()

# ----------------------------- END OF THE PROGRAM -----------------------------
