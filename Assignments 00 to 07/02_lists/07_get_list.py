# PROJECT 4 ASSIGNMENT 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 02_lists

# 07 get_list.py

# PROBLEM STATEMENT :

# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

# SOLUTION :


def get_list(lst):
    """Function to display the entire list"""
    print("\n🌟 Here's your list of elements: 🎉", lst)

def prompt_list():
    """Prompt the user to enter elements for the list"""
    lst = []  # Initialize an empty list
    print(f"\n 👋 Welcome! Let's build a fantastic list together! 📝")
    print("\n ✨ Start adding items one by one, and press Enter when you're done.")
    print("\n ⚡ Ready? Let's get started!")

    # Ask for the first element
    prompt = input("\n 🟢 Enter the first element for your list: ")
    while prompt != "":  # Keep asking for more elements until the user stops
        lst.append(prompt)  # Add the element to the list
        prompt = input("\n ➡️  Enter another element (or press Enter to finish): ")
    return lst

def main():
    """Main function to run the program"""
    print("\n 🎉 Let's create your list now!")
    lst = prompt_list()  # Get the list from the user
    if lst:  # Ensure the list is not empty
        get_list(lst)  # Display the list
    else:
        print("\n ⚠️ Oops! Your list is empty. Please try again!")

if __name__ == "__main__":
    main()

# # # ------------------------------- END OF THE CODE -------------------------------
