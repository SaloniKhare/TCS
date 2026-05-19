class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        p=0
        for i in range(1,len(prices)):
            buy=min(prices[i],buy)
            p=max(prices[i]-buy,p)
        return p
