import numpy as np

arr = [5, 9, 8, 3, 1, 2]

def Merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    slice_index = (len(arr)//2)

    right_side = arr[slice_index:]
    left_side = arr[:slice_index]

    sorted_right = Merge_Sort(right_side)
    sorted_left = Merge_Sort(left_side)

    return sorted_right, sorted_left

arr2 = Merge_Sort(arr)

def Merge(right_side, left_side):
    merged_list = []
    