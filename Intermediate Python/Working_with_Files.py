# ---------------------------------------------
# Working with Files
# ---------------------------------------------

# 🤔 What is File Handling?
# File handling means reading data from and writing data to files stored on your computer.
# Files can be text files (.txt), CSV, JSON, or any other format.
# Python provides simple built-in functions to open, read, write, and close files.

# ---------------------------------------------
# Opening a File

# The open() function opens a file and returns a file object.
# Syntax: open(filename, mode)
# Modes:
# 'r' = read (default) - opens file for reading
# 'w' = write - opens file for writing (overwrites existing content)
# 'a' = append - opens file to add new content at the end
# 'x' = create - creates a new file, fails if file exists

# ---------------------------------------------
# Example 1: Writing to a file

# Open a file named "example.txt" in write mode ('w').
file = open("example.txt", "w")

# Write some text into the file
file.write("Hello, this is the first line.\n")
file.write("Here is another line.")

# Close the file to save changes and free resources
file.close()

# How it works:
# - open() creates the file if it doesn't exist or clears it if it exists (in write mode).
# - write() adds text to the file.
# - close() saves and closes the file (always important).

# ---------------------------------------------
# Example 2: Reading from a file

# Open the file in read mode ('r')
file = open("example.txt", "r")

# Read the entire content of the file
content = file.read()

# Print the content
print("File Content:")
print(content)

# Close the file
file.close()

# How it works:
# - open() opens the file.
# - read() reads all text at once.
# - print() displays it.
# - close() closes the file.

# ---------------------------------------------
# Example 3: Reading line by line

file = open("example.txt", "r")

# Read file line by line using a loop
print("Reading line by line:")
for line in file:
    print(line.strip())  # strip() removes extra newlines and spaces

file.close()

# ---------------------------------------------
# Example 4: Using 'with' statement (Best Practice)

# Using 'with' automatically closes the file, even if errors happen.
with open("example.txt", "a") as file:
    file.write("\nThis line is appended using 'with'.")

# 'a' mode appends to the file without deleting existing content.

# ---------------------------------------------
# Summary:
# - Always open files with a mode ('r', 'w', 'a').
# - Use file.write() to add text.
# - Use file.read() or loop to read text.
# - Close files using file.close() or use 'with' for automatic handling.
# - 'with' statement is recommended for safe file handling.

# ---------------------------------------------
# Practice Ideas:
# 1. Create a program to write user input to a file.
# 2. Read from a file and count the number of lines.
# 3. Append new lines to a file without deleting old content.

