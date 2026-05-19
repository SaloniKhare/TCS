def missingNum(arr):
    n = len(arr) + 1

    # Create hash array of size n+1
    hash = [0] * (n + 1)

    # Store frequencies of elements
    for i in range(n - 1):
        hash[arr[i]] += 1

    # Find the missing number
    for i in range(1, n + 1):
        if hash[i] == 0:
            return i
    return -1

def missingNum(arr):
    n = len(arr) + 1

    # Calculate the sum of array elements
    totalSum = sum(arr)

    # Calculate the expected sum
    expSum = n * (n + 1) // 2

    # Return the missing number
    return expSum - totalSum

b=[1,2,4]
def missingNum(arr):
    n = len(arr) + 1
    xor1 = 0
    xor2 = 0
    for i in range(n - 1):
        xor2 ^= arr[i]
    for i in range(1, n + 1):
        xor1 ^= i
    return xor1 ^ xor2
print(missingNum(b))
