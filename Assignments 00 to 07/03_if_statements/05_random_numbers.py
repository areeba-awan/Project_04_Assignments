# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 03_if_statements

# # 05_random_numbers.py

# PROBLEM STATEMENT :

# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by
#  the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could 
# include 1 and could include 6:

# value = random.randint(1, 6)

# SOLUTION :

import random

# Constants for generating random numbers
N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """Generate and print 10 random numbers between 1 and 100 with a fun and engaging twist!"""
    print(f"\n 🎲 Welcome to the Random Number Generator! 🌟")
    print("\n ✨ I will generate 10 random numbers for you between 1 and 100. 🚀")
    print("\n 🔢  Here are your random numbers:")

    for _ in range(N_NUMBERS):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(f"\n 🎯 {number}")

    print("\n 🎉 Thank you for using the Random Number Generator! Have a great day! 😊")

if __name__ == '__main__':
    main()

# --------------------------- END OF CODE ---------------------------
