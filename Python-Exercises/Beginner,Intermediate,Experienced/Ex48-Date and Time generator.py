from datetime import datetime as dt
#strftime = string from time
#%A=weekday,%B=month,%d=date,%y=year
def ShowTodaysDate():
    print(dt.now().strftime("Today is %A, %B %d,%Y"))

ShowTodaysDate()