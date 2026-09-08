import random

def random_array():
    print("Generating list...")
    arr = [random.randint(1, 5000) for _ in range(20000)]
    print(f"The Unsorted List is = {arr[:20]}....")
    return arr
