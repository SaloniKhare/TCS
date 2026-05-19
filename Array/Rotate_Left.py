ar=[0,1,2,0,3,0,0]
arr=[1,2,3,4,5,6,7]
k=3
if k>len(arr):
        print(-1)
arr[:k]=arr[:k][::-1]
arr[k:]=arr[k:][::-1]
arr.reverse()
print(arr)
        
