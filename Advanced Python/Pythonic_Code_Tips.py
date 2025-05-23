# ---------------------------------------------
# Pythonic Code Tips
# ---------------------------------------------

# 🚀 What is "Pythonic" code?
# Pythonic code means writing Python code in a clean, readable, and efficient way,
# following Python’s best practices and idioms.
# It focuses on simplicity, clarity, and using Python’s built-in features effectively.

# ---------------------------------------------
# Example 1: Using list comprehension instead of a for-loop to create a list

# Non-Pythonic way (more verbose):
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print("Squares (non-Pythonic):", squares)

# Pythonic way (short and clear):
squares_pythonic = [n ** 2 for n in numbers]
print("Squares (Pythonic):", squares_pythonic)

# How it works:
# - List comprehension creates a new list by applying an expression to each item.
# - It’s more readable and concise than using a for-loop with append().

# ---------------------------------------------
# Example 2: Using multiple assignment (tuple unpacking)

# Non-Pythonic way:
x = 5
y = 10
temp = x
x = y
y = temp
print("x:", x, "y:", y)

# Pythonic way (swap values easily):
x, y = 5, 10
x, y = y, x
print("x:", x, "y:", y)

# How it works:
# - Python lets you swap variables in a single line without a temporary variable.
# - This is clean and less error-prone.

# ---------------------------------------------
# Example 3: Using `any()` and `all()` for checking conditions

numbers = [1, 3, 5, 7, 9]

# Check if any number is even (non-Pythonic):
found_even = False
for num in numbers:
    if num % 2 == 0:
        found_even = True
        break
print("Any even numbers? (non-Pythonic):", found_even)

# Pythonic way with any():
found_even_pythonic = any(num % 2 == 0 for num in numbers)
print("Any even numbers? (Pythonic):", found_even_pythonic)

# How it works:
# - `any()` returns True if at least one condition is True.
# - `all()` returns True only if all conditions are True.
# - Using them makes your code clearer and shorter.

# ---------------------------------------------
# Example 4: Using enumerate() instead of manual index counting

fruits = ['apple', 'banana', 'cherry']

# Non-Pythonic way:
index = 0
for fruit in fruits:
    print(index, fruit)
    index += 1

# Pythonic way with enumerate():
for index, fruit in enumerate(fruits):
    print(index, fruit)

# How it works:
# - enumerate() adds a counter to an iterable and returns it as pairs (index, value).
# - This avoids manual index tracking and is cleaner.

# ---------------------------------------------
# Summary:
# - Pythonic code emphasizes readability and simplicity.
# - Use Python’s built-in functions and idioms like list comprehensions, tuple unpacking, any/all, and enumerate.
# - Writing Pythonic code makes your programs easier to read, maintain, and less error-prone.

# ---------------------------------------------
# Practice Ideas:
# 1. Rewrite some of your older code using Pythonic idioms.
# 2. Use list comprehensions to filter and transform data.
# 3. Use any() and all() in real conditional checks.
