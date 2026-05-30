def makeCombination(arr, remSum, cur, res, index):
    if remSum == 0:
        res.append(list(cur))
        return
    if remSum < 0 or index >= len(arr):
        return
    cur.append(arr[index])
    makeCombination(arr, remSum - arr[index], cur, res, index)
    cur.pop()
    makeCombination(arr, remSum, cur, res, index + 1)
def targetSumComb(arr, target):
    cur = []
    res = []
    makeCombination(arr, target, cur, res, 0)
    return res
