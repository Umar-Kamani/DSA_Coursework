import statistics
import csv
from timeit import default_timer as timer


from Insertion_Sort_old import insertionSort
from Merge_Sort import MergeSort
from Random_Array_Generator import random_array


SIZES = [500, 1000, 2000, 4000, 8000]
RUNS = 5


def measure_insertion_random(n):
    times = []

    for i in range(RUNS):

        arr = random_array(n)
        start = timer()
        insertionSort(arr, display_sorted=False)
        end = timer()
        times.append(end - start)

    return statistics.mean(times)


def measure_merge_random(n):
    times = []

    for i in range(RUNS):

        # Build the list BEFORE starting the timer
        arr = random_array(n)
        start = timer()
        MergeSort(arr, display_sorted=False)
        end = timer()
        times.append(end - start)

    return statistics.mean(times)


def measure_insertion_sorted(n):

    times = []

    for i in range(RUNS):
        arr = list(range(n))  # sequential sorted list, rebuilt each run
        start = timer()
        insertionSort(arr, display_sorted=False)
        end = timer()
        times.append(end - start)

    return statistics.mean(times)


def run_benchmark():

    results = []

    print("\nStarting benchmark...")
    print("-" * 70)

    for n in SIZES:

        print(f"\nTesting n = {n}")

        insertion_random = measure_insertion_random(n)

        print(f"Insertion Sort (Random): ")
        print(f"{insertion_random:.10f} seconds")

        merge_random = measure_merge_random(n)

        print(f"Merge Sort (Random): ")
        print(f"{merge_random:.10f} seconds")

        insertion_sorted = measure_insertion_sorted(n)

        print(f"Insertion Sort (Sorted): ")
        print(f"{insertion_sorted:.10f} seconds")

        results.append({
            "n": n,
            "Insertion Sort Random": insertion_random,
            "Merge Sort Random": merge_random,
            "Insertion Sort Sorted": insertion_sorted
        })

    return results


def save_results(results):

    with open("benchmarking/benchmark_results.csv", "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "n",
                "Insertion Sort Random",
                "Merge Sort Random",
                "Insertion Sort Sorted"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nResults saved to benchmark_results.csv")


def calculate_doubling_ratios(results):

    print("\n")
    print("=" * 80)
    print("DOUBLING TEST")
    print("=" * 80)

    for i in range(1, len(results)):

        previous = results[i - 1] #We can do this since values are sequentially stored
        current = results[i]

        print(f"\n{previous['n']} -> {current['n']}")

        insertion_random_ratio = ( #extracts from the dictionary where we wrote the test results
            current["Insertion Sort Random"]
            / previous["Insertion Sort Random"]
        )

        merge_random_ratio = (
            current["Merge Sort Random"]
            / previous["Merge Sort Random"]
        )

        insertion_sorted_ratio = (
            current["Insertion Sort Sorted"]
            / previous["Insertion Sort Sorted"]
        )

        print(
            f"Insertion Sort Random: "
            f"{insertion_random_ratio:.2f}"
        )

        print(
            f"Merge Sort Random: "
            f"{merge_random_ratio:.2f}"
        )

        print(
            f"Insertion Sort Sorted: "
            f"{insertion_sorted_ratio:.2f}"
        )


def create_plot(results):

    import matplotlib.pyplot as plt
    n = [row["n"] for row in results]

    insertion_random = [
        row["Insertion Sort Random"] #key
        for row in results
    ]

    merge_random = [
        row["Merge Sort Random"] #key
        for row in results
    ]

    insertion_sorted = [
        row["Insertion Sort Sorted"]
        for row in results
    ]

    plt.plot(
        n,
        insertion_random,
        marker="o",
        label="Insertion Sort - Random"
    )

    plt.plot(
        n,
        merge_random,
        marker="o",
        label="Merge Sort - Random"
    )

    plt.plot(
        n,
        insertion_sorted,
        marker="o",
        label="Insertion Sort - Already Sorted"
    )

    plt.xlabel("Input size (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Sorting Algorithm Comparison")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("benchmarking/sorting_comparison.png", dpi=600)

    plt.show()
    print("\nGraph saved to comparison.png")