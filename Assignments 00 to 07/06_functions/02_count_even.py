# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 06_functions

# 02_count_even.py

# PROBLEM STATEMENT

# Fill out the function count_even(lst) which

# first populates a list by prompting the user for integers until they press enter (please use the
#  prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on

# SOLUTION

def count_even(lst):
    even_numbers = []
    
    print(f"\n 🌟 Let's create a list and find even numbers together! 🌟\n")
    
    while True:
        values = input("\n 🔢  Enter an integer or press Enter to stop: ")
        if values == "":
            break
        lst.append(int(values))

    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
            
    print("\n📋 Your full list: ", lst)
    print(f"\n ✨ Even numbers in the list are: {even_numbers}")

def main():
    print(f"\n 👋 Welcome to the Even Number Finder Program! 🌈")
    print("\n 🎯 Enter integers to build your list, and I'll help you find the even ones. Let's begin! 🚀\n")
    
    user_list = []
    count_even(user_list)
    
    print("\n 🎉 Thank you for using the Even Number Finder! Keep exploring! 💡")

if __name__ == "__main__":
    main()

# ----------------------------- END OF CODE -----------------------------

