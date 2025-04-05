# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 01_expressions

# 07 tiny mad lib 

# PROBLEM STATEMENT :

# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun 
# sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually
#  filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning 
# of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!



# SOLUTION :

def main():
    """🎉 Mad Libs Game: Create Your Own Fun Sentence! 🎯"""
    print("\n ✨ Welcome to the Mad Libs Game! Let's make a fun story together. 🌟\n")
    
    # Prompt the user for words 🔤
    adjective = input("\n 🌈 Please type an adjective and press enter: ➡️   ")
    noun = input("\n 🛠️ Please type a noun and press enter: ➡️   ")
    verb = input("\n 🚀 Please type a verb and press enter: ➡️   ")

    # Create the sentence with user input ✍️
    SENTENCE_START = "Code in Place is fun."
    story = f"\n {SENTENCE_START} I learned to program and used Python to make my {adjective} {noun} {verb}! 🎉"
    
    # Display the story ✨
    print("\n🎊 Here's your personalized story: 🎊")
    print(story)

    # Thank the user 🌟
    print("\n🌈 Thanks for playing! Keep creating fun stories! 😊")

if __name__ == "__main__":
    main()

# ------------------------ End of Code ------------------------