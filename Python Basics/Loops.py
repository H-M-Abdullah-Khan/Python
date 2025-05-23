# ---------------------------------------------
# 📌 5. Loops in Python (for and while)
# ---------------------------------------------

# 🧠 What are Loops?
# Loops are used to repeat a block of code multiple times.

# Python has two main types of loops:
# - for loop
# - while loop

# ---------------------------------------------
# 🔸 for Loop
# Used to iterate over a sequence (like list, tuple, string, etc.)

# ✅ Example 1: Print numbers from 1 to 5 using a for loop
for i in range(1, 6):  # range(1, 6) gives numbers from 1 to 5
    print("Number:", i)

# Explanation:
# i takes values from 1 to 5, one at a time, and prints them.

# ---------------------------------------------
# ✅ Example 2: Loop through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)

# Explanation:
# fruit takes each item from the list one by one.

# ---------------------------------------------
# 🔸 while Loop
# Runs a block of code as long as a condition is True.

# ✅ Example 3: Print numbers from 1 to 5 using a while loop
count = 1

while count <= 5:
    print("Count is:", count)
    count += 1  # Increment count to avoid infinite loop

# Explanation:
# The loop continues while count is less than or equal to 5.

# ---------------------------------------------
# 🔸 break Statement
# Used to exit the loop early if a condition is met.

# ✅ Example 4: Stop loop when number reaches 3
for i in range(1, 6):
    if i == 3:
        print("Stopping at", i)
        break  # Exit the loop
    print("i =", i)

# ---------------------------------------------
# 🔸 continue Statement
# Skips the current iteration and moves to the next one.

# ✅ Example 5: Skip number 3
for i in range(1, 6):
    if i == 3:
        print("Skipping", i)
        continue  # Skip the rest of the code for this loop
    print("i =", i)

# ---------------------------------------------
# 🔸 else with Loops
# The `else` block runs after the loop ends **only if** it wasn’t stopped by a `break`.

# ✅ Example 6: Loop completed successfully
for i in range(1, 4):
    print("i =", i)
else:
    print("Loop completed without break.")

# ✅ Example 7: Loop with break
for i in range(1, 4):
    if i == 2:
        break
    print("i =", i)
else:
    print("This will not print because loop broke.")

# ---------------------------------------------
# 🧠 Summary:
# - Use `for` when you know the number of iterations.
# - Use `while` when you want to loop until a condition becomes False.
# - Use `break` to stop a loop early.
# - Use `continue` to skip the current iteration.
# - Use `else` with loops to execute code only if the loop wasn't broken.

# Practice Idea:
# Try building a number guessing game using loops!
