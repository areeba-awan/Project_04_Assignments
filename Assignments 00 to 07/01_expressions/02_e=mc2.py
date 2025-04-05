# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 01_expressions

# 02_e=mc2.py

# PROBLEM STATEMENT :

# Write a program that continually reads in mass from the user and then outputs the equivalent energy using
#  Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!

# SOLUTION :

def main():
    """💡 Program to Calculate Energy using E=mc² ⚡"""

    # Prompt the user to enter the mass 🌟
    mass: float = float(input("\n🌍 Enter the mass of your body in kilograms (kg): ➡️  "))

    # Speed of light in m/s 🌠
    c: int = 299792458

    # Equation to calculate energy 🧮
    energy = mass * c ** 2

    # Print the energy 🌟
    print("\n🌟 Here's your energy calculation based on E = m * c²: ⚡")
    print(f"\n 📏 Mass (m) = {mass} kg")
    print(f"\n 💫 Speed of Light (c) = {c} m/s")
    print(f"\n ⚡ Energy (e) = {energy} joules 🎉")

if __name__ == "__main__":
    main()

# ----------------------------- END OF THE PROGRAM -----------------------------

