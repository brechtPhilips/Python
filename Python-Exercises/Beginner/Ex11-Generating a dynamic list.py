# Create the dynamic list filled 1 to 20
numbers = range(1,21)

# Print the list
print(list(numbers))



# Ex12-take the list but multiply the outcome

print([10 * x for x in numbers])

# Ex13-Set the output to strings
# Used map to set every item in the list to a string!
print(list(map(str,numbers)))