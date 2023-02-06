import numpy as np
arr=np.array([2, 3, 2, 2, 2, 1])
# print(arr.size)
encode_arr=np.zeros((arr.size,arr.max()))
for i in range (arr.size):

    encode_arr[i,arr[i]-1]=1


print(encode_arr)
