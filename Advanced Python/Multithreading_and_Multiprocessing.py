# ---------------------------------------------
# Multithreading and Multiprocessing
# ---------------------------------------------

# 🚀 What are Multithreading and Multiprocessing?
# Both are techniques to run multiple tasks at the same time, improving efficiency.
# - Multithreading: Multiple threads run inside the same program, sharing memory.
# - Multiprocessing: Multiple processes run independently, each with its own memory.

# Multithreading is good for I/O-bound tasks (like waiting for files or network).
# Multiprocessing is better for CPU-bound tasks (heavy computations).

# ---------------------------------------------
# Example 1: Multithreading

import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)  # Pause for 1 second

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1.5)  # Pause for 1.5 seconds

# Create thread objects targeting the above functions
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start both threads (run concurrently)
thread1.start()
thread2.start()

# Wait for both threads to complete before moving on
thread1.join()
thread2.join()

print("Both threads finished!")

# How it works:
# - We define two functions doing different tasks.
# - We create threads for each function, then start them.
# - Threads run simultaneously, so numbers and letters print interleaved.
# - join() ensures main program waits for both threads to finish before printing last message.

# ---------------------------------------------
# Example 2: Multiprocessing

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        print(f"Square: {i*i}")
        time.sleep(1)

def cube_numbers():
    for i in range(5):
        print(f"Cube: {i**3}")
        time.sleep(1.5)

# Create process objects targeting the above functions
process1 = multiprocessing.Process(target=square_numbers)
process2 = multiprocessing.Process(target=cube_numbers)

# Start both processes (run independently)
process1.start()
process2.start()

# Wait for both processes to finish
process1.join()
process2.join()

print("Both processes finished!")

# How it works:
# - Similar to threading but each process has its own memory space.
# - Processes run truly in parallel on multi-core CPUs.
# - Good for CPU-heavy tasks like calculations.
# - join() waits for process completion before moving on.

# ---------------------------------------------
# Summary:
# - Use threading for I/O-bound tasks (like web requests, file I/O).
# - Use multiprocessing for CPU-bound tasks (like math calculations, data processing).
# - Both help your program do multiple things at once, speeding up overall execution.
# - Threads share memory; processes don’t, which helps avoid some bugs but needs inter-process communication if they must share data.

# ---------------------------------------------
# Practice:
# 1. Try creating your own threads to run simple tasks simultaneously.
# 2. Experiment with multiprocessing to speed up computation-heavy code.
# 3. Observe how output from threads/processes interleaves or runs in parallel.

