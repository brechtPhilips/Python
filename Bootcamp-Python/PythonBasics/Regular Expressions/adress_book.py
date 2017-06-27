import re

# set reference to the file
names_file = open("names.txt", encoding="utf-8")

# read from the file
data = names_file.read()

# close the reference to the file
names_file.close()

# regex expressions
###
# match matches in the beginning of the string(first word)//(r tells python it's a raw string)
# print(re.match(r'Love',data))
# search--matches for the word somewhere in the string
# print(re.search(r'Kenneth',data))

# \d search for a number -- \D search for anything that isn't a number
print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
print("\n")
print(re.findall(r'\w*, \w+', data))

# Sets in regex expressions [] is the set the + sign after the sets is how many times something in the set can be set
print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
print(re.findall(r'\b[threous]{9}\b', data, re.I))

# Negations: Negated sets let us specify characters and sequences that should be left out of any matches.
# VEBOSE lag that allows regular expressions to span multiple lines and contain (ignored) whitespace and comments.
print(re.findall(r'''
    \b@[-\w\d.]* # First a word boundary, an @, and then any number of characters
    [^gov\t]+ # Ignore 1+ instances of the letters 'g','o', or 'v' and a tab
    \b # Match another word boundary
    ''', data, re.VERBOSE | re.I))

print(re.findall(r"""
    \b[-\w]+, #Find a word boundary, 1+ hyphens or characters and a ,
    \s # find 1 white space
    [-\w ]+ # 1+ hpyhens and characters and explicit spaces
    [^\t\n] # Ignore tabs and newlines
""", data, re.X))
# Making groups () you can later access for example a group for names,phonenumbers,jobs..
# Compile method to pre-compile and save a regular expression pattern, and any associated flags, for later use.
line = re.compile(r'''
    (?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #Phone number
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? #Job and company's
    (?P<twitter>@[\w\d]+)?$ #Twitter
''', re.X | re.MULTILINE)

print()
print(re.search(line, data).groupdict())
print()
print(line.search(data).groupdict())

print("-" * 100)


class Player:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return "Name: {}\nLastname: {}\nEmail: {}".format(self.first_name, self.last_name, self.email)


# finditter method to generate an iterable from the non-overlapping matches of a regular expression. Very handy for for loops.
for match in line.finditer(data):
    # print('{first} {last} <{email}>'.format(**match.groupdict()))
    player = Player(match.group('first'), match.group('last'), match.group('email'))
    print(player)
    print("-" * 100)
