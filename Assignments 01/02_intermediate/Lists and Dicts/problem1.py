# PROJECT 4 ASSIGNMENTS 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 01

# 02_intermediate

# Lists and Dicts

# problem1.py

# PROBLEM STATEMENT

# Problem #1: List Practice

# Now practice writing code with lists! Implement the functionality described in the comments below.

#def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# Print the length of the list.


# Add 'mango' at the end of the list. 

# Print the updated list.

# PROBLEM 1 SOLUTION:

def main():
    """
    ✨ A program to manage a fruit list, showcasing its size and adding a new fruit! ✨
    """
    print(f"\n🍎 Welcome to the Fruit List Manager! 🌟")
    print("\n 🛒 Let's explore the fruits in your list and add something fresh! 🚀\n")
    
    # Initial fruit list
    fruit_list = ['\n apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Display the number of fruits
    print(f"\n 📋 Initial fruit list has {len(fruit_list)} fruits.")
    print(f"\n 🍇 Current fruits: {fruit_list}\n")
    
    # Add a new fruit
    print(f"\n ✨ Adding a fresh fruit: 'mango' 🍋")
    fruit_list.append("mango")
    
    # Display the updated fruit list
    print(f"\n📋 Updated fruit list has {len(fruit_list)} fruits.")
    print(f"\n 🍉 New fruits: {fruit_list}")
    
    print(f"\n🎉 Thanks for managing your fruit list with us! Stay fruity! 🌈")

if __name__ == "__main__":
    main()

# ------------------------------ END OF CODE --------------------------------