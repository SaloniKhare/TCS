class Solution:
    def reverseWords(self, s: str) -> str:
        n=len(x)
        for i in range(n//2):
            x[i],x[n-i-1]=x[n-i-1],x[i]
        
        return " ".join(x)



class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
