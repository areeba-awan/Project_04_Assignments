# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 04_dictionaries

# 03_powerful_passwords.py

# PROBLEM STATEMENT :


# You want to be safe online and use different passwords for different websites. However, you are forgetful 
# at times and want to make a program that can match which password belongs to which website without storing the
#  actual password!

# This can be done via something called hashing. Hashing is when we take something and convert it into a 
# different, unique identifier. This is done using a hash function. Luckily, there are several resources that
#  can help us with this.

# For example, using a hash function called SHA256(...) something as simple as

# hello

# can be hashed into a much more complex

# 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

# Fill out the login(...) function for a website that hashes their passwords. Login should return True if an email's 
# stored password hash in stored_logins is the same as the hash of password_to_check.

# (Hint. You will need to use the provided hash_password(...) function. You don't necessarily need to know how it 
# works, just know that hash_password(...) returns the hash for the password!)

# SOLUTION :

from hashlib import sha256

def login(email, stored_logins, password_to_check):
    """
    🛡️ Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.

    📨 email: the email we are checking the password for
    📖 stored_logins: a dictionary pointing from an email to its hashed password
    🔑 password_to_check: a password we want to test alongside the email to login with
    """
    return stored_logins[email] == hash_password(password_to_check)

def hash_password(password):
    """
    🔒 Takes in a password and returns the SHA256 hashed value for that specific password.
    
    🧾 Inputs:
        password: the password we want
    
    ✨ Outputs:
        the hashed form of the input password
    """
    return sha256(password.encode()).hexdigest()

def main():
    print(f"\n 👋 Welcome to the Secure Login System! 🔐\n")
    print("\n 🌟 Let's validate some logins and ensure security is 🔒 top-notch!\n")
    
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb",
        'example@gmail.com': '98c1eb4ee93476743763878fcb96a25fbc9a175074d64004779ecb5242f645e6'
    }
    
    print("\n 🛂 Testing logins...\n")
    print(f"\n Login attempt for 'example@gmail.com' with password 'word': {login('example@gmail.com', stored_logins, 'word')}")
    print(f"\n Login attempt for 'example@gmail.com' with password 'password': {login('example@gmail.com', stored_logins, 'password')}")
    
    print(f"\n Login attempt for 'code_in_placer@cip.org' with password 'Karel': {login('code_in_placer@cip.org', stored_logins, 'Karel')}")
    print(f"\n Login attempt for 'code_in_placer@cip.org' with password 'karel': {login('code_in_placer@cip.org', stored_logins, 'karel')}")
    
    print(f"\n Login attempt for 'student@stanford.edu' with password 'password': {login('student@stanford.edu', stored_logins, 'password')}")
    print(f"\n Login attempt for 'student@stanford.edu' with password '123!456?789': {login('student@stanford.edu', stored_logins, '123!456?789')}")

    data = "word"
    hashed_data = sha256(data.encode()).hexdigest()
    print(f"\n🔑 Hashed value of 'word': {hashed_data}")

if __name__ == '__main__':
    main()

# --------------------------- END OF CODE ---------------------------
