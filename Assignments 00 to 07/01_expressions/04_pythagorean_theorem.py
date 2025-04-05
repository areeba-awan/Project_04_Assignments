# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 01_expressions

# 04_pythagorean_theorem.py

# PROBLEM STATEMENT :

# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle 
# and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in
#  geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square 
# of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean
#  theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). 
# You will probably find math.sqrt() to be useful.

# Here's a sample run of the program (user input is in bold italics):

# Enter the length of AB: 3

# Enter the length of AC: 4

# The length of BC (the hypotenuse) is: 5.0

# SOLUTION :

from math import sqrt

def main():
    """📐 Calculate the Hypotenuse of a Right Triangle 🌟"""

    # Prompt the user to enter the lengths of two perpendicular sides of the triangle 🟦 🟩

    print("\n 🔺 Let's find the length of the hypotenuse of a right triangle!")

    side1 = float(input("\n 🟦 Enter the length of side AB (in units): ➡️  "))
    side2 = float(input("\n 🟩 Enter the length of side AC (in units): ➡️  "))

    # Calculate the hypotenuse using the Pythagorean theorem 🧮
    side3 = sqrt(side1**2 + side2**2)

    # Display the result 🎉
    print("\n✨ Here's the result based on the Pythagorean theorem 🏆 : ✨")
    print(f"\n 🔹 Length of side AB = {side1} units")
    print(f"\n 🔹 Length of side AC = {side2} units")
    print(f"\n 💫 Length of hypotenuse BC = {side3:.2f} units 🌟")

if __name__ == "__main__":
    main()

# ----------------------------- END OF THE PROGRAM -----------------------------
