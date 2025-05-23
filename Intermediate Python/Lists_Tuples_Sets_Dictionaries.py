# ---------------------------------------------------
# Lists, Tuples, Sets, Dictionaries
# ---------------------------------------------------

# 🤔 What are Collections in Python?
# Collections are data structures that hold multiple items together.
# They help organize and store data efficiently.

# ---------------------------------------------
# 1. Lists
# Lists are ordered, changeable (mutable) collections of items.
# They allow duplicate items and support indexing and slicing.

# Example:
fruits = ["apple", "banana", "cherry", "banana"]
print("List of fruits:", fruits)

# How it works:
# - Items are stored in order (index 0,1,2...)
# - You can access items by their index
print("First fruit:", fruits[0])  # apple

# - You can change an item by assigning a new value
fruits[1] = "blueberry"
print("Changed list:", fruits)

# - Add an item using append()
fruits.append("orange")
print("After adding orange:", fruits)

# - Remove an item by value using remove()
fruits.remove("banana")  # removes the first occurrence
print("After removing banana:", fruits)

# ---------------------------------------------
# 2. Tuples
# Tuples are ordered, unchangeable (immutable) collections.
# They are like lists but you cannot change their items after creation.

# Example:
coordinates = (10, 20)
print("Tuple coordinates:", coordinates)

# How it works:
# - Items stored in order and accessible by index
print("X coordinate:", coordinates[0])  # 10

# - Trying to change an item will cause an error:
# coordinates[0] = 15  # Uncommenting this line will raise TypeError

# ---------------------------------------------
# 3. Sets
# Sets are unordered collections of unique items.
# They automatically remove duplicates and do not support indexing.

# Example:
numbers = {1, 2, 3, 2, 1}
print("Set of numbers (duplicates removed):", numbers)

# How it works:
# - Unordered: no index positions
# - Unique items only (duplicates removed)
# - You can add items with add()
numbers.add(4)
print("After adding 4:", numbers)

# - You can remove items with remove()
numbers.remove(2)
print("After removing 2:", numbers)

# ---------------------------------------------
# 4. Dictionaries
# Dictionaries store key-value pairs.
# Keys are unique and used to access their corresponding values.

# Example:
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print("Dictionary person:", person)

# How it works:
# - Access values by their key
print("Name:", person["name"])  # Alice

# - Change values by key
person["age"] = 31
print("After birthday:", person)

# - Add new key-value pairs
person["job"] = "Engineer"
print("After adding job:", person)

# - Remove key-value pairs with del
del person["city"]
print("After removing city:", person)

# - Loop through dictionary items
for key, value in person.items():
    print(f"{key}: {value}")

# ---------------------------------------------------
# Summary:
# - List: ordered, changeable, allows duplicates, indexed
# - Tuple: ordered, unchangeable, indexed
# - Set: unordered, unique items, no indexing
# - Dictionary: key-value pairs, keys unique

# ---------------------------------------------------
# Practice Ideas:
# 1. Create a list of your favorite colors and print the second color.
# 2. Create a tuple with your birth year, month, and day.
# 3. Create a set with some repeated numbers and print it.
# 4. Create a dictionary with your name, age, and hobby. Loop and print all key-value pairs.
