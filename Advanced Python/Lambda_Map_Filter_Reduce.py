# ---------------------------------------------
# Lambda, Map, Filter, Reduce
# ---------------------------------------------

# 🚀 What is a Lambda Function?
# A lambda function is a small anonymous function — it has no name.
# It can take any number of arguments but only one expression.
# Useful for quick, simple functions without formally defining them with 'def'.

# ---------------------------------------------
# Example 1: Lambda Function

# Traditional function to add 10 to a number
def add_ten(x):
    return x + 10

print(add_ten(5))  # Output: 15

# Same function using lambda
add_ten_lambda = lambda x: x + 10
print(add_ten_lambda(5))  # Output: 15

# How it works:
# - The lambda creates a function that takes x and returns x + 10.
# - It’s shorter and useful for simple, one-line functions.

# ---------------------------------------------
# 🚀 What is Map?
# The map() function applies a given function to each item of an iterable (like a list) and returns a map object (an iterator).
# Useful when you want to transform all items in a list without writing loops.

# ---------------------------------------------
# Example 2: Using map() with lambda

numbers = [1, 2, 3, 4, 5]

# Multiply each number by 2 using map and lambda
doubled = map(lambda x: x * 2, numbers)

print(list(doubled))  # Output: [2, 4, 6, 8, 10]

# How it works:
# - map() takes the lambda function and applies it to each number.
# - Returns an iterator, so we convert it to list to print all values.

# ---------------------------------------------
# 🚀 What is Filter?
# The filter() function creates an iterator from elements of an iterable for which a function returns True.
# Useful for selecting items from a list based on a condition.

# ---------------------------------------------
# Example 3: Using filter() with lambda

numbers = [1, 2, 3, 4, 5, 6]

# Filter out only even numbers
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))  # Output: [2, 4, 6]

# How it works:
# - filter() runs the lambda on each number.
# - If lambda returns True (number is even), the item is included in the result.

# ---------------------------------------------
# 🚀 What is Reduce?
# The reduce() function applies a rolling computation to sequential pairs of values in an iterable.
# It is part of the functools module.
# Useful for accumulating or combining all items into a single value.

from functools import reduce

# ---------------------------------------------
# Example 4: Using reduce() with lambda

numbers = [1, 2, 3, 4, 5]

# Sum all numbers using reduce
sum_all = reduce(lambda x, y: x + y, numbers)

print(sum_all)  # Output: 15

# How it works:
# - reduce takes the first two numbers (1, 2), adds them to get 3.
# - Then adds 3 (result) to next number (3), total 6.
# - Continues until all numbers are added into a single sum.

# ---------------------------------------------
# Summary:
# - Lambda: quick, unnamed function for simple operations.
# - Map: apply a function to every item in a list/iterable.
# - Filter: select items from a list/iterable that satisfy a condition.
# - Reduce: combine all items in a list/iterable into one result using a rolling function.

# ---------------------------------------------
# Practice Ideas:
# 1. Write a lambda to cube a number.
# 2. Use map() to convert a list of temperatures from Celsius to Fahrenheit.
# 3. Use filter() to get all words longer than 4 letters from a list.
# 4. Use reduce() to find the product of all numbers in a list.

