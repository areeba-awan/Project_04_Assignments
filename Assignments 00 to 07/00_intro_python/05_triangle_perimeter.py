# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 00 INTRO PYTHON

# 05 TRIANGLE PERIMETER

# PROBLEM STATEMENT :

# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the 
# perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5


# SOLUTION :

def main():
    """🎉 Program to Calculate the Perimeter of the Triangle 🎈"""
    # Prompt the user to enter the length of each side of the triangle 📐
    side1 = float(input("\n ✨ What is the length of side 1 (in units)? ➡️    "))
    side2 = float(input("\n 🌟 What is the length of side 2 (in units)? ➡️    "))
    side3 = float(input("\n 💫 What is the length of side 3 (in units)? ➡️    "))

    # Calculate the perimeter 🧮
    perimeter = side1 + side2 + side3

    # Print the perimeter of the triangle 🌟
    print(f"\n 🎈 The perimeter of the triangle is: {perimeter} units 🏆")

if __name__ == "__main__":
    main()

# ----------------------------- END OF THE PROGRAM -----------------------------
