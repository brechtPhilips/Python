#Print out hello every 2 seconds
#program prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, 4,
# and so on the interval increases between prints.
import time
def PrintHello():
    i = 0
    while True:
        print("Hello")
        #time.sleep(2)
        i += 1
        if i == 10:
            print("end of loop")
            break
        time.sleep(i)

PrintHello()