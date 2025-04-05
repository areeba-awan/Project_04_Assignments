# PROJECT 4 ASSIGNMENT

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 06_functions

# 01_chaotic_counting.py

# PROBLEM STATEMENT

# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch. 
# We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number, 
# before printing the number, you should call done() and check if it returns True or not. If done() returns True,
#  we're done counting, and you should use a return statement to end the chaotic_counting() function execution
#  and resume execution of main(), which will print "I'm done.". We've written main() for you -- check it out!
#  Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

# Here's a sample run of this program:

# I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.

# SOLUTION

import random  # ✅ Import random module

DONE_LIKELIHOOD = 0.3  # 🎲 Probability setting for when to stop

def chaotic_counting():
    """
    🌟 Counts numbers from 1 to 10, stopping randomly based on DONE_LIKELIHOOD.
    """
    for i in range(10):
        curr_num = i + 1
        if done():
            print(f"\n⏹️  Stopping early... felt like it! 😄")
            return
        print(f"\n 🔢  {curr_num}", end=" ")

def done():
    """
    🎲 Returns True with a probability of DONE_LIKELIHOOD.
    """
    return random.random() < DONE_LIKELIHOOD

def main():
    print(f"\n 👋 Welcome to the Chaotic Counting Program! 🌟")
    print("\n 🤔 I'll count from 1 to 10, but there's a twist! I may stop randomly based on how I feel 🎲\n")
    chaotic_counting()
    print("\n🎉 All done! Thanks for joining the fun! 🚀")

if __name__ == "__main__":
    main()

# ----------------------------- END OF CODE -----------------------------
