# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 02_lists

# 01 add many numbers

# PROBLEM STATEMENT :

# Write a function that takes a list of numbers and returns the sum of those numbers.

# SOLUTION :

# FUNCTION TO TAKE A LIST OF NUMBERS AND RETURN THE SUM OF THOSE NUMBERS

def add_many_numbers(numbers) -> int:
    """
    ✨ Takes in a list of numbers and returns the sum of those numbers. ✨
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number  # Add each number to the total
    return total_so_far

def main():
    """🎉 Main Function to Calculate the Sum of Numbers 🎯"""
    print("\n 🔢 Welcome to the Number Summation Program! ✨\n")
    
    # Example list of numbers
    numbers: list[int] = [1, 2, 3, 4, 5, 6]  # Create a list of numbers 📋
    print(f"\n🌟 Numbers in the list: {numbers}")
    
    # Calculate the sum of the numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum using the function
    
    # Display the result 🎉
    print(f"\n 🎊 The sum of the numbers is: {sum_of_numbers} 🚀")

    # Thank you message 🌈
    print("\n😊 Thank you for using the program! Keep coding and stay awesome! 💻✨")

if __name__ == '__main__':
    main()

# ------------------------ End of Code ------------------------
