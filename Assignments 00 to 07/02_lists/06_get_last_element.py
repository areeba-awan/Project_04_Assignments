# PROJECT 4 ASSIGNMENT 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 02_lists

# 06 get_last_element.py

# PROBLEM STATEMENT :

# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element
#  in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.


# SOLUTION :

def get_last_element(lst):
    """Function to display the last element of the list"""
    print(f"\n 🌟 Here's the last element of your list: 🎉", lst[-1])

def get_lst():
    """Function to create a list from user input"""
    lst = []  # Start with an empty list
    print(f"\n 👋 Welcome to the List Builder! 📝")
    print("\n ✨ Let's create a list together. You must add at least one item.")
    print("\n 👉 Keep adding items, and press Enter when you're done.")

    # Ask for the first item
    element = input("\n 🟢 Enter the first item for your list: ")
    while not element:  # Ensure the user enters at least one item
        element = input("\n ⚠️ Please enter at least one item: ")

    lst.append(element)  # Add the first item to the list

    # Keep asking for more items
    while True:
        element = input("\n ➡️  Enter another item (or press Enter to stop): ")
        if element:  # If input is not empty, add it to the list
            lst.append(element)
        else:  # Stop when the input is empty
            break
    return lst

def main():
    """Main function to run the program"""
    print("\n 🎉 Let's get started!")
    lst = get_lst()  # Get the list from the user
    if lst:  # Ensure the list is not empty
        get_last_element(lst)  # Display the last element
    else:
        print("\n ⚠️ Oops! Something went wrong, and your list is empty.")

if __name__ == "__main__":
    main()

# # ------------------------------- END OF THE CODE -------------------------------