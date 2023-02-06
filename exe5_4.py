window_len= int(input("Enter window length: "))
strides = int(input("Enter strides: "))
sample_arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
res = []
size = len(sample_arr)
# print(list(range(0, size-window_len,strides)))
for i in range(0, size-window_len,strides):
  res.append(sample_arr[i : (i+window_len)])
print(res)
