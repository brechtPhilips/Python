# Functions in python

def hows_the_parrot():
    print("He's pining for the fjords!")


# Calling a function
hows_the_parrot()
print(""
      "")


def lumberjack(name):
    if name.lower() == "jef":
        print("{} is a lumber and he's ok".format(name))
    else:
        print("{} sleeps all night and {} works all day!".format(name, name))


lumberjack("jef")
lumberjack("fons")


def lumberjack(name, pronoun):
    print("{} sleeps all night and {} OK!".format(name, pronoun))


lumberjack("fons", "he's")
lumberjack("sara", "she's")


def average(num1, num2):
    return (num1 + num2) / 2


getal = average(2, 4)
print(getal)
