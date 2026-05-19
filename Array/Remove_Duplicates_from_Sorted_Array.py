def removeDuplicates(arr):
    n = len(arr)
    if n <= 1:
        return n

    # Start from the second element
    idx = 1  
    
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1

    return idx
