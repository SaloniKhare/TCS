class Solution:
    def romanToDecimal(self, s): 
        # code here
        val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        ans=0
        while i<len(s):
            if i+1<len(s) and val[s[i]]<val[s[i+1]]:
                ans+=val[s[i+1]]-val[s[i]]
                i+=2
            else:
                ans+=val[s[i]]
                i+=1
        return ans
            
