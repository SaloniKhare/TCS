class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        m=max(freq.values())
        s=0
        for k,v in freq.items():
            if v==m:
                s+=v
        return s
