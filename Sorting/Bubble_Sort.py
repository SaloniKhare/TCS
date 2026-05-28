def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break





"""# Bubble Sort Complexity Analysis

## Complexity Table

| Complexity Type  | Complexity     |
| ---------------- | -------------- |
| Time Complexity  | Best: O(n)     |
|                  | Average: O(n²) |
|                  | Worst: O(n²)   |
| Space Complexity | O(1)           |

---

# Time Complexity Analysis of Bubble Sort

## Best Case Time Complexity: O(n)

The best case occurs when the array is already sorted.

In this case:

* Number of comparisons = ( n - 1 )
* Number of swaps = 0

Since only one traversal is needed to verify that the array is sorted, the time complexity becomes:

T(n)=O(n)

---

## Worst Case Time Complexity: O(n²)

The worst case occurs when the array is sorted in decreasing order.

Example:

[
[5,4,3,2,1]
]

In Bubble Sort, each pass places one element in its correct position.

### Pass-wise Analysis

### Pass 1

* Comparisons = ( n - 1 )
* Swaps = ( n - 1 )

### Pass 2

* Comparisons = ( n - 2 )
* Swaps = ( n - 2 )

### Pass 3

* Comparisons = ( n - 3 )
* Swaps = ( n - 3 )

...

### Pass ( n-1 )

* Comparisons = 1
* Swaps = 1

---

## Total Number of Comparisons

[
(n-1)+(n-2)+(n-3)+\dots+2+1
]

Using the sum formula:

\sum_{i=1}^{n-1} i = \frac{n(n-1)}{2}

Therefore:

* Total comparisons = ( \frac{n(n-1)}{2} )
* Total swaps = ( \frac{n(n-1)}{2} )

Ignoring constants and lower-order terms:

T(n)=O(n^2)

Hence, the worst-case time complexity of Bubble Sort is **O(n²)**.

---

## Average Case Time Complexity: O(n²)

In the average case, the elements are randomly distributed.

Bubble Sort still performs almost all comparisons:

[
(n-1)+(n-2)+\dots+1
]

Which equals:

[
\frac{n(n-1)}{2}
]

Thus, the number of comparisons is proportional to ( n^2 ).

Even though the number of swaps may vary, the dominant factor remains quadratic.

Therefore:

T(n)=O(n^2)

---

# Space Complexity Analysis of Bubble Sort

Bubble Sort is an **in-place sorting algorithm**.

It only uses a few extra variables such as:

* loop counters
* temporary variable for swapping

No additional array or data structure is required.

Therefore, the space complexity is:

S(n)=O(1)

This means Bubble Sort requires a constant amount of extra memory regardless of input size.

---

# Final Conclusion

* **Best Case:** O(n)
* **Average Case:** O(n²)
* **Worst Case:** O(n²)
* **Space Complexity:** O(1)

Bubble Sort is simple and easy to implement, but it is inefficient for large datasets because of its quadratic time complexity.
"""
