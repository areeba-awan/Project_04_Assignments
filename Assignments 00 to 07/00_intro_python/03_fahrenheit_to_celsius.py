# PROJECT 4 ASSIGNMENTS 

# AUTHOR : AREEBA TANVEER AWAN

# ASSIGNMENTS 00 TO 07

# 00 INTRO PYTHON

# 03 FAHRENHEIT TO CELSIUS


# PROBLEM STATEMENT :

# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

# The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

# The equation you should use for converting from Fahrenheit to Celsius is the following:

# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# (Note. The .0 after the 5 and 9 matters in the line above!!!)

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76

# Temperature: 76.0F = 24.444444444444443C?

# SOLUTION :

def main():
    """🌡️ Convert the temperature from Fahrenheit to Celsius 🌡️"""
    # Prompt the user to enter the temperature in Fahrenheit 🔥
    degrees_fahrenheit = input("\n 🌟 Enter the temperature 🌡️ in Fahrenheit (°F) ❄️  : ")

    # Convert the input to a float 🌟
    degrees_fahrenheit = float(degrees_fahrenheit)

    # Calculate the temperature in Celsius ❄️
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Print the temperature in Celsius 🌟
    print(f"\n 🌡️ Temperature: {degrees_fahrenheit}°F ❄️  = {degrees_celsius:.2f}°C 🔥")

    # Call the main function to run the program 🌟
if __name__ == "__main__":
    main()
 
# END OF THE PROGRAM 🌟 