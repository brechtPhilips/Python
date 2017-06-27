import os
import sys

from TextBasedGameAdventure.Pages import *

ingame_answer = ""


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def play_again():
    if input("Do you wanne play again? Y/n\n> ".lower()) == 'y':
        clear_screen()
        play()
    else:
        sys.exit()


def play():
    clear_screen()
    name = input("Welcome please fill in your name : \n >>")
    clear_screen()
    print(get_beginning_page(name.lower()))
    answer = input("> ")

    if answer.lower() == 'y':
        print(get_room(2))
        print("-" * 10)
        answer = input("Do you want to explore the walk? Y/n \n>")
        if answer.lower() == 'y':
            print(get_room(3))
            ingame_answer = input("> ")
            if ingame_answer.lower() == "run":
                print(get_room(5))
            else:
                print(get_room(6))
        else:
            print(get_room(4))
            clear_screen()
            play_again()
    else:
        clear_screen()
        play_again()


play()
