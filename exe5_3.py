import numpy as np
arr=np.array([1, 3, 7, 1, 2, 6, 0, 1])
l=[]
for i in range(arr.size-1):
    if(i!=0):
        if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
            l.append(i)


print(l)
