import random,string

import array

'''naming the vowels and consonants'''
vowels = "aeiou"
consonants="zrtypqsdfghjklmwxcvbny"
letter_pattern = list()

'''Greeting the user'''
def welcome():
    print("Welcome to baby name generator")

'''Defining the pattern that the user wants to use'''
def set_pattern(number):
    for i in range(number):
        letter_pattern.append(
            input("If you want a vowel type 'v', for constant press 'c' and for any letter press 'l': "))

    return letter_pattern

'''Looping over possible names'''
def set_times_to_loop(number):
    for i in range(number):
        generator(letter_pattern)

'''Let the pattern work'''
def generator(pattern):
    name =""
    for letter in pattern:
        if letter == 'v':
            name += random.choice(vowels)
        elif letter == 'c':
            name += random.choice(consonants)
        elif letter == 'l' :
            name += random.choice(string.ascii_letters)
        else:
            name += letter
    print(name)



welcome()
number = int(input("How many letters can the name have? :"))
set_pattern(number)
set_times_to_loop(int(input("How many times do you want to generate a name?: ")))
# reset the list
letter_pattern = list()
