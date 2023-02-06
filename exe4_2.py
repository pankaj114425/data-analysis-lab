import numpy as np

def median(marks):
    marks.sort()
    n = len(marks)
    m = n//2
    if n % 2 == 0:
        median = (marks[m-1] + marks[m]) / 2
    else:
        median = marks[m]
    return median

def mean(marks):
    return sum(marks) / len(marks)

lst = [30, 40, 55, 60, 65, 20, 28, 80, 81, 90, 95]
marks=np.array(lst)
passing_marks = [mark for mark in marks if mark >= 40]

median = median(passing_marks)
mean = mean(passing_marks)

print("Median:", median)
print("Mean:", mean)
