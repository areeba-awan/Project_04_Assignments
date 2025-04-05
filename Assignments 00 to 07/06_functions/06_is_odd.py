# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 06_functions

# 06_is_odd.py

# PROBLEM STATEMENT

# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd

# SOLUTION

def main():
    print(f"\n 👋 Welcome to the Odd and Even Identifier! 🌟")
    print("\n 🔢  Let's check whether numbers from 0 to 9 are odd or even. Get ready! 🚀\n")
    
    for i in range(10):
        if is_odd(i):
            print(f"\n ✨ {i} is odd")
        else:
            print(f"\n ✨ {i} is even")
    
    print(f"\n🎉 Thanks for exploring odd and even numbers with us! Keep enjoying numbers! 💡")

def is_odd(value: int):
    """
    🔍 Checks to see if a value is odd.
    Returns True if the number is odd.
    """
    remainder = value % 2
    return remainder == 1

if __name__ == "__main__":
    main()

# ----------------------------- END OF CODE -----------------------------


