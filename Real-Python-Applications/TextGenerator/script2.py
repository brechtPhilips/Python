import random,string

'''
Generating random letters
'''
vowels = "aeiouy"
consonants="zrtypqsdfghjklmwxcvbn"
letter_input_one = input("What letter do you want?\n"
                         "Enter 'v' for vowels, 'c' for consonants and 'l' for any letter: ")
letter_input_two = input("What letter do you want?\n"
                         "Enter 'v' for vowels, 'c' for consonants and 'l' for any letter: ")
letter_input_three = input("What letter do you want?\n"
                           "Enter 'v' for vowels, 'c' for consonants and 'l' for any letter: ")


def generator():
    if letter_input_one == 'v':
        letter_one = random.choice(vowels)
    elif letter_input_one == 'c':
        letter_one = random.choice(consonants)
    elif letter_input_one == 'l' :
        letter_one = random.choice(string.ascii_letters)
    else:
        letter_one = letter_input_one

    if letter_input_two == 'v':
        letter_two = random.choice(vowels)
    elif letter_input_two == 'c':
        letter_two = random.choice(consonants)
    elif letter_input_two == 'l' :
        letter_two = random.choice(string.ascii_letters)
    else:
        letter_two = letter_input_two

    if letter_input_three == 'v':
        letter_three = random.choice(vowels)
    elif letter_input_three == 'c':
        letter_three = random.choice(consonants)
    elif letter_input_three == 'l' :
        letter_three = random.choice(string.ascii_letters)
    else:
        letter_three = letter_input_three
    name = letter_one+letter_two+letter_three
    return name

for i in range(20):
    print(generator())