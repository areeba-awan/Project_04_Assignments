# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 07_information_flow

# 03_in_stock.py

# PROBLEM STATEMENT

# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

# Here's two sample runs of the program (user input in bold italics):

# Enter a fruit: pear

# This fruit is in stock! Here is how many:

# 1000

# Enter a fruit: lychee

# This fruit is not in stock.

# SOLUTION

inventory: dict = {
    "apple": 100,
    "mango": 200,
    "banana": "2 dozen",
    "peer": 1000,
    "watermelon": 10
}

def in_stock(fruit):
    """
    🌟 Checks if the fruit is in stock and displays the quantity.
    """
    if fruit in inventory:
        print(f"\n ✅ This fruit is in stock! 🛒 Quantity: {inventory[fruit]}")
    else:
        print("\n ❌ Sorry, this fruit is not in stock. 😔")

def main():
    print(f"\n 👋 Welcome to the Fruit Inventory Checker! 🌟")
    print(f"\n 🍎 Explore your favorite fruits and check their availability. Ready? 🚀\n")

    # Prompt the user to enter a fruit name
    fruit = input("\n 💬 Enter the name of a fruit: ").lower().strip()  # Normalize input by stripping spaces and converting to lowercase
    print("\n  🔍 Checking stock...")
    in_stock(fruit)

    print("\n 🎉 Thanks for using the Fruit Inventory Checker! Have a fruitful day! 🌈")

if __name__ == "__main__":
    main()

# ------------------------- END OF CODE -------------------------
