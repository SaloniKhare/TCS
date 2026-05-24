class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=sorted(strs)
        a,b=x[0],x[-1]
        ans=""
        print(x)
        for i in range(min(len(a),len(b))):
            if a[i]!=b[i]:
                return ans
            ans+=a[i]
        return ans
