# PROJECT 4 ASSIGNMENTS 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 01

# 01_basics

# 01_double_it.py

# PROBLEM STATEMENT

# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# For example if the user enters the number 2 you would then print:

# 4 8 16 32 64 128

# Note that:

# 2 doubled is 4

# 4 doubled is 8

# 8 doubled is 16

# and so on.

# We stop at 128 because that value is greater than 100.

# Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value. Recall that you can double the value of curr_value using a line like:

# curr_value = curr_value * 2

# This program should have a while loop and the while loop condition should test if curr_value is less than 100. Thus, your program will have the line:

# while curr_value < 100:

# SOLUTION

MAX_VALUE: int = 100

def double(curr_value):
    """
    ✨ Doubles the value repeatedly until it reaches or exceeds MAX_VALUE. ✨
    """
    while curr_value < MAX_VALUE:
        curr_value *= 2
        print(f"💡 {curr_value}", end=" ")

def main():
    print(f"\n 👋 Welcome to the Double Up Program! 🌟")
    print(f"\n 📈 Enter a number, and I'll keep doubling it until we hit 100 or more! 🚀\n")
    
    # User input
    curr_value = int(input("\n 💬 Please enter a number: "))
    
    print(f"\n🔍 Doubling process:")
    double(curr_value)
    
    print(f"\n\n🎉 Thanks for using the Double Up Program! Have a great day! 🌈")

if __name__ == "__main__":
    main()

# ------------------ END OF CODE ------------------
