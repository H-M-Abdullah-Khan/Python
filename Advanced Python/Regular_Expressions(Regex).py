# ---------------------------------------------
# Regular Expressions (Regex)
# ---------------------------------------------

# 🚀 What are Regular Expressions?
# Regular Expressions (Regex) are special patterns used to find, match, or manipulate text.
# They allow you to search for specific strings, validate formats (like emails), extract parts of text, and much more.
# In Python, regex functionality is provided by the 're' module.

import re  # Import the regex module

# ---------------------------------------------
# Example 1: Simple Search with regex

text = "Hello, my phone number is 123-456-7890."

# Pattern to find phone numbers in the format xxx-xxx-xxxx
pattern = r'\d{3}-\d{3}-\d{4}'

# re.search() finds the first match of the pattern in the text
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No phone number found.")

# How it works:
# - \d means digit (0-9)
# - {3} means exactly 3 digits
# - So pattern looks for 3 digits, a dash, 3 digits, a dash, and 4 digits
# - re.search() scans the string and returns the first matching text if found.

# ---------------------------------------------
# Example 2: Find all matches

text = "Call me at 123-456-7890 or at 987-654-3210."

# re.findall() returns all non-overlapping matches as a list
matches = re.findall(pattern, text)
print("Phone numbers found:", matches)

# How it works:
# - re.findall() finds all matches of the pattern and returns them in a list.

# ---------------------------------------------
# Example 3: Validate email format

email = "example.user@gmail.com"

# Regex pattern for a simple email validation
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

if re.match(email_pattern, email):
    print("Valid email address.")
else:
    print("Invalid email address.")

# How it works:
# - ^ means start of string, $ means end of string
# - [a-zA-Z0-9_.+-]+ means one or more allowed characters before @
# - @ is literal '@' symbol
# - After '@' we expect domain name and domain extension separated by dot '.'

# ---------------------------------------------
# Example 4: Replace text using regex

text = "I love cats. Cats are great!"

# Replace 'cats' (case-insensitive) with 'dogs'
new_text = re.sub(r'cats', 'dogs', text, flags=re.IGNORECASE)

print(new_text)  # Output: I love dogs. Dogs are great!

# How it works:
# - re.sub() replaces all matches of pattern with replacement text.
# - flags=re.IGNORECASE makes the search case-insensitive.

# ---------------------------------------------
# Summary:
# - Regex helps find, validate, and manipulate text with patterns.
# - Use 're' module functions: search(), findall(), match(), sub(), etc.
# - Patterns consist of special characters like \d (digits), ^ (start), $ (end), [] (character sets), + (one or more), etc.

# ---------------------------------------------
# Practice Ideas:
# 1. Write a regex to find all dates in format dd/mm/yyyy in a text.
# 2. Use regex to extract hashtags (#example) from a tweet.
# 3. Validate a password with at least 8 characters, one uppercase, one digit.
