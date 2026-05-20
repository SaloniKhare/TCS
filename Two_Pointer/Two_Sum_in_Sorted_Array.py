class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n,m=0,len(numbers)-1
        while n<m:
            s=numbers[n]+numbers[m]
            if s<target:
                n+=1
            elif s>target:
                m-=1
            else:
                return [n+1,m+1]
