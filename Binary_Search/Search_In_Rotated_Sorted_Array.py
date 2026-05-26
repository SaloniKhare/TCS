class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        rot = bisect_left(nums, True, key=lambda n: n <= nums[-1])
        
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real
                
            if nums[real] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid

            if nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left = mid+1
            else:
                if nums[right]>=target>nums[mid]:
                    left = mid+1
                else:
                    right = mid-1       
        return -1
