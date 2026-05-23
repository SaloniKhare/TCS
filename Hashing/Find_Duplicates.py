class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums) + 1)
        res = []
        for num in nums:
            if arr[num] == 0:
                arr[num] = 1
            else:
                res.append(num)
        return res


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicate=[]
        left=0
        hash=set()
        for i in nums:
            if i in hash:
                duplicate.append(i)
            hash.add(i)
        return duplicate


from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        c=Counter(nums)
        for i in c:
            if c[i]>=2:
                res.append(i)
        return res
       
