# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 07_information_flow

# 04_multiple_returns.py

# PROBLEM STATEMENT

# There are times where you are working with lots of different data within a function that you want to return. While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with multiple bits of data.

# To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website. Fill out the get_user_data() function which:

# Asks the user for their first name and stores it in a variable

# Asks the user for their last name and stores it in a variable

# Asks the user for their email address and stores it in a variable

# Returns all three of these pieces of data in the order it was asked

# You can return multiple pieces of data by separating each piece with a comma in the return line.

# Here is an example run of the program:

# What is your first name?: Jane

# What is your last name?: Stanford

# What is your email address?: janestanford@stanford.edu

# Received the following user data: ('Jane', 'Stanford', 'janestanford@stanford.edu')

# (Note. This idea is called tuple packing/unpacking. We "pack" our return values into a single data structure called a tuple. We can then "unpack" these values back into our original values or leave them as a tuple.)

# SOLUTION



def get_user_info():
    """
    ✨ Collects user information: First Name, Last Name, and Email. ✨
    """
    user_info = {
        "First Name": input("\n 👤 What is your first name?: "),
        "Last Name": input("\n 👥 What is your last name?: "),
        "Email": input("\n 📧 What is your email address?: ")
    }
    return user_info  

def main():
    print(f"\n 👋 Welcome to the User Info Collector Program! 🌟")
    print("\n 📋 Please enter your details, and I'll display them neatly for you. Let's get started! 🚀\n")

    # Collect user data
    user_data = get_user_info()

    # Display collected data
    print("\n🎉 Received the following user data:")
    for key, value in user_data.items():  # Pretty Print
        print(f"\n ✨ {key}: {value}")
    
    print("\n🌈 Thank you for using the User Info Collector! Have a wonderful day! 💖")

if __name__ == "__main__":
    main()

# ------------------------- END OF CODE -------------------------
