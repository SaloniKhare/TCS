class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res=len(nums)
        l=0
        h=len(nums)-1
        while l<=h:
            m=l+(h-l)//2
            if nums[m]<target:
                l=m+1
            else:
                res=m
                h=m-1
        return res
