psss=[".",",","?","!"]

def reverseword(str):
    l=len(str)
    i=1
    j=len(str) - 3  
    k=j-1 
    if str[l-1] in psss:




        while(i<j):



            temp=str[i]
            str[i]=str[j]
            str[j]=temp
            i +=1
            j -=1
        return "".join(str)
    else:
        while(i<k):
            temp1=str[i]  
            str[i]=str[k]
            str[k]=temp1
            i +=1
            k-=1
        return "".join(str)    
def reversewords(str):
    str=str.split()

    for i in str:
        j=[h for h in i]           #make a list of ith word from the str
                # print (j)
        print(reverseword(j), end= "  ")
str=input("enter string ")
reversewords(str) 




