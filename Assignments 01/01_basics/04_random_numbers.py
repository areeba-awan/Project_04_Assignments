# PROJECT 4 ASSIGNMENTS 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 01

# 01_basics

# 04_random_numbers.py

# PROBLEM STATEMENT

# Print 10 random numbers in the range 1 to 100.

# Here is an example run:

# 45 79 61 47 52 10 16 83 19 12

# Each time you run your program you should get different numbers

# 81 76 70 1 27 63 96 100 32 92

# Recall that the python random library has a function randint which returns an integer in the range set by 
# the parameters (inclusive). For example this call would produce a random integer between 1 and 6, which could 
# include 1 and could include 6:

# value = random.randint(1, 6)

# SOLUTION :

import random

# Constants for random number generation
N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    ✨ Generates and prints 10 random numbers using a loop. ✨
    """
    print(f"\n🎉 Welcome to the Random Number Generator! 🌟")
    print(f"\n 🔢 I'll generate 10 random numbers between 1 and 100 for you. Ready? 🚀\n")

    print(f"\n 📋 Here are your random numbers:")
    for _ in range(N_NUMBERS):
        num = random.randint(MIN_VALUE, MAX_VALUE)
        print(f"\n ✨ {num}", end=" ")  # Print numbers with some flair
    
    print("\n\n🎊 Thanks for using the Random Number Generator! Have a great day! 🌈")

if __name__ == '__main__':
    main()

# --------------------- END OF CODE ---------------------