# PROJECT 4 ASSIGNMENT : ASSIGNMENT 00 TO 07

# AUTHOR : AREEBA TANVEER AWAN

# 00_intro_python

# 01_add_two_numbers.py

# PROBLEM STATEMENT:

# Write a Python program that takes two integer inputs from the user and calculates their sum. 
# The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main()
#  function guides the user through the process of entering two numbers and displays their sum.

# SOLUTION:

def main():
    # Prompt the user to enter the first number
    num1 = input("\n 🎯 Enter the first number : ")
    # Convert the input to an integer
    num1 = int(num1)
    # Prompt the user to enter the first number
    num2 = input("\n 🎯 Enter the Second number : ")
    # Convert the input to an integer
    num2 = int(num2)
    # Calculate the sum of the two numbers
    sum = num1 + num2
    # Print the total sum with an appropriate message
    print(f"\n ➰ The sum of {num1} and {num2} is : {sum}")

#  code to call the Main function
if __name__ == "__main__":
    main()

# ----------------------------- END OF THE PROGRAM -----------------------------