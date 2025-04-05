# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 06_functions

# 04_double.py

# PROBLEM STATEMENT

# Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() 
# function for you which asks the user for a number, calls your code for double(num) , and prints the result.

# Here's a sample run of the program (user input in bold italics):

# Enter a number: 2 Double that is 4

# SOLUTION

def main(number):
    """
    🌟 Function to calculate the double of the given number. 🌟
    """
    double_number = number * 2
    return double_number

if __name__ == "__main__":
    print(f"\n👋 Welcome to the Number Doubler Program! 🌟")
    print("\n 🔢  Enter a number, and I'll double it for you. Ready? 🚀\n")
    
    # User input
    number = int(input(f"\n 💬 Enter a number: "))
    
    # Calculate the result using the main function
    result = main(number)
    
    # Display the result with emojis
    print(f"\n ✨ You entered: {number}")
    print(f"\n 🎯 Double that is: {result}")
    
    print("\n🎉 Thanks for using the Number Doubler! Keep having fun with numbers! 💡")

# ----------------------------- END OF CODE -----------------------------