def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    i = 0  
    j = 0  
    k = left  
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)



"""# Merge Sort Complexity Analysis

## Complexity Table

| Complexity Type  | Complexity          |
| ---------------- | ------------------- |
| Time Complexity  | Best: O(n log n)    |
|                  | Average: O(n log n) |
|                  | Worst: O(n log n)   |
| Space Complexity | O(n)                |

---

# Time Complexity Analysis of Merge Sort

Merge Sort follows the **Divide and Conquer** approach.

The algorithm works in three steps:

1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the sorted halves.

---

# Division Process

The array is repeatedly divided into halves until each subarray contains only one element.

If the array size is ( n ), then the number of divisions is:

\log_2 n

---

# Merging Process

At each level, all elements are merged once.

The work done at every level is proportional to:

[
O(n)
]

Since there are ( \log n ) levels, total work becomes:

T(n)=O(n\log n)

---

# Best Case Time Complexity: O(n log n)

Even if the array is already sorted, Merge Sort still:

* divides the array
* recursively processes subarrays
* merges all elements

Therefore, the best-case complexity remains:

T(n)=O(n\log n)

---

# Worst Case Time Complexity: O(n log n)

The worst case occurs when maximum merging operations are required.

However, Merge Sort always performs:

* ( \log n ) levels of division
* ( n ) operations at each level

Hence:

T(n)=O(n\log n)

---

# Average Case Time Complexity: O(n log n)

For randomly arranged elements:

* recursive division still occurs
* merging still processes all elements at every level

Therefore, average-case complexity is also:

T(n)=O(n\log n)

---

# Recurrence Relation of Merge Sort

The recurrence relation for Merge Sort is:

T(n)=2T\left(\frac{n}{2}\right)+O(n)

Using Master’s Theorem:

[
a = 2,\quad b = 2,\quad f(n)=O(n)
]

Result:

[
T(n)=O(n\log n)
]

---

# Space Complexity Analysis of Merge Sort

Merge Sort requires additional temporary arrays during merging.

Extra memory required:

[
O(n)
]

Therefore:

S(n)=O(n)

---

# Advantages of Merge Sort

* Efficient for large datasets
* Stable sorting algorithm
* Guaranteed ( O(n \log n) ) performance
* Works well for linked lists and external sorting

---

# Disadvantages of Merge Sort

* Requires extra memory
* Not an in-place sorting algorithm
* Recursive calls add overhead

---

# Final Conclusion

* **Best Case:** O(n log n)
* **Average Case:** O(n log n)
* **Worst Case:** O(n log n)
* **Space Complexity:** O(n)

Merge Sort is one of the most efficient comparison-based sorting algorithms and is widely used when stable and predictable performance is required.

"""
