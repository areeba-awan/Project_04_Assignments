# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 07_information_flow

# 05_subtract_7.py

# PROBLEM STATEMENT

# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to 
# call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

# SOLUTION

def subtract_seven(num):
    """
    ✨ Subtracts 7 from the given number and returns the result. ✨
    """
    return num - 7

def main():
    print(f"\n 👋 Welcome to the Subtract Seven Program! 🌟")
    print("\n 🧮 Enter a number, and I'll subtract 7 for you. Simple and fun! 🚀\n")

    try:
        # User input
        num = int(input(f"\n 💬 Please enter a number: "))
        # Output the result
        print(f"\n 🎉 The result is: {subtract_seven(num)} ✨")
    except ValueError:
        # Handle invalid input
        print(f"\n ❌ Invalid input. Please type a valid integer! 🔢")

    print(f"\n🌈 Thank you for using the Subtract Seven Program! Have a great day! 🌟")

if __name__ == "__main__":
    main()

# ------------------------------ END OF CODE  --------------------------