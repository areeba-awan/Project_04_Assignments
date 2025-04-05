# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 07_information_flow

# 02_in_range.py

# PROBLEM STATEMENT

# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high 
# is guaranteed to be greater than low. """

# SOLUTION

def in_range(n, low, high):
    """
    🔍 Checks if the number `n` is within the range `[low, high]`.
    Returns True if the number is in range, otherwise False.
    """
    return low <= n <= high  # Using comparison operators directly for concise logic

def main():
    print(f"\n 👋 Welcome to the Range Checker Program! 🌟")
    print(f"\n 📏 Enter numbers, and I’ll tell you whether they’re within a specific range. Ready? 🚀\n")
    
    # Test cases
    print(f"\n ✅  Testing some values:")
    print(f"\n 🔢  Is 5 in the range 1 to 10? {'✔️ Yes!' if in_range(5, 1, 10) else '❌ No!'}")
    print(f"\n 🔢  Is 15 in the range 1 to 10? {'✔️ Yes!' if in_range(15, 1, 10) else '❌ No!'}")
    
    print(f"\n🎉 Thank you for using the Range Checker! Explore numbers and have fun! 🌈")

if __name__ == "__main__":
    main()

# ------------------------- END OF CODE -------------------------
