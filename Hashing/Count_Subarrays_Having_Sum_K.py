def cntSubarrays(arr, k):
    
    # for maintaining the count of 
    # subarrays whose sum equal to k
    count = 0
    n = len(arr)

    for i in range(n):
        currSum = 0

        # subarray from i to each j -> arr[i....j]
        for j in range(i, n):
            currSum += arr[j]

            # increment count if the currSum equals k
            if currSum == k:
                count += 1
                
    return count


def cntSubarrays(arr, k):
  
    # Dictionary to store prefix sums frequencies
    prefixSums = {}
    res = 0
    currSum = 0

    for val in arr:
        # Add current element to sum so far
        currSum += val

        # If currSum is equal to desired sum
        # then a new subarray is found
        if currSum == k:
            res += 1

        # Check if the difference exists
        # in the prefixSums dictionary
        if currSum - k in prefixSums:
            res += prefixSums[currSum - k]

        # Add currSum to the dictionary of prefix sums
        prefixSums[currSum] = prefixSums.get(currSum, 0) + 1

    return res
