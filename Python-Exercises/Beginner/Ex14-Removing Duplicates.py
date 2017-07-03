# Complete the script so that it removes duplicate items from list a

a = ["1",1,"1",2]

# Converting the list to a set removes the duplicates of the same type
# Converting it back to a list gives you back a list

print(list(set(a)))


# An Other solution would be
b = []

for i in a:
    if i not in b:
        b.append(i)

print(b)