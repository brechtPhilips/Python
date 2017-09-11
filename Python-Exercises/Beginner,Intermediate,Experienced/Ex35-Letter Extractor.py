# write a script that extraxt letters from the 26 text files
#  and put the letters in to a list

import glob

letters = []
file_list = glob.glob("Files/Ex34/*.txt")

for filename in file_list:
    with open(filename,'r') as file:
        letters.append(file.read().strip("\n"))

print(letters)