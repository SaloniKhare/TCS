def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


"""# Selection Sort Complexity Analysis

## Complexity Table

| Complexity Type  | Complexity     |
| ---------------- | -------------- |
| Time Complexity  | Best: O(n²)    |
|                  | Average: O(n²) |
|                  | Worst: O(n²)   |
| Space Complexity | O(1)           |

---

# Time Complexity Analysis of Selection Sort

Selection Sort works by repeatedly selecting the minimum element from the unsorted part of the array and placing it at the correct position.

---

# Best Case Time Complexity: O(n²)

Even if the array is already sorted, Selection Sort still compares every element with the remaining unsorted elements.

Example:

[
[1,2,3,4,5]
]

The algorithm still performs all comparisons to find the minimum element.

### Comparisons Per Pass

### Pass 1

Comparisons = ( n - 1 )

### Pass 2

Comparisons = ( n - 2 )

### Pass 3

Comparisons = ( n - 3 )

...

### Pass ( n-1 )

Comparisons = 1

---

## Total Comparisons

[
(n-1)+(n-2)+(n-3)+\dots+2+1
]

Using the summation formula:

\sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}

Ignoring constants and lower-order terms:

T(n)=O(n^2)

Hence, the best-case time complexity is **O(n²)**.

---

# Worst Case Time Complexity: O(n²)

The worst case occurs when the array is sorted in reverse order.

Example:

[
[5,4,3,2,1]
]

Selection Sort still performs the same number of comparisons as in the best case.

Total comparisons remain:

[
\frac{n(n-1)}{2}
]

Thus:

T(n)=O(n^2)

---

# Average Case Time Complexity: O(n²)

In the average case, elements are randomly arranged.

Selection Sort always searches the entire unsorted portion to find the minimum element.

Therefore, the number of comparisons remains approximately:

[
\frac{n(n-1)}{2}
]

Hence:

T(n)=O(n^2)

---

# Swap Analysis of Selection Sort

One important advantage of Selection Sort is that it performs fewer swaps.

* Maximum swaps = ( n - 1 )

Because only one swap is performed in each pass after finding the minimum element.

This makes Selection Sort useful when swapping is costly.

---

# Space Complexity Analysis of Selection Sort

Selection Sort is an **in-place sorting algorithm**.

It only uses:

* loop variables
* temporary variable for swapping

No extra array is required.

Therefore, the space complexity is:

S(n)=O(1)

---

# Final Conclusion

* **Best Case:** O(n²)
* **Average Case:** O(n²)
* **Worst Case:** O(n²)
* **Space Complexity:** O(1)

Selection Sort is simple and memory-efficient, but inefficient for large datasets because it always performs quadratic comparisons regardless of input order.
"""
