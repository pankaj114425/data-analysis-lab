lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
max_sum=0
list_max_sum=[]

def get_sum(x):

    sum=0
    for i in x:
        sum=sum+i
    return sum

for x in lists:
    lsum=get_sum(x)
    if lsum>max_sum:

        max_sum=lsum
        list_max_sum=x

print(list_max_sum)
