#Recursion
def subsetRecur(i, arr, res, subset):
    if i == len(arr):
        res.append(list(subset))
        return
    subset.append(arr[i])
    subsetRecur(i + 1, arr, res, subset)
    print(res)
    subset.pop()
    subsetRecur(i + 1, arr, res, subset)

def subsets(arr):
    subset = []
    res = []
    subsetRecur(0, arr, res, subset)
    return res


#Bit_Manipulation
def subsets(arr):
    n = len(arr)
    res = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        res.append(subset)
    return res
