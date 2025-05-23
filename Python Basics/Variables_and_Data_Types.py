# ---------------------------------------------
# 📊 2. Data Types in Python
# ---------------------------------------------

# 🤔 What are Data Types?
# Data types tell Python what kind of value a variable holds.
# Different types help Python understand how to store and use data.

# Common data types in Python include:
# - int (integer): whole numbers like 1, 100, -5
# - float (floating point): decimal numbers like 3.14, -0.001
# - str (string): text like "Hello", "Python123"
# - bool (boolean): True or False values
# - list: a collection of items like [1, 2, 3]
# - tuple: an ordered, unchangeable collection like (1, 2, 3)
# - dict (dictionary): key-value pairs like {"name": "Alice", "age": 25}

# ---------------------------------------------
# 🧮 Integer (int)
x = 10
print("Integer value x:", x)
print("Type of x is:", type(x))  # type() tells us the data type of a variable

# Integers represent whole numbers without decimals

# ---------------------------------------------
# 🧮 Float (decimal numbers)
pi = 3.14159
print("Float value pi:", pi)
print("Type of pi is:", type(pi))

# Floats are used when we need numbers with decimals

# ---------------------------------------------
# ✨ String (str)
name = "Alice"
print("String value name:", name)
print("Type of name is:", type(name))

# Strings are text values and must be enclosed in quotes (single or double)

# ---------------------------------------------
# 🔘 Boolean (bool)
is_student = True
has_passed = False
print("Boolean value is_student:", is_student)
print("Boolean value has_passed:", has_passed)
print("Type of is_student is:", type(is_student))

# Booleans represent True or False values, useful for conditions

# ---------------------------------------------
# 📋 List
fruits = ["apple", "banana", "cherry"]
print("List fruits:", fruits)
print("Type of fruits is:", type(fruits))

# Lists store multiple items in an ordered collection, can be changed (mutable)

# Access list items by index (starting at 0)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# ---------------------------------------------
# 🔒 Tuple
coordinates = (10.0, 20.0)
print("Tuple coordinates:", coordinates)
print("Type of coordinates is:", type(coordinates))

# Tuples are like lists but cannot be changed (immutable)

# ---------------------------------------------
# 🗂️ Dictionary (dict)
person = {"name": "Bob", "age": 30, "city": "New York"}
print("Dictionary person:", person)
print("Type of person is:", type(person))

# Dictionaries store key-value pairs
# Access values by keys
print("Person's name:", person["name"])
print("Person's age:", person["age"])

# ---------------------------------------------
# 🧠 Summary:
# - Use int for whole numbers
# - Use float for decimal numbers
# - Use str for text
# - Use bool for True/False
# - Use list for ordered, changeable collections
# - Use tuple for ordered, unchangeable collections
# - Use dict for key-value pairs

# ---------------------------------------------
# 🧪 Practice:
# Create variables with each data type
# Print their values and types to see the output
