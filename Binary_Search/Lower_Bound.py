class Solution:
    def lowerBound(self, arr, target):
        # code here
        l,h=0,len(arr)-1
        while l<=h:
            m=l+(h-l)//2
            if arr[m]<target:
                l=m+1
            else:
                h=m-1
        return l
        
        
import bisect

def lowerBound(arr, target):
    
    # Using bisect_left to get the lower bound index
    index = bisect.bisect_left(arr, target)
    return index
