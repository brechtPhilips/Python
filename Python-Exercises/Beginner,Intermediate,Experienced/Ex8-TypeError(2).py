# Why is there an error in the code and how would you fix it?

def foo(a, b):
    print(a+b)

x= foo(2, 3)*10

#This generates an typeError because the function doesn't return anything
# Sow the *10 can't be multiplied with a None type Object

# Solution

def faa(a, b):
    return a+b

x= faa(2, 3)*10
print(x)