# PROJECT 4 ASSIGNMENTS 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 01

# 01_basics

# 00_joke_bot.py

# PROBLEM STATEMENT

# Problem Statement
# Write a simple joke bot. The bot starts by asking the user what they want. However, your program will only respond to one response: Joke.

# If the user enters Joke then we will print out a single joke. Each time the joke is always the same:

# Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

# If the user enters anything else we print out:

# Sorry I only tell jokes

# You should use the three constants:

# PROMPT JOKE SORRY

# which contain the strings for the prompt asked to the user, the joke to print out if the user enters Joke and the sorry message if the user enters anything else.

# Your program will need to use an if statement which checks if the user input is Joke:

# if user_input == "Joke":

# Recall that == is a comparison which tests if two values are equal to one another.

# Here is a full run of the program (user input is in blue):

# What do you want? Joke Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

# SOLUTION 

# Constants (as per the problem statement)

PROMPT = "💬 What do you want? "
JOKE = (
    "😂 Here is a joke for you! Sophia is heading out to the grocery store. "
    "A programmer tells her: \"Get a liter of milk, and if they have eggs, get 12.\" "
    "Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: \"Because they had eggs.\" 🤓"
)
SORRY = "❌ Sorry, I only tell jokes. Maybe next time! 😊"

# Function to handle user input
def joke_bot(prompt_user: str) -> str:
    """
    ✨ Responds with a joke or an apology based on user input. ✨
    """
    if prompt_user.lower().strip() == "joke":
        return JOKE
    else:
        return SORRY  


def main():
    print(f"\n 👋 Welcome to the Joke Bot Program! 🌟")
    print(f"\n 😂 Type 'joke' to hear a funny programmer joke, or type anything else for my response. Let's have some fun! 🚀\n")
    
    user_input = input(PROMPT)  # User input
    print(f"\n🤖 Bot Response:")
    print(joke_bot(user_input))

    print(f"\n🎉 Thanks for chatting with Joke Bot! Have a laughter-filled day! 🌈")

if __name__ == "__main__":
    main()

# ---------------------- END OF CODE ----------------------
