class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s={}
        c=0
        for i ,j in enumerate(nums):
            c=target-j
            if c in s:
                return [s[c],i]
            s[j]=i
        
