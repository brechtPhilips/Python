# Create a dictionary that contains the keys a  and b
# and their respective values 1  and 2

dic_one = {'a':1,'b':2}

# OR

dic_two = dict(a=1, b=2)

# Ex16-Printing out the value of the keys
print(dic_one['a'])
print(dic_one['b'])


# Ex17-Calculate the sum of the values
print(dic_one['a']+dic_one['b'])

# Ex19-Adding na new pair of keys and values to a dictionary
# Refer to c(the key) and set it's value
dic_one['c'] = 3
print(dic_one)

#Ex20-Calculate the sum of all the values
d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))

#Ex 21- Dictionary Filtering
# Filter the dictionary by removing all items with a value of greater than 1.
d = dict((key,value) for key,value in d.items() if value <= 1)
print(d)
