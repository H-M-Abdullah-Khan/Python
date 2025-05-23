# ---------------------------------------------------
# String Manipulation
# ---------------------------------------------------

# 🤔 What is a String?
# A string is a sequence of characters enclosed in quotes.
# Strings are used to store text data.

# ---------------------------------------------
# Creating Strings:
greeting = "Hello, World!"
print("Greeting:", greeting)

# How it works:
# - Text inside quotes is stored as a string.
# - You can use single (' '), double (" "), or triple (''' ''') quotes.

# ---------------------------------------------
# Accessing Characters:
first_char = greeting[0]
print("First character:", first_char)  # H

# How it works:
# - Strings are indexed like lists starting at 0.
# - You can access individual characters by their index.

# ---------------------------------------------
# Slicing Strings:
part = greeting[0:5]
print("First 5 characters:", part)  # Hello

# How it works:
# - Slicing extracts a substring.
# - [start:end] extracts characters from 'start' index up to but not including 'end' index.

# ---------------------------------------------
# String Methods (functions to manipulate strings):

# 1. Lowercase and Uppercase
print("Lowercase:", greeting.lower())
print("Uppercase:", greeting.upper())

# How it works:
# - .lower() returns the string in all lowercase letters.
# - .upper() returns the string in all uppercase letters.

# 2. Strip (remove whitespace)
text = "   Python   "
print("Original text:", repr(text))  # Shows spaces
print("Stripped text:", repr(text.strip()))  # Removes spaces from both ends

# How it works:
# - .strip() removes leading and trailing spaces.

# 3. Replace
new_text = greeting.replace("World", "Python")
print("Replaced text:", new_text)

# How it works:
# - .replace(old, new) replaces occurrences of 'old' with 'new'.

# 4. Split
words = greeting.split(",")
print("Split by comma:", words)

# How it works:
# - .split(separator) splits the string into a list where each part is separated by the given character.

# 5. Join
joined = " ".join(words)
print("Joined with space:", joined)

# How it works:
# - "separator".join(list) joins list elements into one string separated by the specified separator.

# ---------------------------------------------
# String Formatting:
name = "Alice"
age = 25

# Old style
print("Name: %s, Age: %d" % (name, age))

# New style using format()
print("Name: {}, Age: {}".format(name, age))

# f-string (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# How it works:
# - These allow inserting variables inside strings in different ways.
# - f-string is the most readable and modern method.

# ---------------------------------------------------
# Summary:
# - Strings are text data in quotes.
# - You can access, slice, and manipulate strings with built-in methods.
# - Formatting helps combine strings with variables easily.

# ---------------------------------------------------
# Practice Ideas:
# 1. Create a string with your full name.
# 2. Extract and print your first name using slicing.
# 3. Convert your name to uppercase and print.
# 4. Replace a word in a sentence and print the new sentence.
# 5. Format a sentence with your age and city using f-string.
