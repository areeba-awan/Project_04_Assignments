 # PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 05_loops_control_flow

# 03_wholesome_machine.py

# PROBLEM STATEMENT

# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing 
# anything I put my mind to.") until they type it correctly. Sometimes, especially in the midst of such uncertain
#  times, we just need to be reminded that we are resilient, capable, and strong; this little Python program may 
# be able to help!

# Here's a sample run of the program (user input is in blue):

# Please type the following affirmation: I am capable of doing anything I put my mind to.
#  Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. 
# I am capable of doing anything I put my mind to. That's right! :)

# Note that you can call input() with no prompt and it will still wait for a user to type something!

# SOLUTION

affirmation_sentence = """I am capable of doing anything I put my mind to."""

def main():
    print(f"\n 🌟 Welcome to the Daily Affirmation Exercise! 🌈")
    print("\n 💪 Let's build positivity together. Type the following affirmation exactly as it is written below: \n")
    print(f"\n ✍️ \"{affirmation_sentence}\"\n")

    # Prompt the user to type the affirmation
    user = input(f"\n 📝 Your turn: ")
    while user != affirmation_sentence:
        print("\n ❌ Hmmm, that wasn't quite right. Let's try again! 🤔\n")
        print(f"\n 💬 Please type the following affirmation again: \n✍️ \"{affirmation_sentence}\"\n")
        user = input("📝 Your turn: ")

    print("\n🎉 Fantastic! 🌟 You typed it perfectly!")
    print("\n👏 \"I am capable of doing anything I put my mind to.\" That's the spirit! 🚀 Keep believing in yourself! 💖")

if __name__ == "__main__":
    main()

# ----------------------------- END OF CODE -----------------------------
