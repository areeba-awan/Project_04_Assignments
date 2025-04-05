# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 04_dictionaries

# 02_pop_up_shop.py

# PROBLEM STATEMENT :

# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5

# SOLUTION :

def fruit_shop():
    """
    A function for a fun fruit shop experience! Users can choose the quantity of fruits they want,
    and the program calculates the total cost.
    """
    fruit_dict = {
        "🍎 Apple": 2.5,
        "🍈 Durian": 10,
        "🌴 Jackfruit": 5,
        "🥝 Kiwi": 1.5,
        "🍑 Rambutan": 3,
        "🥭 Mango": 4
    }

    total = 0
    print(f"\n 👋 Welcome to the Fruity Paradise! 🌟")
    print("\n ✨ Here's our price list:")
    for fruit, price in fruit_dict.items():
        print(f"\n {fruit}: ${price} per unit")
    print("\n ⚡ Pick your favorites and we'll calculate the total!")

    for fruit_name, price in fruit_dict.items():
        try:
            quantity = input(f"\n 🟢 How many of {fruit_name} do you want?: ")
            quantity = int(quantity)
            total += price * quantity
        except ValueError:
            print(f"\n ⚠️  Invalid input for {fruit_name}. Skipping...")

    print(f"\n💰 Your total is ${total:.2f}. Thank you for shopping with us! 😊")

def main():
    """Main function to run the fruit shop program."""
    fruit_shop()

if __name__ == "__main__":
    main()

# # # # # ------------------------------- END OF THE CODE -------------------------------