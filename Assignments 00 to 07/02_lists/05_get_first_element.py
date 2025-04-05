# PROJECT 4 ASSIGNMENT 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 02_lists

# 05 get_first_element.py

# PROBLEM STATEMENT :

# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the
# first element in the list. 
# The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

# SOLUTION :

def get_first_element(lst):
    """Function to display the first element of the list"""
    print("\n 🌟 Here's the first element of your list: 🎉", lst[0])

def prompt_list():
    """Prompt the user to enter elements for the list"""
    lst = []
    print("\n 👋 Welcome! Let's create your list. 📝")
    print(f"\n 👉 Please enter the elements for your list one by one.")
    print("\n ⚡ Press Enter without typing anything to finish.")

    prompt = input("\n ✨ Enter the first element: ")
    while prompt != "":
        lst.append(prompt)
        prompt = input("\n ➡️  Add another element (or press Enter to finish): ")
    return lst

def main():
    lst = prompt_list()
    if lst:  # Check if the list is not empty
        get_first_element(lst)
    else:
        print("\n ⚠️ Your list is empty. Please try again!")

if __name__ == "__main__":
    main()

# ------------------------------- END OF THE CODE -------------------------------
