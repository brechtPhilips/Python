# Executing the code will throw an error. Can you explain why?

a = 1
b = 2
print(a == b)
c = b
print(b == c)
# On line 6 we compare b to c but c is never defined!
# U can define c with the value of b by using the '=' sign
# example on line  6