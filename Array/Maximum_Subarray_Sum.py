class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c=m=nums[0]
        for i in range(1,len(nums)):
            c=max(nums[i],c+nums[i])
            m=max(c,m)
        return m
