# PROJECT 4 ASSIGNMENT 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 02_lists

# 08 shorten.py

# PROBLEM STATEMENT :

# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, 
# and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than
#  MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes 
# it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but 
# feel free to change it around to test your program.

# SOLUTION :

def shorten(lst):
    """Function to remove elements from the end of the list until it is MAX_LENGTH items long"""
    MAX_LENGTH = 3
    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()
        print(f"\n ❌ Removing '{removed_element}' from the list to keep it within {MAX_LENGTH} items!")

def prompt_list():
    """Prompt the user to enter elements for the list"""
    lst = []  # Initialize an empty list
    print("\n 👋 Welcome to the List Shortener! ✂️")
    print("\n ✨ You can create your list, and I'll help you keep only the first 3 elements.")
    print("\n 🚀 Let's get started!")

    # Prompt the user to enter elements for the list
    elem = input("\n 🟢 Enter an element to add to the list (press Enter to stop): ")
    while elem != "":
        lst.append(elem)
        elem = input("\n ➡️  Enter the next element (or press Enter to finish): ")
    return lst

def main():
    """Main function to run the program"""
    print("\n 🎉 Ready to create your awesome list?")
    lst = prompt_list()  # Get the list from the user
    if lst:  # Ensure the list is not empty
        print(f"\n ✅  Original list: {lst}")
        shorten(lst)  # Shorten the list
        print(f"\n 🌟 Final list after shortening: {lst}")  # Display the final list
    else:
        print("\n ⚠️ Oops! Your list is empty. Try again with some elements.")

# Function to run the code
if __name__ == "__main__":
    main()

# # # ------------------------------- END OF THE CODE -------------------------------

