import itertools
import sys
import threading
import time
from timeit import default_timer as timer
from random_array_generator import random_array

def animate_loading(stop_event, items):
    spinner = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])
    while not stop_event.is_set():
        sys.stdout.write(
            f"\r{next(spinner)} Running Insertion Sort on {items} items... Please wait..."
        )
        sys.stdout.flush()
        time.sleep(0.1)
    # Clear the loading message once completed
    sys.stdout.write("\r✅ Sorting Complete!\n\n")


# 1. Generate the random unsorted data
arr = random_array()

# 2. Setup and start the loading animation thread
stop_loading = threading.Event()
items = len(arr)
loading_thread = threading.Thread(target=animate_loading, args=(stop_loading,items))


loading_thread.start()

# 3. Execution of your Insertion Sort algorithm
start = timer()
for i in range(1, len(arr)):
    index = i
    current_value = arr.pop(i)

    for j in range(i - 1, -1, -1):
        if arr[j] > current_value:
            index = j
    arr.insert(index, current_value)
end = timer()

# 4. Stop the spinner cleanly after the loop finishes
stop_loading.set()
loading_thread.join()

timetaken = end - start

# 5. Output results
print(f"The Sorted List is = {arr[:20]}....")
print(f"The time taken for the function to execute is: {timetaken:.3f}s")

