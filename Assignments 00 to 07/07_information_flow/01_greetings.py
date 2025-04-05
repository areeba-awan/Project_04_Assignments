# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 07_information_flow

# 01_greetings.py

# PROBLEM STATEMENT

# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

# Here's a sample run of the program (user input in bold italics):

# What's your name? Sophia

# Greetings Sophia!

# SOLUTION

def main():
    print(f"\n 👋 Welcome to the Personalized Greeting Program! 🌟")
    print("\n ✨ Let's make someone feel special with a warm greeting! 💖\n")

    # Prompt user for their name
    name: str = input("\n 💬 What's your name? ")

    # Call the greet function and display the result
    print(f"\n 🎉 {greet(name)} 🎉")
    print(f"\n 🌈 Thanks for stopping by! Have a wonderful day! 🌟")

def greet(name):
    """
    ✨ Generates a personalized greeting for the given name. ✨
    """
    return f"Greetings, {name}! 😊"

if __name__ == '__main__':
    main()
    
# ----------------------------- END OF CODE -----------------------------
