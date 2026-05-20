class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        arr.sort()
        if len(arr)<3:
            return False
        n=len(arr)
        for i in range(n-2):
            a,b=i+1,n-1
            while a<b:
                s=arr[i]+arr[a]+arr[b]
                if s==target:
                    return True
                elif s<target:
                    a+=1
                else:
                    b-=1
        return False
        
