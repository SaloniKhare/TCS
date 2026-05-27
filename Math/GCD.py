#O(min(a,b)),O(1)
def gcd(a, b):
    if(a==0 or b==0):
        return max(a, b)
    result = min(a, b)
    while result > 0:
        if a % result == 0 and b % result == 0:
            break
        result -= 1
    return result


#O(min(a,b)), O(min(a,b))
def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)

#O(min(a,b)), O(min(a,b))
def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        if a % b == 0:
            return b
        return gcd(a - b, b)
    if b % a == 0:
        return a
    return gcd(a, b - a)


#O(log(min(a,b)), O(log(min(a,b)
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

#O(log(min(a,b),O(1)
import math
def gcd(a, b):
    return math.gcd(a, b)
