def sort012(arr):
    arr.sort()


def sort012(arr):
    c0 = 0
    c1 = 0
    c2 = 0
    for num in arr:
        if num == 0:
            c0 += 1
        elif num == 1:
            c1 += 1
        else:
            c2 += 1
    idx = 0
    for i in range(c0):
        arr[idx] = 0
        idx += 1
    for i in range(c1):
        arr[idx] = 1
        idx += 1
    for i in range(c2):
        arr[idx] = 2
        idx += 1


def sort012(arr):
    n = len(arr)
    lo = 0
    hi = n - 1
    mid = 0
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1
