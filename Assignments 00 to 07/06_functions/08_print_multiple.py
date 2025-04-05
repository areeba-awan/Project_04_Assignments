# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 06_functions

# 08_print_multiple.py

# PROBLEM STATEMENT

# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message. We've written the main() function for you, which prompts the user for a message and a number of repeats.

# Here's a sample run of the program (user input is in blue):

# Please type a message: Hello! Enter a number of times to repeat your message: 6 Hello! Hello! Hello! Hello! Hello! Hello!

# SOLUTION

def repeat(message: str, repeat_count: int):
    """
    🌟 Repeats the input message a specified number of times and returns the result. 🌟
    """
    return " ".join([message] * repeat_count)

def main():
    print(f"\n ✨ Welcome to the Message Repeater Program! ✨")
    print("\n 🔁 This program will repeat your message as many times as you'd like. Ready? 🚀\n")

    # Collect user inputs
    message = str(input("\n 💬 Please type a message: "))
    repeat_count = int(input("\n 🔢  Enter the number of times to repeat your message: "))

    # Repeat the message and display the result
    repeat_message = repeat(message, repeat_count)
    print("\n📝 Your repeated message:")
    print(f"\n 🎉 {repeat_message} 🎉")

    print("\n✨ Thanks for using the Message Repeater! Have fun! 💡")

if __name__ == "__main__":
    main()

# ----------------------------- END OF CODE -----------------------------
