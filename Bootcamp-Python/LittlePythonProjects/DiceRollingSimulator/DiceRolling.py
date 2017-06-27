import random
import sys


def roll():
    while True:
        answer = input("Do you wanne roll? Y/n \n> ".lower())

        if answer == "y":
            number = random.randrange(1, 7)
            print("It's number : {}".format(number))
        else:
            print("--Goodbye--")
            sys.exit()


roll()
