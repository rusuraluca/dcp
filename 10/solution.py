"""
Problem #10 [Medium]

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
# We can implement a job scheduler using the threading module in Python.
# The scheduler will create a new thread that sleeps for n milliseconds
# before calling the function f. This allows the main thread to continue executing
# without being blocked by the sleep.
# Time complexity of O(1) for scheduling the job
# Space complexity of O(1) for storing the thread reference
# where n is the number of milliseconds to wait before calling f.
import threading
import time
from typing import Callable


def job_scheduler(f: Callable, n: int) -> None:
    def wrapper():
        time.sleep(n / 1000)  # Convert milliseconds to seconds
        f()

    thread = threading.Thread(target=wrapper)
    thread.start()
    return thread  # Return the thread in case we want to join it later

# Example usage:
if __name__ == "__main__":
    def my_function():
        print("Function executed!")

    print("Scheduling function to be called after 2000 milliseconds...")
    job_scheduler(my_function, 2000)
    print("Function scheduled. Main thread continues to run.")
    time.sleep(3)  # Wait to ensure the scheduled function has time to execute
    print("Main thread finished.")
