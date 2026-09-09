import itertools
import sys
import threading
import time
from timeit import default_timer as timer
from Random_Array_Generator import random_array

def MergeSort(arr, display_sorted = True):
    def animate_loading(stop_event, items):
        spinner = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])
        while not stop_event.is_set():
            sys.stdout.write(
                f"\r{next(spinner)} Running Merge Sort on {items} items... Please wait..."
            )
            sys.stdout.flush()
            time.sleep(0.1)
        # Clear the loading message once completed
        sys.stdout.write("\r✅ Merge Sort Complete!\n")

    #arr = random_array()

    stop_loading = threading.Event()
    items = len(arr)
    loading_thread = threading.Thread(target=animate_loading, args=(stop_loading,items))

    loading_thread.start()
    start = timer()

    def Merge_Sort(arr):
        if len(arr) <= 1:
            return arr

        slice_index = len(arr)//2
        right_side = arr[slice_index:]
        left_side = arr[:slice_index]

        sorted_right = Merge_Sort(right_side)
        sorted_left = Merge_Sort(left_side)


        return Merge(sorted_right, sorted_left)


    def Merge(sorted_right, sorted_left):
        merged_list = []
        i=0
        j=0

        while i < len(sorted_right) and j < len(sorted_left):
            if sorted_left[j] < sorted_right[i]:
                merged_list.append(sorted_left[j])
                j += 1
            else:
                merged_list.append(sorted_right[i])
                i += 1

        merged_list.extend(sorted_left[j:])
        merged_list.extend(sorted_right[i:])

        return merged_list

    stop_loading.set()
    loading_thread.join()

    result = Merge_Sort(arr)

    end = timer()
    timetaken = end - start

    if display_sorted:
        print(f"The Sorted List is = {result[:20]}....")
    print(f"The time taken for the Merge Sort to execute is: {timetaken:.3f}s")