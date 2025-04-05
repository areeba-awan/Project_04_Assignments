# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 06_functions

# 10_print_ones_digit.py

# PROBLEM STATEMENT

# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones
#  digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

# Here's a sample run (user input is in blue):

# Enter a number: 42 The ones digit is 2

# SOLUTION

def print_ones_digit(num: int):
    """
    ✨ Calculates and returns the ones digit of the given number. ✨
    """
    return num % 10

def main():
    print(f"\n 👋 Welcome to the Ones Digit Finder Program! 🌟")
    print("\n 🔢  Enter any number, and I'll find the ones digit for you. Let's get started! 🚀\n")
    
    # User input
    num = int(input("\n 💬 Please type a number: "))
    
    # Calculate and display the ones digit
    ones_digit = print_ones_digit(num)
    print(f"\n ✨ The ones digit of {num} is: {ones_digit} 🔢")

    print("\n🎉 Thank you for using the Ones Digit Finder! Keep exploring numbers! 🌈")

if __name__ == "__main__":
    main()

# ----------------------------- END OF CODE -----------------------------