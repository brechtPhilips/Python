#Please create a script that generates 26 text files named
# a.txt, b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename.
# So, a.txt will contain letter a, b.txt will contain letter b and so on.

import string,os

#Creating a directory if it doesn't exist
if not os.path.exists("Files/Ex34"):
    os.makedirs("Files/Ex34")

for letter in string.ascii_lowercase:
    with open("Files/Ex34/"+ letter +".txt","w") as file:
        file.write(letter+"\n")