# ---------------------------------------------
# Context Managers
# ---------------------------------------------

# 🚀 What are Context Managers?
# Context Managers help you manage resources like files, network connections, or locks.
# They ensure that resources are properly acquired and released, even if errors happen.
# The most common example is opening and closing files safely.

# The 'with' statement is used to work with context managers in Python.

# ---------------------------------------------
# Example 1: Using a Context Manager to open a file

# This code opens a file, writes some text, and automatically closes it after.
with open('example.txt', 'w') as file:
    file.write("Hello, this file is managed by a context manager!\n")

# How it works:
# - 'open' creates a file object.
# - 'with' ensures the file is automatically closed when the block ends.
# - 'file' is the variable representing the file inside the block.
# - You don't have to call file.close() manually; it's done automatically.

# ---------------------------------------------
# Example 2: Custom Context Manager using a class

class MyContextManager:
    def __enter__(self):
        print("Entering the context (setup).")
        # Setup actions go here
        return self  # Return any object you want to use in the block

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context (cleanup).")
        # Cleanup actions go here
        # exc_type, exc_value, traceback help handle exceptions if needed
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        # Return True to suppress exception, False to propagate it
        return False

# Using the custom context manager
with MyContextManager() as manager:
    print("Inside the with block.")
    # Uncomment below to test exception handling inside context
    # raise ValueError("Oops! Something went wrong.")

# How it works:
# - __enter__() runs at the start of the 'with' block.
# - __exit__() runs when the block ends, even if an error occurs.
# - If an exception occurs, __exit__ receives details about it.
# - You can handle exceptions or let them propagate.

# ---------------------------------------------
# Example 3: Context Manager with 'contextlib' module

from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    print("Opening the file.")
    f = open(file_name, mode)
    try:
        yield f  # This is where the 'with' block code runs
    finally:
        print("Closing the file.")
        f.close()

with open_file('example2.txt', 'w') as f:
    f.write("Writing to file using a custom context manager!\n")

# How it works:
# - @contextmanager decorator helps you create context managers easily.
# - Code before 'yield' runs on entering the block.
# - Code after 'yield' runs when exiting the block (cleanup).
# - 'yield' temporarily hands control back to the block inside 'with'.

# ---------------------------------------------
# Summary:
# - Context managers manage setup and cleanup of resources automatically.
# - Use 'with' statement for safer, cleaner code.
# - You can write your own context managers by defining __enter__ and __exit__ methods or using @contextmanager decorator.

# ---------------------------------------------
# Practice Ideas:
# 1. Write a context manager that times how long a block of code takes to run.
# 2. Create a context manager that temporarily changes the working directory.
# 3. Use a context manager to handle database connections safely.
