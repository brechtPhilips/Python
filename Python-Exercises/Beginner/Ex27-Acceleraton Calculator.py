# Create a function that calculates acceleration given
# initial velocity v1, final velocity v2, start time t1, and end time t2

def CalculateAcceleration(v1,v2,t1,t2):
    a=(v2-v1)/(t2-t1)
    print(a)


CalculateAcceleration(0,10,0,20)