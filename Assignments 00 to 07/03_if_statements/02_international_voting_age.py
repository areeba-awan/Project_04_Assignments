
# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 03_if_statements

# 02_international_voting_age.py

# PROBLEM STATEMENT :

# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.

# SOLUTION :

def main():
    """This function asks the user for their age and lets them know if they can or can't 
    vote in the following three fictional countries."""
    print(f"\n 👋 Welcome to the Voting Eligibility Checker! 🌟")
    print("\n ✨ Let's see if you're eligible to vote in three unique countries. 🚀")

    try:
        age = int(input("\n 🟢 How old are you? "))

        print("\n 🔍 Checking your eligibility in each country...")

        # Peturksbouipo
        if age >= 16:
            print("\n ✅  You can vote in 🏙️ **Peturksbouipo** where the voting age is 16.")
        else:
            print("\n ❌ You cannot vote in 🏙️ **Peturksbouipo** where the voting age is 16.")

        # Stanlau
        if age >= 25:
            print("\n ✅  You can vote in 🏞️ **Stanlau** where the voting age is 25.")
        else:
            print("\n ❌ You cannot vote in 🏞️ **Stanlau** where the voting age is 25.")

        # Mayengua
        if age >= 48:
            print("\n ✅  You can vote in 🌄 **Mayengua** where the voting age is 48.")
        else:
            print("\n ❌ You cannot vote in 🌄 **Mayengua** where the voting age is 48.")

        print("\n 🎉 Thank you for using the Voting Eligibility Checker! Have a great day! 😊")
    except ValueError:
        print(f"\n ⚠️ Please enter a valid age (a number)!")

if __name__ == "__main__":
    main()

# # # # ------------------------------- END OF THE CODE -------------------------------
