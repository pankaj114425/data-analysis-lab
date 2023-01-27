def if_sublist(x,y):
    sub_list=False
    if y== []:
        sub_list=True
    elif y == x:
        sub_list=True
    elif len(y) > len(x):
        sub_list=False
    else:
        for i in range(len(x)):
            if x[i]==y[0]:
                n = 1
                while (n < len(y)) and (x[i+n] ==y[n]):
                    n += 1
                if n == len(y):
                    sub_list = True    
    return sub_list   

l1=[5,6,3,8,7]
l2=[4,5,7]
l3=[3,8]
print(if_sublist(l1,l2))
print(if_sublist(l1,l3))
