import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        h=[]
        for i,v in freq.items():
            heapq.heappush(h,(-v,i))
        ans=[]
        for _ in range(k):
            a=heapq.heappop(h)
            ans.append(a[1])
        return ans
