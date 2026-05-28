def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



"""# Insertion Sort Complexity Analysis

## Complexity Table

| Complexity Type  | Complexity     |
| ---------------- | -------------- |
| Time Complexity  | Best: O(n)     |
|                  | Average: O(n²) |
|                  | Worst: O(n²)   |
| Space Complexity | O(1)           |

---

# Time Complexity Analysis of Insertion Sort

Insertion Sort works by taking one element at a time and inserting it into its correct position in the sorted part of the array.

---

# Best Case Time Complexity: O(n)

The best case occurs when the array is already sorted.

Example:

[
[1,2,3,4,5]
]

In this case:

* Each element is already greater than the previous element.
* Only one comparison is needed for each pass.
* No shifting is required.

### Comparisons

[
n - 1
]

Therefore:

T(n)=O(n)

So, the best-case time complexity is **O(n)**.

---

# Worst Case Time Complexity: O(n²)

The worst case occurs when the array is sorted in decreasing order.

Example:

[
[5,4,3,2,1]
]

Each new element must be compared with all previously sorted elements and shifted to the beginning.

---

## Pass-wise Analysis

### Pass 1

Comparisons = 1
Shifts = 1

### Pass 2

Comparisons = 2
Shifts = 2

### Pass 3

Comparisons = 3
Shifts = 3

...

### Pass ( n-1 )

Comparisons = ( n-1 )
Shifts = ( n-1 )

---

# Total Comparisons

[
1+2+3+\dots+(n-1)
]

Using the summation formula:

\sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}

Ignoring constants and lower-order terms:

T(n)=O(n^2)

Hence, the worst-case time complexity is **O(n²)**.

---

# Average Case Time Complexity: O(n²)

In the average case, elements are randomly arranged.

Each element may need to be shifted halfway through the sorted portion of the array.

Average comparisons and shifts are proportional to:

[
\frac{n(n-1)}{2}
]

Therefore:

T(n)=O(n^2)

Thus, the average-case complexity is **O(n²)**.

---

# Space Complexity Analysis of Insertion Sort

Insertion Sort is an **in-place sorting algorithm**.

It only requires:

* one temporary variable (`key`)
* loop counters

No additional array is used.

Therefore, the space complexity is:

S(n)=O(1)

---

# Advantages of Insertion Sort

* Simple and easy to implement
* Efficient for small datasets
* Adaptive (works faster for nearly sorted arrays)
* Stable sorting algorithm
* In-place sorting algorithm

---

# Final Conclusion

* **Best Case:** O(n)
* **Average Case:** O(n²)
* **Worst Case:** O(n²)
* **Space Complexity:** O(1)

Insertion Sort performs efficiently for small or nearly sorted arrays but becomes slow for large datasets because of its quadratic time complexity in average and worst cases.
"""
