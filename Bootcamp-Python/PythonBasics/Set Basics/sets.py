COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


test_set = {1, 2, 3}
print(test_set)
#add one new data
test_set.add(4)

#add multiple data
test_set.update({5,6},{0,7})
print(test_set)
#remove data
test_set.remove(4)
print(test_set)

#use discard methode to remove items it won't give you an error if the value is not there
test_set.discard(8)
test_set.discard(7)
print(test_set)

set1 = set(range(11))
set2= {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}


#Sets data is always unique!!


# Get all of the items from both sets with function or operators
#function
print(set1.union(set2))
#operators
print(set1 | set2)

# Get all of the items in the FIRST set that are NOT shared in de second set
#function
print(set1.difference(set2))
#operator
print(set1 - set2)

# Get all the common items between the sets
#function
print(set1.intersection(set2))
#operator
print(set1 & set2)

# Get all of the items that are Not shared between sets
#functions
print(set1.symmetric_difference(set2))
#operator
print(set1 ^set2)
print()
print()
#sets testing
name1 = set("brecht")
name2 = set("sanne")
print("alle the items from both sets")
print(name1 | name2)
print("different items in name One")
print(name1 - name2)
print("different items in name Two")
print(name2 - name1)
print("alle the common items from set One and Two")
print(name1 & name2)
print("alle the items that are not shared between nameOne and nameTwo")
print(name1 ^ name2)


def covers(courses):
    new_list = []

    for key,value in COURSES.items():
        if value & courses:
            new_list.append(key)
    print( new_list)


def covers_all(courses):
    new_list = []

    for key, value in COURSES.items():
        #Test whether every element in courses is in the value set.
        if value.issuperset(courses):
            new_list.append(key)
    print(new_list)

covers({'Ruby'})
covers_all({"conditions", "input"})
