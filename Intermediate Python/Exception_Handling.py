# ---------------------------------------------------
# Exception Handling
# ---------------------------------------------------

# 🤔 What is Exception Handling?
# Exceptions are errors that occur during the execution of a program.
# Exception handling allows you to manage errors gracefully without crashing the program.

# ---------------------------------------------
# Basic try-except block:

try:
    # Code that might cause an error
    result = 10 / 0  # Division by zero error!
except ZeroDivisionError:
    # Code to run if the above error occurs
    print("Error: Cannot divide by zero!")

# How it works:
# - Python tries to run code inside 'try'.
# - If a ZeroDivisionError occurs, the code inside 'except' runs instead of crashing.
# - This prevents the program from stopping abruptly.

# ---------------------------------------------
# Catching multiple exceptions:

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: That was not a valid number!")

# How it works:
# - The 'try' block runs code that might raise multiple types of errors.
# - Different 'except' blocks handle specific error types separately.

# ---------------------------------------------
# Using else and finally blocks:

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: That was not a valid number!")
else:
    print(f"Success! Result is {result}")
finally:
    print("This runs no matter what, cleanup code goes here.")

# How it works:
# - 'else' runs if no exceptions were raised in try.
# - 'finally' always runs, even if an error happened or not.

# ---------------------------------------------
# Raising your own exceptions:

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    else:
        print(f"Your age is {age}")

try:
    check_age(-5)
except ValueError as e:
    print(f"Caught an error: {e}")

# How it works:
# - You can use 'raise' to create an exception intentionally.
# - It can be caught later with try-except.

# ---------------------------------------------------
# Summary:
# - Exception handling keeps programs from crashing.
# - Use try-except blocks to catch errors.
# - else runs if no error, finally runs always.
# - You can raise custom exceptions to handle specific cases.

# ---------------------------------------------------
# Practice Ideas:
# 1. Write code that handles division by zero and invalid input.
# 2. Create a function that raises an exception for invalid temperature values.
# 3. Use finally to close a file even if an error happens.
