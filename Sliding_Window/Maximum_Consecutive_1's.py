def maxConsecBits(arr):
    maxCount, count = 0, 1
    
    # Loop through the array starting from the second element
    for i in range(1, len(arr)):
     
        # If the current element is the same as the previous one
        # increment the count
        if arr[i] == arr[i - 1]:
            count += 1
        # If not equal, update maxCount if needed and reset count
        else:
            maxCount = max(maxCount, count)
            count = 1

    return max(maxCount, count)


def maxConsecBits(arr):
    maxCount, count, prev = 0, 0, -1

    for num in arr:
        
        # If the current number is the same 
        # as the previous number
        if (prev ^ num) == 0:
            count += 1
        else:
            
            # Update max_count and reset count
            maxCount = max(maxCount, count)
            count = 1
        prev = num

    return max(maxCount, count)
