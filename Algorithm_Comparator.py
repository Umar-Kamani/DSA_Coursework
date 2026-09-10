from Insertion_Sort_old import insertionSort
from Merge_Sort import MergeSort

def algorithm_comparator(arr):
    insertionSort(arr, display_sorted = False)
    MergeSort(arr, display_sorted= False)

