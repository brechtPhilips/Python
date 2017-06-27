# learning to work with dictonaries
# you have a key(title) and a value(python collections)

course = {"title": "Python Collections", "teacher": {"first_name": "kenneth", "last_name": "love"}, "videos": 22}
# add a key and value to a dictonarie one at a time
print("add a key and value to a dictonarie one at a time")
course["newKey"] = "new Value"
print(course)
# delete a key and value from a dictonarie
print("delete a key and value from a dictonarie")
del course["newKey"]
print(course)
# for update you must give a new dictionarie to the method with yout values and keys
# update can be used to add multiple keys and values in one time
print("for update you must give a new dictionarie to the method with yout values and keys \n"
      "update can be used to add multiple keys and values in one time")
course.update({"job": "python teacher", "editor": "vim"})
print(course)

# Change a value
print("Change a value")
course["job"] = "student"
print(course)

# Packing and unpacking dictonaries
print("Packing dictonaries")


def packer(**kwargs):
    print(kwargs)


packer(name="Brecht", num=42, spanish_inquisition=None)


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name")


unpacker(**{"last_name": "Philips", "first_name": "Brecht"})

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]
template = "Hi, I'm {name} and I love to eat {food}!"


def string_factory(list_of_dictionaries):
    result_list = []

    for dictonary in list_of_dictionaries:
        result_list.append(template.format(**dictonary))

    return result_list


string_factory(dicts)


def word_count(a_string):
    string_dict = {}
    sentence_list = a_string.lower().split()
    for word in sentence_list:
        if word in string_dict:
            string_dict[word] += 1
        else:
            string_dict[word] = 1
    print(string_dict)


word_count("I do not like it Sam I Am I I I I I I i i i")

dicts = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics', 'fons fons'],
         'Kenneth Love': ['Python Basics', 'Python Collections', 'Node.js Basics', 'Node.js Basics']}


def courses(dictionary):
    course_list = []
    for list in dictionary.values():
        for i in range(len(list)):
            course_list.append(list[i])
    print(course_list)


courses(dicts)


def most_courses(dictionary):
    count = 0
    teacher = ""
    for key in dictionary.keys():
        if len(dictionary[key]) > count:
            count = len(dictionary[key])
            teacher = key

    print(teacher)


most_courses(dicts)


def stats(dictionary):
    stats_list = []

    for item in dictionary.keys():
        stats_list.append([item, len(dictionary[item])])
    print(stats_list)


stats(dicts)
