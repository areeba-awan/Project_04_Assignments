# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 06_functions

# 09_sentence_generator.py

# PROBLEM STATEMENT

# Implement the helper function make_sentence(word, part_of_speech) which will take a string word and an integer part_of_speech as parameters and, depending on the part of speech,
#  place the word into one of three sentence templates (or one from your imagination!):

# If part_of_speech is 0, we will assume the word is a noun and use the template: "I am excited to add this ____ to my vast collection of them!"

# If part_of_speech is 1, we will assume the word is a verb use the template: "It's so nice outside today it makes me want to ____!"

# If part_of_speech is 2, we will assume the word is an adjective and use the template: "Looking out my window, the sky is big and ____!" make_sentence(word, part_of_speech) should not return anything, just print the correct sentence with the word filled in the blank.

# Here's a sample run of the program (user input is in blue):

# Please type a noun, verb, or adjective: groovy Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: 2 Looking out my window, the sky is big and groovy!

# SOLUTION

def make_sentence(word, part_of_speech):
    """
    ✨ Constructs a sentence based on the word and its part of speech. ✨
    """
    if part_of_speech == 0:
        # noun
        print(f"\n 📚 I am excited to add this \"{word}\" to my vast collection of nouns!")
    elif part_of_speech == 1:
        # verb
        print(f"\n 💃 It's so nice outside today it makes me want to \"{word}\"!")
    elif part_of_speech == 2:
        # adjective
        print(f"\n 🌈 Looking out my window, the sky is big and \"{word}\"!")
    else:
        # part_of_speech is invalid (not 0, 1, or 2)
        print(f"\n ⚠️ Part of speech must be 0, 1, or 2! Can't make a sentence. Please try again. 😅")

def main():
    print(f"\n 👋 Welcome to the Sentence Maker Program! 🌟")
    print("\n 🔤  This program constructs creative sentences based on the word and its part of speech. Let's start! 🚀\n")

    # User input for word and part of speech
    word: str = input("💬 Please type a noun, verb, or adjective: ")
    print("\n📖 Is this word a noun, verb, or adjective?")
    part_of_speech = int(input("\n 🧠 Type 0 for noun, 1 for verb, or 2 for adjective: "))

    # Make and display the sentence
    print("\n✍️ Here's your sentence:")
    make_sentence(word, part_of_speech)
    
    print("\n🎉 Thanks for using the Sentence Maker! Have a wonderful day! 🌈")

if __name__ == '__main__':
    main()

# ----------------------------- END OF CODE -----------------------------


