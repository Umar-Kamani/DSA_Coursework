from Insertion_Sort import insertionSort
from Merge_Sort import MergeSort
from Random_Array_Generator import random_array

def main_menu(n, arr):
    print(f"\nCURRENT VALUE n = {n}")
    print("1. Run Insertion Sort")
    print("2. Run Merge Sort")
    print("3. Run Insertion Sort Vs Merge Sort")
    print("4. Choose Value of n")
    print("5. Exit")

    while True:  # This loop checks for correct user choice input
     main_menu_choice = input("Enter your choice: ").lower()
     if main_menu_choice not in ('1', '2', '3', '4', '5', 'exit'):
         print("Invalid choice. Please try again.")
     else:
         break
    if main_menu_choice == '1':
        print("\n")
        insertionSort(arr)
        return main_menu(n, arr)

    elif main_menu_choice == '2':
        print("\n")
        MergeSort(arr)
        return main_menu(n, arr)

    elif main_menu_choice == '3':
        insertionSort(arr)
        MergeSort(arr)
        return main_menu(n, arr)

    elif main_menu_choice == '4':
        n = valueOfN()
        arr = random_array(n)
        return main_menu(n, arr)

    else:
         print("Thank you.")
         exit()


def valueOfN():
    while True:  # This loop checks for correct user choice input
     n = int(input("Enter your value of n: ").lower())
     if not n:
         print("Invalid value of n. Please try again.")
     else:
         print(f"\nThe Value of n is: {n}")
         break
    return n

print("Welcome Facilitator!!!")
print("This program is designed to help us compare Insertion Sort and Merge Sort")
print("-------------------------------------------------------------------------")
n = valueOfN()
arr = random_array(n)
main_menu(n, arr)