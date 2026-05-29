#O(2^n), O(n)
def nth_fibonacci(n):
    if n <= 1:
        return n
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

#O(n), O(n)
def nthFibonacciUtil(n, dp):
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = nthFibonacciUtil(n - 1, dp) + nthFibonacciUtil(n - 2, dp)
    return dp[n]

#O(n), O(n)
def nthFibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

#O(n), O(1)
def nthFibonacci(n):
    if n <= 1:
        return n
    curr = 0
    prev1 = 1
    prev2 = 0
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr

