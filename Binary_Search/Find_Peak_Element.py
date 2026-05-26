class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ind=0
        m=float('-inf')
        for i in range(len(nums)):
            if nums[i]>m:
                m=nums[i]
                ind=i
        return ind


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left
