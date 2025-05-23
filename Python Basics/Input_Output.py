# ---------------------------------------------
# 📥📤 2. Input and Output in Python
# ---------------------------------------------

# 🤔 What is Input and Output?
# Input means getting data from the user.
# Output means showing data to the user (usually on screen).

# ---------------------------------------------
# 🖥️ Output using print()

# The print() function displays data on the screen.
# You can print text, numbers, or variables.

print("Hello, World!")  # Prints the text Hello, World! on the screen

# Printing multiple items separated by commas adds spaces automatically
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
# Output: Name: Alice Age: 25

# You can also format strings for cleaner output
print(f"My name is {name} and I am {age} years old.")
# f-string is used to embed variables directly into the string

# ---------------------------------------------
# ⌨️ Input using input()

# The input() function asks the user to type something and presses Enter
# It always returns user input as a string

user_name = input("Enter your name: ")  # Shows prompt and waits for input
print("Hello,", user_name)  # Greets the user by name

# Getting numeric input requires converting the string to a number
user_age = input("Enter your age: ")  # Takes input as string, e.g., "30"
# Convert string input to integer using int()
user_age = int(user_age)  # Now user_age is a number (int)

# Use the age in a calculation or message
next_year_age = user_age + 1
print(f"Next year, you will be {next_year_age} years old.")

# ---------------------------------------------
# 🧠 Summary:
# - Use print() to show data/output on the screen
# - Use input() to get data from the user (always returns string)
# - Convert input string to int or float if numeric value is needed
# - Use f-strings or commas to format output messages nicely

# ---------------------------------------------
# 🧪 Practice:
# Try writing a program that asks the user for their favorite color
# and then prints a message like "Your favorite color is Blue."
