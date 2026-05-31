def nextLargerElement(arr):
    n = len(arr)
    res = [-1] * n  
    stk = []  
    for i in range(n - 1, -1, -1):
        while stk and arr[stk[-1]] <= arr[i]:
            stk.pop()
        if stk:
            res[i] = arr[stk[-1]]
        stk.append(i)
    return res
