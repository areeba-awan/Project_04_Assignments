# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 05_loops_control_flow

# 05_double_it.py

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

# Maintain the current number in a variable named curr_value. When you double the number, you should be updating 
# curr_value. Recall that you can double the value of curr_value using a line like:

# curr_value = curr_value * 2

# This program should have a while loop and the while loop condition should test if curr_value is less than 100. Thus, your program will have the line:

# while curr_value < 100:


# SOLUTION

def main():
    print(f"\n 🌟 Welcome to the Multiplication Fun Program! 🌟")
    print("\n 🧮 Let's double your number repeatedly until we reach 100 or beyond. Get ready! 🚀\n")

    # Taking input from the user
    curr_value = int(input(f"\n 🔢  Enter a starting number: "))

    print("\n📈 Here's how your number grows:")
    while curr_value < 100:  # Loop until the number is at least 100
        print(f"\n ✨ {curr_value}", end=" ")  # Display the current value with some flair
        curr_value *= 2  # Multiply the number by 2
    
    print(f"\n🎉 Final value: {curr_value} 🚀 You've reached 100 or more!\n")
    print(f"\n✨ Thank you for exploring the magic of multiplication with us! ✨")

if __name__ == "__main__":
    main()

