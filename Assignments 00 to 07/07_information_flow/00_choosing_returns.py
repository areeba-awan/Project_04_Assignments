# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 07_information_flow

# 00_choosing_returns

# PROBLEM STATEMENT

# There are times where we want to return different things from a function based on some condition.
#  To practice this idea, imagine that we want to check if someone is an adult. We might check their age and
#  return different things depending on how old they are!

# We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an
#  adult (in the United States). Fill out the is_adult(age) function, which returns True if the function 
# takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, 
# return False instead.

# Here are two sample runs of the program, one for each return option (user input in bold italics):

# (Entered age is an adult age)

# How old is this person?: 35

# True

# (Entered age is not an adult age)

# How old is this person?: 7

# False

# SOLUTION

ADULT_AGE = 18

def isAdultAge(age):
    """
    🔍 Checks if the given age meets the adult age threshold.
    Returns True if age is 18 or above, otherwise False.
    """
    return age >= ADULT_AGE

def main():
    print(f"\n 👋 Welcome to the Adult Age Checker Program! 🌟")
    print("\n 🧮 Let's find out if someone is considered an adult based on their age. 🚀\n")

    # Prompt user for input
    age = int(input(f"\n 💬 How old is this person? 🔢  : "))

    # Check and display the result
    if isAdultAge(age):
        print(f"\n 🎉 Yes, at {age} years old, this person is an adult! 💪")
    else:
        print(f"\n ❌ Nope, at {age} years old, this person is not yet an adult. 🧒")
    
    print(f"\n✨ Thank you for using the Adult Age Checker! Keep exploring the possibilities! 🌈")

if __name__ == "__main__":
    main()

# ------------------------ END OF CODE ------------------------