# Exceptions (try,expect)
try:
    count = int(input("Give me a number "))
except NameError:
    print("That's not a number!")
else:
    print("Hi " * count)


def add(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Oops")
    else:
        print(num1 + num2)


add(2, 3)
