import os
import sys
import time


calculate_string=""

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def backspace(n):
    print('\r' * n,end =' ')


def bereken():
    print("Berekenen...")
    time.sleep(3)
    for i in range(101):  # for 0 to 100
        s = str(i) + '%'  # string for output
        print(s, end =' ')  # just print and flush
        backspace(len(s))  # back for n chars
        time.sleep(0.2)


def startGame():
    mol = input("Geef de naam van de mol in: ").lower()
    clear_screen()
    while True:
        suspect = input("Wie is de mol ? :").lower()
        clear_screen()
        if suspect == mol:
            bereken()
            print()
            print("U heeft de mol geraden!!!!")

            print("Opnieuw spelen ? Y/n :")
            answer = input("> ").lower()
            if answer == 'y':
                startGame()
            else:
                sys.exit(1)
        else:
            bereken()
            print()
            print("Helaas {} is niet de mol!!".format(suspect))
            print("Succes met zoeken!")

startGame()
