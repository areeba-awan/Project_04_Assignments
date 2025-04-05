# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 06_functions

# 05_get_name.py

# PROBLEM STATEMENT

# Fill out the get_name() function to return your name as a string! We've written a main() function for you 
# which calls your function to retrieve your name and then prints it in a greeting.

# Here's a sample run of the program where the name we've decided to return is Sophia (the autograder expects
#  the returned name to be Sophia):

# Howdy Sophia ! 🤠

# SOLUTION

def get_name(name):
    """
    ✨ Function to return the name passed as input.
    """
    return name

def main():
    print(f"\n 🌟 Welcome to the Personalized Greeting Program! 🌟")
    print("\n 🎉 Let's greet someone in style! 🤠\n")

    # Calling the get_name function
    print(f"\n Howdy, {get_name('Areeba')}! 🤠 Hope you’re having a fantastic day! 🌈")

if __name__ == "__main__":
    main()

# ----------------------------- END OF CODE -----------------------------

