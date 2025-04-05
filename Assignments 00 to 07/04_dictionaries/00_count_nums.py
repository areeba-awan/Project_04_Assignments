
# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 04_dictionaries

# 00_count_nums.py

# PROBLEM STATEMENT :

# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 
# 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

# SOLUTION :

def get_user_numbers():
    """Prompt the user to enter numbers and return them as a list."""
    user_number: list[int] = []
    print(f"\n 👋 Welcome! Let's count how many times each number appears. 🌟")
    print("\n ✨ Keep entering numbers, and press Enter without typing anything to stop.")

    while True:
        number = input("\n 🟢 Enter a number (press Enter to stop): ")
        if number == "":  # Exit the loop when input is empty
            break
        try:
            number = int(number)  # Convert input to integer
            user_number.append(number)
        except ValueError:
            print("\n ⚠️  Please enter a valid number!")

    return user_number

def count_nums(num_list):
    """Count the occurrences of each number in the list and return a dictionary."""
    num_dict = {}
    for i in num_list:
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1
    return num_dict

def print_num_count(num_dict):
    """Display the count of each number in the dictionary."""
    print("\n 🔢   Here's the count of each number you entered:")
    for key in num_dict:
        print(f"\n 🎯 {key} appears {num_dict[key]} times")

def main():
    """Main function to run the program."""
    print("\n 🎉 Let's get started!")
    user_numbers = get_user_numbers()
    if user_numbers:
        num_dict = count_nums(user_numbers)
        print_num_count(num_dict)
    else:
        print("\n ⚠️  You didn't enter any numbers. Please try again!")

    print("\n 🌟 Thank you for using the Number Counter! Have a great day! 😊")

# Function to run code
if __name__ == "__main__":
    main()

# # # # # ------------------------------- END OF THE CODE -------------------------------