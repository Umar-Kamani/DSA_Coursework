import numpy as np

arr = [5, 9, 8, 3, 1, 2,0]

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

sorted_arr = Merge_Sort(arr)
print(sorted_arr)

