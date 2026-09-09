import random

def random_array(n):
    print("Generating list...")
    arr = [random.randint(1, 5000) for _ in range(n)]
    print(f"The Unsorted List is = {arr[:20]}....")
    return arr
