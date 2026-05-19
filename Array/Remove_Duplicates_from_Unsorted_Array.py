def removeDuplicates(arr):
    
    # To track seen elements
    seen = set()
    
    # To maintain the new size of the array
    idx = 0

    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            arr[idx] = arr[i]
            idx += 1

    # Return the size of the array 
    # with unique elements
    return idx
