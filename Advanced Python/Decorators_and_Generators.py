# ---------------------------------------------
# Decorators & Generators
# ---------------------------------------------

# 🚀 What are Decorators?
# Decorators are special functions that modify or enhance other functions without changing their code.
# They "wrap" another function to extend its behavior in a clean and reusable way.
# Think of a decorator as a wrapper around a gift — it adds something extra to the original function.

# ---------------------------------------------
# Example 1: Simple Decorator

def decorator_function(original_function):
    def wrapper_function():
        print("Before the original function runs")
        original_function()  # Call the original function
        print("After the original function runs")
    return wrapper_function  # Return the wrapped function

# Using the decorator on a function
@decorator_function
def say_hello():
    print("Hello!")

say_hello()

# How it works:
# - The decorator_function takes say_hello as input.
# - It defines wrapper_function that adds behavior before and after calling say_hello.
# - The @decorator_function syntax applies the decorator to say_hello.
# - When you call say_hello(), you actually call wrapper_function with extra steps.

# ---------------------------------------------
# Example 2: Decorator with Arguments

def decorator_with_args(func):
    def wrapper(name):
        print(f"Hello, {name}! Before the function call.")
        func(name)
        print(f"Goodbye, {name}! After the function call.")
    return wrapper

@decorator_with_args
def greet(name):
    print(f"Greeting {name}")

greet("Alice")

# How it works:
# - The wrapper function takes an argument and passes it to the original function.
# - Decorator adds print statements before and after calling greet().

# ---------------------------------------------
# 🚀 What are Generators?
# Generators are functions that return an iterator that yields items one at a time, saving memory.
# Instead of returning all values at once, they produce values on the fly using the `yield` keyword.
# Useful for processing large datasets or streams where you don’t want to hold everything in memory.

# ---------------------------------------------
# Example 3: Simple Generator

def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Yield value and pause function here
        count += 1

# Using the generator
counter = count_up_to(5)

print("Generator output:")
for number in counter:
    print(number)

# How it works:
# - The function uses 'yield' to return one number at a time.
# - Each time 'yield' is called, the function pauses, and next() resumes it.
# - This saves memory because values are generated only when needed.

# ---------------------------------------------
# Example 4: Generator Expression

# Similar to list comprehensions but returns a generator object
squares = (x * x for x in range(1, 6))

print("Squares using generator expression:")
for square in squares:
    print(square)

# How it works:
# - The expression inside parentheses creates a generator.
# - It produces squares from 1 to 5 one by one.

# ---------------------------------------------
# Summary:
# - Decorators add functionality to existing functions in a clean, reusable way.
# - Use @decorator_name syntax to apply decorators.
# - Generators use 'yield' to produce values one at a time, great for saving memory.
# - Generator expressions are compact syntax for creating generators.

# ---------------------------------------------
# Practice Ideas:
# 1. Write a decorator that logs function execution time.
# 2. Create a generator that yields even numbers up to a limit.
# 3. Write a generator expression to generate cube numbers from 1 to 10.

