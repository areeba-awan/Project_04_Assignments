# # # # ------------------------------- START OF THE CODE -------------------------------

# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 03_if_statements

# 01 print_events.py

# PROBLEM STATEMENT :

# Problem Statement
# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all 
# use a loop of some sort. Do no write twenty print statements

# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

# SOLUTION :

def main():
    """Main function to display the first 20 even numbers"""
    print(F"\n👋 Welcome to the Even Number Generator! 🌟")
    print("\n ✨ Get ready to see the first 20 even numbers! 🚀")
    print("\n 🔢  First 20 even numbers are:")
    
    # Loop to print the first 20 even numbers
    for i in range(0, 40, 2):
        print(f"\n 🟢 {i}", end=" ")

    print(f"\n 🎉 Thank you for using the program! Have a great day! 😊")

if __name__ == "__main__":
    main()

# # # # ------------------------------- END OF THE CODE -------------------------------