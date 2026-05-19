ar=[0,1,2,0,3,0,0]
arr=[0,0,3,0,6,0,7]
j=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1
print(arr)
        
