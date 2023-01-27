from operator import itemgetter
tupple=[("Tom",19,80),("John",20,90),("Jony",17,91),("Jony",17,93),("Json",21,85)]
tupple.sort(key=itemgetter(0,1,2))
print(tupple)
