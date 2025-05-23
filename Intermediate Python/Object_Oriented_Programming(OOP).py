# ---------------------------------------------------
# Object-Oriented Programming (OOP)
# ---------------------------------------------------

# 🤔 What is OOP?
# Object-Oriented Programming is a way to organize code by creating "objects" that
# represent real-world things or concepts. Each object can have:
# - Attributes (data or properties)
# - Methods (functions/actions the object can do)

# OOP helps make code more modular, reusable, and easier to maintain.

# ---------------------------------------------
# Defining a Class and Creating Objects:

# A class is like a blueprint for creating objects.
class Car:
    # The __init__ method is called a constructor.
    # It runs automatically when you create an object.
    def __init__(self, brand, model, year):
        # These are attributes of the Car object.
        self.brand = brand
        self.model = model
        self.year = year

    # Method: A function that belongs to the class
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

    # Method to simulate starting the car
    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine has started.")

# ---------------------------------------------
# Creating objects (instances) of the Car class:

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

# ---------------------------------------------
# Using object methods:

car1.display_info()       # Output: Car: Toyota Corolla, Year: 2020
car1.start_engine()       # Output: The Toyota Corolla's engine has started.

car2.display_info()       # Output: Car: Honda Civic, Year: 2018
car2.start_engine()       # Output: The Honda Civic's engine has started.

# ---------------------------------------------
# How it works:
# - The class 'Car' defines what attributes (brand, model, year) and methods
#   (display_info, start_engine) all car objects will have.
# - When you create an object like 'car1', Python runs __init__ to set its attributes.
# - You call methods on objects using dot notation (car1.display_info()).
# - Each object has its own independent data.

# ---------------------------------------------
# Encapsulation: Keeping data safe and controlled

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute (note the __ prefix)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Added {amount} to balance.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount} from balance.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

# ---------------------------------------------
# Using the BankAccount class:

account = BankAccount("Alice", 1000)
account.deposit(500)          # Adds money
account.withdraw(200)         # Withdraws money
print("Current balance:", account.get_balance())  # Access balance safely

# Trying to access __balance directly will fail:
# print(account.__balance)    # This will cause an error

# ---------------------------------------------
# Summary:
# - Classes are blueprints; objects are instances of classes.
# - Use __init__ to initialize objects.
# - Methods define behaviors.
# - Attributes store data.
# - Encapsulation hides internal data (with __).
# - OOP helps structure complex programs.

# ---------------------------------------------
# Practice Ideas:
# 1. Create a class for a library book with attributes like title, author, and methods to borrow or return the book.
# 2. Add encapsulation to protect some attributes.
# 3. Experiment with multiple objects and their interactions.

