# ---------------------------------------------
# 📊 6. Functions in Python
# ---------------------------------------------

# 🧠 What is a Function?
# A function is a block of code that runs only when it's called.
# Functions help us reuse code and keep programs organized.

# Python has two types of functions:
# - Built-in functions (like print(), len(), type(), etc.)
# - User-defined functions (you create them with the 'def' keyword)

# ---------------------------------------------
# 🔹 Defining and Calling a Function

# ✅ Example 1: A simple function that prints a message
def greet():
    print("Hello! Welcome to Python functions.")

# Calling the function
greet()  # This will print the message

# Explanation:
# 'greet' is the name of the function. It prints the message when called.

# ---------------------------------------------
# 🔹 Function with Parameters (Inputs)

# ✅ Example 2: Function that accepts a name and prints a greeting
def greet_user(name):
    print("Hello,", name + "!")

# Calling with an argument
greet_user("Abdullah")

# Explanation:
# 'name' is a parameter. "Abdullah" is passed as an argument.

# ---------------------------------------------
# 🔹 Function with Multiple Parameters

# ✅ Example 3: Add two numbers
def add(a, b):
    result = a + b
    print("Sum is:", result)

add(5, 7)

# Explanation:
# The function takes two numbers, adds them, and prints the result.

# ---------------------------------------------
# 🔹 Function that Returns a Value

# ✅ Example 4: Return the square of a number
def square(num):
    return num * num

value = square(4)
print("Square is:", value)

# Explanation:
# 'return' sends the result back. We can store and use it.

# ---------------------------------------------
# 🔹 Default Parameter Value

# ✅ Example 5: Function with default argument
def greet_default(name="Guest"):
    print("Hello,", name)

# Call with and without argument
greet_default("Ali")
greet_default()

# Explanation:
# If no argument is passed, "Guest" will be used as the default value.

# ---------------------------------------------
# 🔹 Keyword Arguments

# ✅ Example 6: Using keyword arguments for clarity
def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

describe_pet(animal="cat", name="Whiskers")

# ---------------------------------------------
# 🧠 Summary:
# - Define functions with 'def' keyword
# - Functions help avoid repeating code
# - Use parameters to pass data into functions
# - Use 'return' to get output from functions
# - You can set default values and use keyword arguments

# 🔧 Practice Idea:
# Write a function that takes a list of numbers and returns the largest one.
