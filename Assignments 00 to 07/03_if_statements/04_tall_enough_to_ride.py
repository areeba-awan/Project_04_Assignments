
# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 03_if_statements

# 04_tall_enough_to_ride.py

# PROBLEM STATEMENT :

# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

# Here's two sample runs (user input is in bold italics):

# How tall are you? 100

# You're tall enough to ride!

# How tall are you? 10

# You're not tall enough to ride, but maybe next year!

# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this? See the function tall_enough_extension() in the solution code!)

# SOLUTION :


def main():
    """This function asks the user how tall they are and prints whether or not they're taller than 
    a pre-specified minimum height."""
    print(f"\n 🎢 Welcome to the Height Checker for Thrill Rides! 🌟")
    print("\n ✨ Let's see if you're tall enough to enjoy the ride! 🚀")
    print("\n ⚡ Enter your height in centimeters. Press Enter without typing anything to quit.")

    while True:
        height = input(f"\n 🟢 How tall are you? ")
        if height == "":  # Exit the loop if the input is empty
            print("\n 👋 Thank you for checking! Have a fantastic day! 😊")
            break
        try:
            height = int(height)
            if height >= 50:
                print("\n ✅  You're tall enough to ride! 🎉 Enjoy the adventure! 🌟")
            else:
                print("\n ❌ You're not tall enough to ride, but keep growing! Maybe next year! 🌱")
        except ValueError:
            print("\n ⚠️  Please enter a valid number for your height!")

if __name__ == "__main__":
    main()

# --------------------------- END OF CODE ---------------------------

