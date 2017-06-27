a = 5
b = 20

# swap variables values
# unpacking
a, b = b, a
print(a, b)

c = b, a
print(c)


# packing
# base takes the first argument, args takes everything after that
def add(base, *args):
    total = base
    for num in args:
        total += num
    print(total)


add(5, 5)
add(32)
# enumerate makes tupples with indexe's
for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print("{}: {}".format(index + 1, letter))


def stringcases(a_string):
    tuple_string = (a_string.upper(), a_string.lower(), a_string.title(), a_string[::-1])
    return tuple_string


print(stringcases("brecht"))


def combo(listOne, listTwo):
    result_list = []
    for index, item in enumerate(listOne):
        for indexx, itemm in enumerate(listTwo):
            if index == indexx:
                result_list.append((item, itemm))

    print(result_list)


combo([1, 2, 3], 'abc')
