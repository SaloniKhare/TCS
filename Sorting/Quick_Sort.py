def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)
    return i + 1
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)



"""# Quick Sort Complexity Analysis

## Complexity Table

| Complexity Type  | Complexity          |
| ---------------- | ------------------- |
| Time Complexity  | Best: O(n log n)    |
|                  | Average: O(n log n) |
|                  | Worst: O(n²)        |
| Space Complexity | O(log n)            |

---

# Time Complexity Analysis of Quick Sort

Quick Sort follows the **Divide and Conquer** approach.

The algorithm works as follows:

1. Select a pivot element.
2. Partition the array around the pivot.
3. Recursively sort the left and right subarrays.

---

# Partitioning Process

During partitioning:

* elements smaller than the pivot move to the left
* elements greater than the pivot move to the right

Partitioning takes:

[
O(n)
]

because every element is compared with the pivot once.

---

# Best Case Time Complexity: O(n log n)

The best case occurs when the pivot divides the array into two equal halves.

Example:

[
\frac{n}{2}, \frac{n}{2}
]

At each level:

* partitioning takes ( O(n) )
* number of levels becomes ( \log n )

Therefore:

T(n)=O(n\log n)

---

# Recurrence Relation (Best Case)

T(n)=2T\left(\frac{n}{2}\right)+O(n)

Using Master’s Theorem:

[
T(n)=O(n\log n)
]

---

# Worst Case Time Complexity: O(n²)

The worst case occurs when the pivot is always the smallest or largest element.

Example:

* already sorted array
* reverse sorted array

Partition sizes become:

[
0 \quad \text{and} \quad n-1
]

---

# Recurrence Relation (Worst Case)

T(n)=T(n-1)+O(n)

Expanding:

[
n + (n-1) + (n-2) + \dots + 1
]

Using summation:

\sum_{i=1}^{n} i = \frac{n(n+1)}{2}

Ignoring constants and lower-order terms:

T(n)=O(n^2)

Hence, worst-case complexity is **O(n²)**.

---

# Average Case Time Complexity: O(n log n)

In the average case:

* pivot divides the array reasonably evenly
* recursion depth remains close to ( \log n )

Each level performs ( O(n) ) work.

Thus:

T(n)=O(n\log n)

---

# Space Complexity Analysis of Quick Sort

Quick Sort is an **in-place sorting algorithm** because it does not require extra arrays.

However, recursive function calls use stack memory.

* Best/Average case recursion depth:

[
\log n
]

Therefore:

S(n)=O(\log n)

* Worst-case recursion depth:

[
n
]

which can lead to:

[
O(n)
]

stack space in the worst case.

---

# Advantages of Quick Sort

* Very fast in practice
* In-place sorting algorithm
* Cache efficient
* Widely used in real-world applications

---

# Disadvantages of Quick Sort

* Worst-case complexity is ( O(n^2) )
* Recursive calls may cause stack overflow for very large arrays
* Not a stable sorting algorithm

---

# Final Conclusion

* **Best Case:** O(n log n)
* **Average Case:** O(n log n)
* **Worst Case:** O(n²)
* **Space Complexity:** O(log n)

Quick Sort is one of the fastest sorting algorithms in practice and is commonly used because of its excellent average-case performance and in-place sorting capability.
"""
