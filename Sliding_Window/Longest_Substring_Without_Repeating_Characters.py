class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        di={}
        l=0
        ans=0
        for i,j in enumerate(s):
            di[j]=di.get(j,0)+1
            while di[j]>1:
                di[s[l]]-=1
                l+=1
            ans=max(ans,i-l+1)
        return ans



