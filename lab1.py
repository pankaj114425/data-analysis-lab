def reverseword(str):
     i=1
     j=len(str) - 2   
                                   
     while(i<j):
        temp=str[i]
        str[i]=str[j]
        str[j]=temp
        i +=1
        j -=1

     return "".join(str)
def reversewords(str):
    str=str.split()

    for i in str:
        j=[h for h in i]           #make a list of ith word from the str
                # print (j)
        print(reverseword(j), end= "  ")
str=input("enter string ")
reversewords(str)  




