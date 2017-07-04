from pprint import pprint

d=dict(a=list(range(1,11)),b=list(range(11,21)),c=list(range(21,31)))
pprint(d)

#Ex23-Multilevel Indexing
# Access the third value of key b  from the dictionary.
print(d['b'][2])

#Ex24-Iterate Dictionary
for key,value in d.items():
    print(key, "has value", value)