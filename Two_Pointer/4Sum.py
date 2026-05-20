def fourSum(arr, target):
    res = []
    n = len(arr)
    arr.sort()
    for i in range(n):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            k, l = j + 1, n - 1
            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]
                if total == target:
                    res.append([arr[i], arr[j], arr[k], arr[l]])
                    k += 1
                    l -= 1
                    while k < l and arr[k] == arr[k - 1]:
                        k += 1
                    while k < l and arr[l] == arr[l + 1]:
                        l -= 1
                elif total < target:
                    k += 1
                else:
                    l -= 1
    return res


def fourSum(arr, target):
    res_set = set()
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            s = set()
            for k in range(j + 1, n):
                sum_val = arr[i] + arr[j] + arr[k]
                last = target - sum_val
                if last in s:
                    curr = sorted([arr[i], arr[j], arr[k], last])
                    res_set.add(tuple(curr))
                s.add(arr[k])
    return [list(t) for t in res_set]
