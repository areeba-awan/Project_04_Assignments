# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 02_lists

# 04 flowing_with_data_structures.py

# PROBLEM STATEMENT :

# In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

# However, there are also mutable data types where changes stay even if we don't return anything. Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

# To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

# Here is an example run of this program (user input in bold italics):

# Enter a message to copy: Hello world!

# List before: []

# List after: ['Hello world!', 'Hello world!', 'Hello world!']

# (Note. The concept of immutable/mutable data types is called mutability. Be careful because different programming languages have different rules regarding mutability!)

# SOLUTION :

def add_three_copies(my_list, data):
    """
    ✨ Function to Add Three Copies of Data to a List 🌟
    """
    for i in range(3):
        my_list.append(data)  # Append the data to the list three times 🔄

def main():
    """🎉 Main Function to Demonstrate List Modification 🚀"""
    print("\n🌟 Welcome to the List Copying Program! Let's make your list magical. ✨\n")
    
    # Prompt the user for a message to copy 📩
    message = input("\n 🖊️ Enter a message to copy: ➡️ ")
    
    # Initialize an empty list 📋
    my_list = []
    print(f"\n 📋 List before modification: {my_list}")
    
    # Call the function to add three copies of the message 🧮
    add_three_copies(my_list, message)
    
    # Display the updated list 🎊
    print(f"\n 🎯 List after modification: {my_list} 🚀")
    
    print("\n😊 Thank you for using this program! Keep creating fun lists. 🌈")

if __name__ == "__main__":
    main()

# ------------------------------- END OF THE CODE -------------------------------
