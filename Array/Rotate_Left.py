ar=[0,1,2,0,3,0,0]
arr=[1,2,3,4,5,6,7]
k=3
arr[:3]=arr[:3][::-1]
arr[3:]=arr[3:][::-1]
arr.reverse()
print(arr)
        
