# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 06_functions

# 00_averages.py

# PROBLEM STATEMENT

# Write a function that takes two numbers and finds the average between the two.

# SOLUTION

def average(a: float, b: float):
    """
    📏 Calculates the number that is halfway between a and b.
    """
    total = a + b
    return total / 2

def main():
    print(f"\n 🌟 Welcome to the Average Calculator Program! 🌟")
    print("\n 🧮 This program will calculate averages and show the halfway point between numbers. Ready? Let's go! 🚀\n")

    # Calculate averages
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    final = average(avg_1, avg_2)

    # Display results with flair
    print(f"\n 🔢  First average (0 and 10): {avg_1}")
    print(f"\n 🔢  Second average (8 and 10): {avg_2}")
    print(f"\n 🎯 Final average (avg_1 and avg_2): {final}")
    
    print(f"\n✨ Thank you for using the Average Calculator! Keep exploring the power of numbers! 💡")

if __name__ == '__main__':
    main()

# ----------------------------- END OF CODE -----------------------------
