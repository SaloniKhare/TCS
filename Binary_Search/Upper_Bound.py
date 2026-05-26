class Solution:
    def upperBound(self, arr, target):
        # code here
        l,h=0,len(arr)-1
        res=len(arr)
        while l<=h:
            m=l+(h-l)//2
            if arr[m]<=target:
                l=m+1
            else:
                res=m
                h=m-1
        return res


import bisect

def upperBound(arr, target):
    
    # Using bisect_right to get the upper bound index
    index = bisect.bisect_right(arr, target)
    return index
