import requests
from pprint import pprint

#Print out the text of this file http://www.pythonhow.com/data/universe.txt.
# Please don't manually download the file. Let Python do all the work.
r = requests.get("http://www.pythonhow.com/data/universe.txt")

pprint(r.text)

#Count the number of "a" characters in this text file
# : http://www.pythonhow.com/data/universe.txt

r = requests.get("http://www.pythonhow.com/data/universe.txt")
print(r.text.count('a'))