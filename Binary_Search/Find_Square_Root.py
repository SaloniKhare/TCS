import math
class Solution:
    def floorSqrt(self, n): 
        # code here
        if n==0 or n==1:
            return n
        l,h=1,n
        res=0
        while l<=h:
            m=(l+h)//2
            if m*m>n:
                h=m-1
            elif m*m<n:
                res=m
                l=m+1
            else:
                return m
        return res
