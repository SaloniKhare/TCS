class Solution:
    def merge(self, inte: List[List[int]]) -> List[List[int]]:
        i=0
        ans=[]
        inte.sort(key=lambda x: x[0])
        n=len(inte)
        while i<n:
            st=inte[i][0]
            e=inte[i][1]
            while i+1<n and e>=inte[i+1][0] :
                e=max(e,inte[i+1][1])
                i+=1
            i+=1
            ans.append([st,e])
        return ans
