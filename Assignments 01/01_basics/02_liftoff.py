# PROJECT 4 ASSIGNMENTS 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 01

# 01_basics

# 02_liftoff.py

# PROBLEM STATEMENT

# Write a program that prints out the calls for a spaceship that is about to launch. Countdown from 10 to 1 
# and then output Liftoff!

# Here's a sample run of the program:

# 10 9 8 7 6 5 4 3 2 1 Liftoff!

# There are many ways to solve this problem. One approach is to use a for loop, and to use the for loop variable i. 
# Recall that i will keep track of how many times the for loop has completed executing its body. As an example this
#  code:


# for i in range(10): print(i)

# Will print out the values 0,


# SOLUTION 

def main():
    print(f"\n 🚀 Welcome to the Countdown Program! 🌟")
    print(f"\n ✨ Get ready for an exciting journey as we count down to liftoff! 🌌\n")

    # Countdown logic
    i = 10  # Countdown start
    while i > 0:
        print(f"\n 🔥 {i}", end=" ")  # Countdown numbers with a fire emoji
        i -= 1  # Reverse counting
    
    print(f"\n🎉 Liftoff! 🚀✨ Enjoy your adventure into the cosmos! 🌠")

if __name__ == "__main__":
    main()


