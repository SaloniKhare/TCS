#Iterative Approach
def factorial(n):
    ans = 1
    i = 2
    while (i <= n):
        ans *= i
        i += 1
    return ans

#Recursive Approach
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
