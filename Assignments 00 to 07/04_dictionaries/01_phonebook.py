# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 04_dictionaries

# 01_phonebook.py

# PROBLEM STATEMENT :

# In this program we show an example of using dictionaries to keep track of information in a phonebook.

# SOLUTION :

def read_phone():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}
    print(f"\n 👋 Welcome to the Phonebook Manager! 📞")
    print("\n ✨ You can add names and numbers to your phonebook. Let's get started! 🚀")
    print("\n ⚡ Keep entering names and numbers, and press Enter without typing anything to finish.")

    while True:
        name = input("\n 🟢 Enter Name (or press Enter to stop): ")
        if name == "":
            break
        number = input("\n 🔢  Enter Number: ")
        phonebook[name] = number

    print("\n ✅ All contacts added successfully!\n")
    return phonebook

def print_phonebook(phone):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\n 📖 Here is your phonebook: 🎉")
    for name in phone:
        print(f"\n ➡️ {name} ---> {phone[name]}")
    print("\n 🌟 Thank you for reviewing your phonebook! 😊")

def lookup_num(phone):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    print(f"\n🔍 Welcome to the Phone Lookup Tool! 🧐")
    print("\n ✨ You can search for numbers by entering a name. Press Enter to stop.")
    while True:
        name = input("\n 🔎 Enter name to lookup (or press Enter to stop): ")
        if name == "":
            print("\n 👋 Exiting the lookup tool. Have a great day! 😊")
            break
        if name not in phone:
            print(f"\n ❌ {name} is not in the phonebook.")
        else:
            print(f"\n ✅  Number for {name}: {phone[name]}")

def main():
    """
    Main function to read phone numbers, print the phonebook,
    and allow the user to look up numbers.
    """
    print("\n 🌟 Let's manage your phonebook! 🚀")
    phonebook = read_phone()
    if phonebook:
        print_phonebook(phonebook)
        lookup_num(phonebook)
    else:
        print("\n ⚠️  Your phonebook is empty. Please add contacts first!")

if __name__ == '__main__':
    main()

# # # # # ------------------------------- END OF THE CODE -------------------------------
