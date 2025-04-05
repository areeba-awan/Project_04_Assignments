# PROJECT # 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 00 INTRO PYTHON

# 04 HOW OLD ARE THEY

# PROBLEM STATEMENT :

# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. 
# The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):

# SOLUTION :

def main():
    """🎉 Let's calculate the ages of our friends! 🎈"""

    # Store the age of each person into a variable 🎂
    anthon_age = 21
    beth_age = anthon_age + 6
    chen_age = beth_age + 20
    drew_age = chen_age + anthon_age
    ethan_age = chen_age

    # Print the name of friends with their age 🌟
    print(f" \n 🎈 Antho is {anthon_age} years old 🎂")
    print(f" \n 🎉 Beth is {beth_age} years old 🎂")
    print(f" \n ✨ Chen is {chen_age} years old 🎂")
    print(f" \n 🎁 Drew is {drew_age} years old 🎂")
    print(f" \n 🎊 Ethan is {ethan_age} years old 🎂")

if __name__ == "__main__":
    main()

# ----------------------------- END OF THE PROGRAM -----------------------------
