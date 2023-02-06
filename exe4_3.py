import sys
import numpy as np
from datetime import datetime
from dateutil.relativedelta import relativedelta as rel



dates=["2009-02-11","1994-02-01","2001-02-01","2011-02-01","2003-11-01","1997-02-01","2004-05-11","2013-02-01","2022-02-01","2011-02-01"]

dates=[datetime.fromisoformat(date) for date in dates] #list comprehension in python 
sz=len(dates)
labels=["No Label"]*sz

# print(dates)

today=datetime.fromisoformat("2023-01-30")

dif=[rel(today,date) for date in dates]
# for _ in dif:
#     print(_.years)

for i in range(sz):
    agein_year=dif[i].years
    
    if(agein_year==18):
        labels[i]="First"
    if(agein_year==19):
        labels[i]="Second"
    if(agein_year==20):
        labels[i]="Third"
    if(agein_year==21):
        labels[i]="Fourth"

for i in range(sz):
    print(dates[i],"  age:",dif[i].years,end="  ")
    print(labels[i])
