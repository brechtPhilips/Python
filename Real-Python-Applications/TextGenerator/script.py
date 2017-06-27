import random,string

'''
Generating random letters
'''


def generator():
    letter_one = random.choice(string.ascii_letters)
    letter_two = random.choice(string.ascii_letters)
    letter_three = random.choice(string.ascii_letters)
    name = letter_one+letter_two+letter_three
    return name

print(generator())