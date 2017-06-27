# Naming Variables

# python chooses the right variable

favorite_fruit = "apple"
favorite_number = 42

print(favorite_fruit)

print(favorite_number / 4)

# String editing
# use \if you want to ignore e sign like ' or "..
name = "brecht "
last_name = "philips"
full_name = name + last_name
print(full_name)
# Error you can't add a string with an integer
# print "a"+ 5
print('a' + str(5))
# format strings
status_message = "Hey we have {} people using the site right now"
print(status_message.format(favorite_fruit))

# List,arrays...

my_list = [1, 2, 3, 4]
# add a single item to a list
my_list.append(5)
print(my_list)
# add multiple items to a list
my_list.extend([6, 7, 8, 9])
print(my_list)

name_list = "fons;jef;karel".split(";")
print(name_list)

names = "The names are :{}".format(", ".join(name_list))
print(names)

alpha = 'abcade'
print(alpha.index('a'))
aplha_list = list(alpha)
print(alpha.index('ca'))

# Booleans true or false
# empty variables are false
print(bool(""))
# variables with data are true
print(bool("1"))
print(5 != 5)

# if-else statements
a = 8
b = 10

if a < b:
    print("A is tiny!")
elif a == b:
    print("They are equal")
else:
    print("A is bigger")

# IN keyword checks if something is in another item,to make it negative place NOT before in
if "cheese" in "cheeseshop":
    print(True)

days_open = ['Monday', 'Tuesday', 'Wednesday', 'Thursday']
today = 'Tuesday'

if today in days_open:
    print("Come on in")
else:
    print("Sorry we are closed")

# Loops For and while
numbers = [1, 2, 3, 4, 5, 6]
doubles = []

for number in numbers:
    doubles.append(number * 2)

print(doubles)
number = 4
while number > 2:
    print("still looping")
    number -= 1

hellos = [
    "Hello",
    "Tungjatjeta",
]
for hello in hellos:
    print("{} World".format(hello))

# Getting information from users "input"

age = int(input("What's your age? "))

print(age + 1)
