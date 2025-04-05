# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 02_lists

# 02 double_list.py

# PROBLEM STATEMENT :

# Write a program that doubles each element in a list of numbers. For example, if you start 
# with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# SOLUTION :

def main():
    """✨ Program to Double the Numbers in a List 🎯"""
    # Welcome message 🌟
    print("\n 🔢 Welcome to the List Doubler Program! Let's multiply some numbers. 🚀\n")
    
    # Original list of numbers 📋
    numbers: list[int] = [1, 2, 3, 4]
    print(f"\n 🌈 Original list: {numbers}")
    
    # Loop through the list to double each element 🔄
    for i in range(len(numbers)):
        index_elem = numbers[i]
        numbers[i] = index_elem * 2  # Multiply each number by 2

    # Display the updated list 🎉
    print(f"\n ✨ Updated list (doubled values): {numbers} 🚀")

    # Closing message 🌟
    print("\n🎊 Thanks for using the List Doubler Program! Keep coding! 😊")

# Function to run the code 🔧
if __name__ == "__main__":
    main()

# ------------------------------- END OF THE CODE -------------------------------