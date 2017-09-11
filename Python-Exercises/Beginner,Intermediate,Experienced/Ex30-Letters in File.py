import string

#Write a file with every letter of the alphabet in it.
def CreateAlphabet():
    with open("Files/alphabet.txt",'w') as file:
        for letter in string.ascii_letters.lower():
            file.write(letter+"\n")



CreateAlphabet()