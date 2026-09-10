from Insertion_Sort_old import insertionSort as insertion_sort_old
from Insertion_Sort_new import insertionSort as insertion_sort_new
from Merge_Sort import MergeSort
from Algorithm_Comparator import algorithm_comparator
from Random_Array_Generator import random_array
import benchmark_new as bench_new
import benchmark_old as bench_old


def main_menu(n, arr):
    print(f"\nCURRENT VALUE n = {n}")
    print("1. Run Insertion Sort (AI Corrected)")
    print("2. Run Insertion Sort (Umar's Wonky Algorithm")
    print("3. Run Merge Sort")
    print("4. Run Insertion Sort Vs Merge Sort")
    print("5. Choose Value of n")
    print("6. Run Benchmark (Using AI Corrected Insertion Sort")
    print("7. Run Benchmark (Using Umar's Wonky Insertion Sort")
    print("8. Exit")
    print("Note: ** The 2 Insertion Sort Algorithms work the same when running a single sort **")

    while True:  # This loop checks for correct user choice input
     main_menu_choice = input("Enter your choice: ").lower()
     if main_menu_choice not in ('1', '2', '3', '4', '5', '6', '7', '8', 'exit'):
         print("Invalid choice. Please try again.")
     else:
         break
    if main_menu_choice == '1':
        print("\n")
        insertion_sort_new(arr, display_sorted=True)
        return main_menu(n, arr)

    elif main_menu_choice == '2':
        print("\n")
        insertion_sort_old(arr, display_sorted=True)
        return main_menu(n, arr)

    elif main_menu_choice == '3':
        print("\n")
        MergeSort(arr, display_sorted=True)
        return main_menu(n, arr)

    elif main_menu_choice == '4':
        algorithm_comparator(arr)
        return main_menu(n, arr)

    elif main_menu_choice == '5':
        n = valueOfN()
        arr = random_array(n)
        return main_menu(n, arr)

    elif main_menu_choice =='6':
        results = bench_new.run_benchmark()
        bench_new.save_results(results)
        bench_new.calculate_doubling_ratios(results)
        bench_new.create_plot(results)

    elif main_menu_choice =='7':
        results = bench_old.run_benchmark()
        bench_old.save_results(results)
        bench_old.calculate_doubling_ratios(results)
        bench_old.create_plot(results)

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

if __name__ == "__main__":
    print("Welcome Facilitator!!!")
    print("This program is designed to help us compare Insertion Sort and Merge Sort")
    print("-------------------------------------------------------------------------")
    n = valueOfN()
    arr = random_array(n)
    main_menu(n, arr)