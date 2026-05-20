class Solution:
    def trap(self, arr: List[int]) -> int:
        re=0
        l,r=1,len(arr)-2
        lm,rm=arr[0],arr[len(arr)-1]
        while l<=r:
            if rm<=lm:
                re+=max(0,rm-arr[r])
                rm=max(rm,arr[r])
                r-=1
            else:
                re+=max(0,lm-arr[l])
                lm=max(lm,arr[l])
                l+=1
            
        return re
