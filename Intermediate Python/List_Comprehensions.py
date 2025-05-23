# ---------------------------------------------------
# List Comprehensions
# ---------------------------------------------------

# 🤔 What is a List Comprehension?
# A concise way to create lists by applying an expression to each item in an iterable (like a list or range),
# optionally filtering items with a condition.

# ---------------------------------------------
# Basic Example:
numbers = [1, 2, 3, 4, 5]

# Using a for loop to create a list of squares
squares = []
for n in numbers:
    squares.append(n ** 2)
print("Squares using for loop:", squares)

# Using list comprehension to do the same thing in one line
squares_lc = [n ** 2 for n in numbers]
print("Squares using list comprehension:", squares_lc)

# How it works:
# - 'n ** 2' is the expression applied to each item 'n' in 'numbers'.
# - The result is a new list containing these squared values.

# ---------------------------------------------
# Adding a Condition (Filtering):
# Create a list of even numbers only

even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)

# How it works:
# - 'if n % 2 == 0' filters only numbers divisible by 2 (even).
# - The list comprehension only includes these filtered items.

# ---------------------------------------------
# Using List Comprehensions with Strings:
words = ["apple", "banana", "cherry"]

# Create a list of uppercase words
uppercase_words = [word.upper() for word in words]
print("Uppercase words:", uppercase_words)

# How it works:
# - Calls the .upper() method on each word in the list.
# - Collects results into a new list.

# ---------------------------------------------
# Nested Loops in List Comprehension:
# Example: Create pairs (i, j) where i and j range from 1 to 3

pairs = [(i, j) for i in range(1, 4) for j in range(1, 4)]
print("Pairs:", pairs)

# How it works:
# - Two for loops are combined inside the comprehension.
# - For each i in 1 to 3, iterate j in 1 to 3, forming tuples.

# ---------------------------------------------
# More Complex Example:
# Extract vowels from a string

text = "Hello, World!"
vowels = [char for char in text if char.lower() in "aeiou"]
print("Vowels in text:", vowels)

# How it works:
# - Iterates through each character in 'text'.
# - Includes character only if it is a vowel (case insensitive).

# ---------------------------------------------------
# Summary:
# - List comprehensions create new lists in a concise, readable way.
# - You can apply expressions and filter conditions.
# - They often replace loops for cleaner code.

# ---------------------------------------------------
# Practice Ideas:
# 1. Create a list of cubes of numbers 1 to 10.
# 2. Create a list of odd numbers from 1 to 20.
# 3. Extract all uppercase letters from a sentence.
# 4. Make a list of lengths of each word in a list.
# 5. Create a list of tuples (number, square) for numbers 1 to 5.
