# ---------------------------------------------
# 📌 4. Conditional Statements in Python
# ---------------------------------------------

# 🧠 What are Conditional Statements?
# These are used to make decisions in your code.
# Python checks conditions using `if`, `elif`, and `else`.

# 🔸 Syntax:
# if condition:
#     code block
# elif another_condition:
#     code block
# else:
#     code block

# ---------------------------------------------
# ✅ Example 1: Basic if statement
age = 18

if age >= 18:
    print("You are eligible to vote.")  # This will print

# Explanation: Since age is 18, the condition (age >= 18) is True.

# ---------------------------------------------
# ✅ Example 2: if-else statement
marks = 55

if marks >= 50:
    print("You passed the exam!")
else:
    print("You failed the exam.")

# Explanation: If the condition is True, the first block runs;
# otherwise, the code under else runs.

# ---------------------------------------------
# ✅ Example 3: if-elif-else (Multiple Conditions)
temperature = 35

if temperature > 40:
    print("It's too hot!")
elif temperature > 30:
    print("It's warm.")
elif temperature > 20:
    print("It's pleasant.")
else:
    print("It's cold!")

# Explanation:
# Python checks from top to bottom.
# As soon as one condition is True, it stops checking the rest.

# ---------------------------------------------
# ✅ Example 4: Nested if (if inside another if)
has_ID = True
age = 22

if has_ID:
    if age >= 18:
        print("Access granted.")
    else:
        print("You are underage.")
else:
    print("No ID. Access denied.")

# Explanation:
# This structure allows more detailed decision trees.

# ---------------------------------------------
# ✅ Example 5: Short Hand If-Else (One Line)
a = 10
b = 20

# Print the greater value using one line if-else
print("A is greater") if a > b else print("B is greater")

# ---------------------------------------------
# 🧠 Summary:
# - Use `if` to check a condition.
# - Add `elif` for extra conditions.
# - Use `else` when no condition matches.
# - You can nest if statements inside each other.
# - You can use short-hand if-else for simple conditions.

# Practice Tip:
# Try writing a simple grade-checker or weather app using conditionals!
