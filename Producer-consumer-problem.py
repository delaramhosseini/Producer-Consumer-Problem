import time
import random

class AtomicVariable:
    def __init__(self, initial_value,sleep_time=1):
        self.value = initial_value
        self.lock = False  # Simulate a lock using a boolean flag
        self.sleep_time = sleep_time

    def read(self,thread_number=1):
        if (self.lock):print(f"Thread number {thread_number} is waiting..." )
        while self.lock:
            pass
        print(f"Thread number {thread_number} entered into atomic_increment " )
        return self.value

    def atomic_increment(self , thread_number= 1):
        if (self.lock):print(f"Thread number {thread_number} is waiting..." )
        while self.lock:
            pass
        self.lock = True
        print(f"Thread number {thread_number} entered into atomic_increment " )
        self.value += 1
        time.sleep(random.uniform(0.1*thread_number  ,self.sleep_time) )
        self.lock = False

    def atomic_decrement(self , thread_number= 1):
        if (self.lock):print(f"Thread number {thread_number} is waiting..." )
        while self.lock:
            pass
        self.lock = True
        print(f"Thread number {thread_number} entered into atomic_decrement " )
        self.value -= 1
        time.sleep(random.uniform(0.1*thread_number  ,self.sleep_time) )
        self.lock = False

    def atomic_add(self, value , thread_number= 1):
        if (self.lock):print(f"Thread number {thread_number} is waiting..." )
        while self.lock:
            pass
        print(f"Thread number {thread_number} entered into atomic_add " )
        self.lock = True

        self.value += value
        time.sleep(random.uniform(0.1*thread_number  ,self.sleep_time) )
        self.lock = False

    def atomic_subtract(self, value , thread_number= 1):
        if (self.lock):print(f"Thread number {thread_number} is waiting..." )
        while self.lock:
            pass
        self.lock = True
        print(f"Thread number {thread_number} entered into atomic_subtract " )
        time.sleep(random.uniform(0.1*thread_number  ,self.sleep_time) )
        self.value -= value
        self.lock = False

    def atomic_multiply(self, factor, thread_number= 1):
        if (self.lock):print(f"Thread number {thread_number} is waiting..." )
        while self.lock:
            pass
        self.lock = True
        print(f"Thread number {thread_number} entered into atomic_multiply " )
        self.value *= factor
        time.sleep(random.uniform(0.1*thread_number  ,self.sleep_time) )
        self.lock = False



import threading

# Implement the AtomicVariable class here...

def worker_function1(atomic_var,thread_number):
    # Perform a sequence of atomic operations
    atomic_var.atomic_increment(thread_number)
    atomic_var.atomic_increment(thread_number)
    atomic_var.atomic_increment(thread_number)
    atomic_var.atomic_increment(thread_number)
    atomic_var.atomic_increment(thread_number)
    atomic_var.atomic_add(8,thread_number)
    atomic_var.atomic_multiply(2,thread_number)
    atomic_var.atomic_subtract(3,thread_number)
    atomic_var.atomic_decrement(thread_number)

def worker_function2(atomic_var,thread_number):
    # Perform a sequence of atomic operations
    atomic_var.atomic_increment(thread_number)
    atomic_var.atomic_add(8,thread_number)
    atomic_var.atomic_multiply(2,thread_number)
    atomic_var.atomic_subtract(3,thread_number)
    atomic_var.atomic_decrement(thread_number)

# Example usage in a multi-threaded program:
atomic_var = AtomicVariable(initial_value=10)

# Create two threads
thread1 = threading.Thread(target=worker_function1, args=(atomic_var,1))
thread2 = threading.Thread(target=worker_function2, args=(atomic_var,2))

# Start the threads
thread2.start()
thread1.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

# Read the final result after concurrent atomic operations
result = atomic_var.read()
print(f"Final Result after Concurrent Atomic Operations: {result}")

