from datetime import datetime as dt

def CalculateBirthYear(age):
    currentYear = dt.now().year
    birthYear = currentYear - age
    print("You were born in %s"%(birthYear))



CalculateBirthYear(int(input("Enter your age: ")))