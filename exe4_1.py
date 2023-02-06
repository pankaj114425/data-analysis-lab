import numpy as np

def check_zeroes(a):
    for i in a:
        if i==0:
            return True
    else:
            return False    


print("enter the number of element in array")
n= int(input())
print("enter",n ,"elements")
lst=[]
for i in range(0,n):
    x=int(input())
    lst.append(x)
a=np.array(lst)
ans=check_zeroes(a)
if ans:
    print("zeroes in array")
else:
    print("no zeroes in array")
