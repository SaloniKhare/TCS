#Using Modified Insertion Sort
def rearrange(arr):
    for i in range(1, len(arr)):

        # if current element is positive
        # do nothing
        if arr[i] > 0:
            continue

        # if current element is negative,
        # shift positive elements of arr[0..i-1],
        # to one position to their right 
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > 0:
            arr[j + 1] = arr[j]
            j -= 1

        # Put negative element at its right position
        arr[j + 1] = temp

      
#Using Modified Merge Sort (with extra space)
def rotateSubArray(arr, left, right):
    temp = arr[right]
    for i in range(right, left - 1, -1):
        arr[i] = arr[i - 1]
    arr[left] = temp

def rearrange(arr):
  
    # pointer to last added negative number in prefix
    idx = -1

    for i in range(len(arr)):
        if arr[i] < 0:
            idx += 1

            # place current negative element after the 
            # last negative element added
            arr[i], arr[idx] = arr[idx], arr[i]

            # Rotate array to maintain order of positive numbers 
            # in the block arr[(idx + 1) ... i]
            if i - idx >= 2:
                rotateSubArray(arr, idx + 1, i)

              
#Sequentially Placing Negative element to the prefix
              def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = arr[l:m+1]
    R = arr[m+1:r+1]

    i = j = 0
    k = l

    # copy negative elements of left subarray
    while i < n1 and L[i] < 0:
        arr[k] = L[i]
        i += 1
        k += 1

    # copy negative elements of right subarray
    while j < n2 and R[j] < 0:
        arr[k] = R[j]
        j += 1
        k += 1

    # copy positive elements of left subarray
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # copy positive elements of right subarray
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# Function to Rearrange positive and negative
# numbers in an array
def rearrange(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        # Sort first and second halves
        rearrange(arr, l, m)
        rearrange(arr, m + 1, r)

        merge(arr, l, m, r)

      
#Using Modified Merge Sort (without extra space)
def reverse(arr, l, r):
    if l < r:
        arr[l], arr[r] = arr[r], arr[l]
        reverse(arr, l + 1, r - 1)
def merge(arr, l, m, r):
    i = l
    j = m + 1
    while i <= m and arr[i] < 0:
        i += 1
    while j <= r and arr[j] < 0:
        j += 1
    j -= 1
    reverse(arr, i, m)

    reverse(arr, m + 1, j)

    # reverse arr[i..j]
    reverse(arr, i, j)
def rearrange(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        rearrange(arr, l, m)
        rearrange(arr, m + 1, r)

        merge(arr, l, m, r)
