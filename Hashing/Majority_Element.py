from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h=Counter(nums)
        n=len(nums)
        s=n/2
        
        for k,v in h.items():
            if v>s:
                return k

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
