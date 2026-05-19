def second_largest(arr):
    m = float('-inf')  # largest
    s = float('-inf')  # second largest
    for i in arr:
        if i > m:
            s, m = m, i
        elif i > s and i != m:
            s = i
    return s if s != float('-inf') else None
