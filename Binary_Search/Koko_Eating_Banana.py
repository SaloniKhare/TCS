class Solution:
    def kokoEat(self, arr, k):
        # Code here
        def check(arr, mid, k):
            totalHours = 0
            for i in range(len(arr)):
                totalHours += (arr[i] + mid - 1) // mid
            return totalHours <= k
        lo = 1
        hi = max(arr)
        res = hi

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if check(arr, mid, k) == True:
                hi = mid - 1
                res = mid
            else:
                lo = mid + 1
        return res
        


    
        
