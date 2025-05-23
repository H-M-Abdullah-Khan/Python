# ---------------------------------------------
# ⚙️ 3. Operators in Python
# ---------------------------------------------

# 🤔 What are Operators?
# Operators are special symbols used to perform operations on variables and values.
# Example: +, -, *, /, ==, >, etc.

# Python has different types of operators:
# 1. Arithmetic Operators
# 2. Comparison Operators
# 3. Assignment Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership Operators

# ---------------------------------------------
# 1️⃣ Arithmetic Operators
# Used for basic math operations.

# ➕ Addition
a = 10
b = 5
print("Addition:", a + b)  # 15

# ➖ Subtraction
print("Subtraction:", a - b)  # 5

# ✖️ Multiplication
print("Multiplication:", a * b)  # 50

# ➗ Division
print("Division:", a / b)  # 2.0

# 🟰 Modulus (Remainder)
print("Modulus:", a % b)  # 0

# 🟰 Exponentiation (Power)
print("Exponentiation:", a ** 2)  # 100

# ➗ Floor Division (No decimal)
print("Floor Division:", a // b)  # 2

# ---------------------------------------------
# 2️⃣ Comparison Operators
# Used to compare two values. Returns True or False.

x = 10
y = 20

print("Is x equal to y?", x == y)        # False
print("Is x not equal to y?", x != y)    # True
print("Is x greater than y?", x > y)     # False
print("Is x less than y?", x < y)        # True
print("Is x >= 10?", x >= 10)            # True
print("Is y <= 15?", y <= 15)            # False

# ---------------------------------------------
# 3️⃣ Assignment Operators
# Used to assign values to variables.

z = 5           # Basic assignment
z += 2          # z = z + 2 => 7
z *= 3          # z = z * 3 => 21
print("Final value of z:", z)

# You can also use -=, /=, %=, **=, //=

# ---------------------------------------------
# 4️⃣ Logical Operators
# Used to combine conditional statements.

is_sunny = True
has_umbrella = False

print("Go outside?", is_sunny and not has_umbrella)  # True
print("Need umbrella?", not is_sunny or has_umbrella)  # False

# 'and': True only if both are True
# 'or': True if at least one is True
# 'not': Reverses the result

# ---------------------------------------------
# 5️⃣ Identity Operators
# Used to compare if two variables are the same object in memory.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)       # True (same memory)
print("a is c:", a is c)       # False (same content, different memory)
print("a is not c:", a is not c)  # True

# ---------------------------------------------
# 6️⃣ Membership Operators
# Used to check if a value is in a sequence.

colors = ["red", "green", "blue"]

print("Is 'green' in colors?", "green" in colors)  # True
print("Is 'yellow' not in colors?", "yellow" not in colors)  # True

# ---------------------------------------------
# 🧠 Summary:
# - Use arithmetic operators for math
# - Comparison operators return True/False
# - Assignment operators update variable values
# - Logical operators connect conditions
# - Identity checks memory address
# - Membership checks elements in sequences

# 🧪 Practice:
# Try writing your own expressions using each type of operator!

