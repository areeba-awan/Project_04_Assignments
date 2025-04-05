# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 06_functions

# 07_print_divisor.py

# PROBLEM STATEMENT

# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors
#  (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the 
# division). Don't forget to call your function in main()!

# Here's a sample run (user input is in blue):

# Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12

# SOLUTION

def divisors(num):
    """
    🔍 Finds and prints all divisors of the given number.
    """
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(f"✨ {curr_divisor}", end=" ")

def main():
    print(f"\n🌟 Welcome to the Divisors Finder Program! 🌟")
    print("\n 🧮 Enter a number, and I'll find its divisors for you. Ready? 🚀\n")
    
    # Taking input from the user
    num = int(input("💬 Enter a number: "))
    print(f"\n📋 The divisors of {num} are: ", end="")
    divisors(num)

    print("\n\n🎉 Thanks for using the Divisors Finder! Keep exploring numbers! 🌈")

if __name__ == "__main__":
    main()

# ----------------------------- END OF CODE -----------------------------

