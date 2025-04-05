# PROJECT 4 ASSIGNMENTS

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 01_expressions

# 06_seconds_in_year.py

# PROBLEM STATEMENT :

# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print 
# statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an 
# hour, and 60 seconds per minute.


# SOLUTION :

def main():
    """⏳ Program to Calculate the Number of Seconds in a Year 🌟"""
    # Welcome message 🎉
    print("\n ✨ Welcome to the Seconds-in-a-Year Calculator! ✨\n")
    
    # Defining constants for the calculation 🧮
    days_in_year = 365  # Number of days in a year 📅
    hours_in_day = 24   # Hours in a day ⏰
    minutes_in_hour = 60  # Minutes in an hour ⏳
    seconds_in_minute = 60  # Seconds in a minute 🔢

    # Calculate the number of seconds in a year 🧮
    seconds_in_a_year = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

    # Display the result 🎊
    print("🌟 Let's break it down:")
    print(f"\n 📅 Days in a year: {days_in_year}")
    print(f"\n ⏰ Hours in a day: {hours_in_day}")
    print(f"\n ⏳ Minutes in an hour: {minutes_in_hour}")
    print(f"\n 🔢 Seconds in a minute: {seconds_in_minute}")
    print("\n 🎯 Therefore:")
    print(f"\n ✨ There are {seconds_in_a_year:,} seconds in a year! 🚀")

    # Thank you message 🌟
    print("\n🎉 Thank you for using this calculator! Have a wonderful day! 🌈")

if __name__ == "__main__":
    main()

# ------------------------ End of Code ------------------------