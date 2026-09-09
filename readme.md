# DSA Coursework - Sorting Algorithm Comparison

A Python-based Data Structures and Algorithms coursework project designed to demonstrate, execute, and compare two sorting algorithms:

* **Insertion Sort**
* **Merge Sort**

The program generates a random list of integers and allows the user to run either sorting algorithm individually or compare their execution times.

---

## Project Overview

This project demonstrates the practical implementation and performance comparison of two fundamental sorting algorithms.

The user is first asked to provide a value for **n**, representing the number of elements in the randomly generated array.

The program then provides an interactive menu allowing the user to:

1. Run Insertion Sort
2. Run Merge Sort
3. Compare Insertion Sort and Merge Sort
4. Choose a new value of `n`
5. Exit the program

---

## Project Structure

```text
DSA_Coursework/
│
├── Main.py
├── Algorithm_Comparator.py
├── Insertion_Sort.py
├── Merge_Sort.py
├── Random_Array_Generator.py
│
└── README.md
```

### File Descriptions

| File                        | Description                                         |
| --------------------------- | --------------------------------------------------- |
| `Main.py`                   | Contains the main program flow and interactive menu |
| `Algorithm_Comparator.py`   | Runs both sorting algorithms for comparison         |
| `Insertion_Sort.py`         | Implements the Insertion Sort algorithm             |
| `Merge_Sort.py`             | Implements the Merge Sort algorithm                 |
| `Random_Array_Generator.py` | Generates random integer arrays                     |
| `README.md`                 | Project documentation                               |

---

## Program Flow

The general flow of the program is:

```text
Start
  │
  ▼
Display Welcome Message
  │
  ▼
Ask user for n
  │
  ▼
Generate random array of n elements
  │
  ▼
Display Main Menu
  │
  ├── 1 → Run Insertion Sort
  │
  ├── 2 → Run Merge Sort
  │
  ├── 3 → Compare Both Algorithms
  │
  ├── 4 → Choose a New Value of n
  │
  └── 5 → Exit
  │
  ▼
Return to Main Menu
```

---

# Algorithms

## 1. Insertion Sort

Insertion Sort builds a sorted portion of the array one element at a time.

For each element, the algorithm:

1. Selects the current element.
2. Compares it with elements before it.
3. Finds its appropriate position.
4. Inserts it into the sorted portion.

## 2. Merge Sort

Merge Sort uses the **divide-and-conquer** approach.

The algorithm:

1. Divides the array into two halves.
2. Recursively sorts each half.
3. Merges the two sorted halves together.
4. Continues until the complete array is sorted.


# Algorithm Comparison

The project can be used to demonstrate the difference in performance between the two algorithms.

| Feature                     | Insertion Sort      | Merge Sort         |
| --------------------------- | ------------------- | ------------------ |
| Approach                    | Incremental sorting | Divide and conquer |
| Best Case                   | `O(n)`              | `O(n log n)`       |
| Average Case                | `O(n²)`             | `O(n log n)`       |
| Worst Case                  | `O(n²)`             | `O(n log n)`       |
| Extra Space                 | `O(1)`              | `O(n)`             |
| Suitable for large datasets | Generally No        | Generally Yes      |
| Implementation              | Relatively simple   | More complex       |



---


This repository was created as part of a **Data Structures and Algorithms (DSA)** coursework project.
