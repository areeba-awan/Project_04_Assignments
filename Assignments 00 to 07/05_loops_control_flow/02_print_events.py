 # PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 05_loops_control_flow

# 02_print_events.py

# PROBLEM STATEMENT

# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a 
# loop of some sort. Do no write twenty print statements

# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

# SOLUTION

def main():
    print(f"\n 🌟 Welcome to the Even Numbers Generator! 🌟")
    print("\n ✨ This program will generate the first 20 even numbers for you. Ready? Let’s go! 🚀\n")

    # Using a for-loop to generate even numbers
    print("\n 🔢  Generating even numbers using the for-loop:")
    for i in range(20):  # Loop from 0 to 19
        print(f"\n 💡 {i * 2}", end=" ")  # Use 'i' to calculate even numbers
    print("\n\n🎉 Done with the for-loop approach! 🎉\n")

    # Using a while-loop to generate even numbers
    print(f"\n 🔢  Generating even numbers using the while-loop:")
    num = 0  # First even number
    count = 0  # Counter to keep track of how many numbers have been generated

    while count < 20:
        print(f"\n 💡 {num}", end=" ")  # Display the current even number
        num += 2  # Calculate the next even number
        count += 1  # Increment the counter
    print(f"\n\n🎊 You've successfully generated 20 even numbers! Hope you enjoyed it! 🌈")

if __name__ == "__main__":
    main()

# ----------------------------- END OF CODE -----------------------------


