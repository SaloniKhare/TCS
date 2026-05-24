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


def longestUniqueSubstr(s):
    n = len(s)
    res = 0
    lastIndex = [-1] * 26
    start = 0
    for end in range(n):
        start = max(start, lastIndex[ord(s[end]) - ord('a')] + 1)
        res = max(res, end - start + 1)
        lastIndex[ord(s[end]) - ord('a')] = end
    return res
