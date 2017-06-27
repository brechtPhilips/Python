import numpy

# create numpy object , n is an array
n = numpy.arange(27)
print("Array")
print(n)
print("\n")

# reshape to a 2 dimensional array
n = n.reshape(3,9)
print("2 Dimensional Array")
print(n)
print("\n")

# reshape to a 3 dimensional array
n = n.reshape(3,3,3)
print("3 Dimensional Array")
print(n)
print("\n")
