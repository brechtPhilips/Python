import os
import random
import sys

words = []


def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def fill_word_list():
    # make a list of words
    f = open("words.txt", 'r')

    line = f.readline()
    temp_word= line.split(',')

    for word in temp_word:
        words.append(word)

    welcome()


def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print("Strikes : {}/{}".format(len(bad_guesses), (len(secret_word) / 2)))
    print("")

    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')

    # draw guessed letters , strikes and spaces for the letters
    for letter in secret_word:
        if letter in good_guesses:
            # end print different letters on the same line
            print(letter, end='')
        else:
            print('_', end='')
    print('')


def get_guess(guesses):
    while True:
        # take guess
        guess = input("Guess a letter : ").lower()
        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in guesses:
            print("You've already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess


def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses = set()
    good_guesses = set()
    word_set = set(secret_word)

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses | good_guesses)

        if guess in word_set:
            good_guesses.add(guess)
            if not word_set.symmetric_difference(good_guesses):
                print("You Win!")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.add(guess)
            if len(bad_guesses) == (len(secret_word) / 2).__round__():
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True

        if done:
            play_aigain = input("Play again. Y/n").lower()
            if play_aigain != 'n':
                return play(done=False)
            else:
                sys.exit(1)


def welcome():
    start = input("Press enter/return to start,or enter Q to quit")
    if start.lower() == 'q':
        print("Bye")
        sys.exit(1)
    else:
        return True


done = False





while True:
    fill_word_list()
    clear()
    play(done)
