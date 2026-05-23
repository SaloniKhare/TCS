#User function Template for python3
import heapq
class Solution:
    #Function to return kth largest element from an array.
    
    def kthLargest(self,arr,k):
        he = list(map(lambda x: -x, arr))
        heapq.heapify(he)
        for i in range(k):
            h=-heapq.heappop(he)
        return h
        # code here
        
        
        
