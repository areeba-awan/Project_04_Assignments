# PROJECT 4 ASSIGNMENT : ASSIGNMENT 00 TO 07

# AUTHOR : AREEBA TANVEER AWAN

# 00_intro_python

# 02_agreement_bot.py

# PROBLEM STATEMENT:

# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

#  My favorite animal is also cow!

# SOLUTION:

def main():

    # Prompt the user to enter their favorite animal 🐾
    animal = input("\n 🤔 What's your favorite animal? 🐶🐱🐰 ")
    
    # Respond with a cheerful message including emojis 🌟
    print(f"\n 😉 My favorite animal is also {animal} ! 🐾❤️")

# Call the main function to execute the program
if __name__ == "__main__":
    main()

# -------------------- END OF THE CODE --------------------