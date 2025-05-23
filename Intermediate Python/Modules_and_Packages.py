# ---------------------------------------------------
# Modules and Packages
# ---------------------------------------------------

# 🤔 What are Modules and Packages?
# - A **Module** is a file containing Python code (functions, classes, variables) that you can reuse in other programs.
# - A **Package** is a folder containing multiple modules, organized with a special file (__init__.py) to group related modules together.

# Why use them?
# - To organize your code better.
# - To reuse code without rewriting it.
# - To share functionality across different projects.

# ---------------------------------------------
# Creating and using a module:

# Suppose you have a file named math_helpers.py with this content:
# (This is your module)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# ---------------------------------------------
# Using the module in another Python file:

# Import the module
import math_helpers

result1 = math_helpers.add(5, 3)
result2 = math_helpers.subtract(10, 7)

print("Addition Result:", result1)
print("Subtraction Result:", result2)

# How it works:
# - The 'import' keyword loads the math_helpers module.
# - You access the functions using 'math_helpers.function_name()'.
# - This helps keep your code clean and modular.

# ---------------------------------------------
# Importing specific functions:

from math_helpers import add

result = add(20, 30)
print("Addition with specific import:", result)

# How it works:
# - You can import only the functions or variables you need.
# - This avoids loading everything and can make code easier to read.

# ---------------------------------------------
# Using aliases:

import math_helpers as mh

result = mh.subtract(15, 5)
print("Subtraction using alias:", result)

# How it works:
# - 'as' lets you give a shorter or different name to the module for convenience.

# ---------------------------------------------
# What is a package?

# A package is a folder with modules and a file named __init__.py inside it.
# Example folder structure:
# mypackage/
#   __init__.py
#   module1.py
#   module2.py

# You can import modules from packages like this:
# import mypackage.module1

# ---------------------------------------------
# Using modules inside packages:

# import mypackage.module1
# result = mypackage.module1.some_function()

# ---------------------------------------------
# Summary:
# - Modules help break code into reusable files.
# - Packages organize modules into folders.
# - Import modules using 'import' or 'from ... import ...'.
# - Use aliases to shorten module names.

# ---------------------------------------------
# Practice Ideas:
# 1. Create your own module with math functions and import it.
# 2. Organize multiple modules into a package.
# 3. Experiment with different import styles.

