import random
import sys


def play_again():
    answer = input("Do you wnt to play again? Y/n ")
    if answer.lower() == 'y':
        play()
    else:
        sys.exit()


def play():
    number = random.randrange(0, 100, 1)
    while True:
        print("Guess the number between 0 and 100!")
        try:
            guessed_number = int(input("> "))

            if guessed_number == number:
                print("You have guessed the number, the number was {}".format(number))
                break
            elif guessed_number < number:
                print("To bad the number is higher than your guess")
            else:
                print("To bad the number is lower than your guess number")
        except ValueError:
            print("Pleas fill in a number!")
            continue
    play_again()


play()
