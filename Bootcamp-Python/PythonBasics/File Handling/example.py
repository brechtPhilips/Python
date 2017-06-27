#Basic methods of file handeling
# r=read,w=write,a=append
# open a file r= read w = write
file = open("example", 'r')

# get content from file
content = file.read()
print(content)
# places the pointe back to the beginning of the file
file.seek(0)
# read the first line
content = file.readline()
#print(content)

# Close file
file.close()

# write to a file
file = open("example",'w+')
sentence = "writing to a file\n"
# Write one line to a file for more lines in 1 file use the append methode
file.write(sentence)
file.close()

# writing to a file with the append method a = append
file = open("example", 'a+')
for i in range(10):
    file.write("test\n")
file.close()


# using the with statement to open and close a file
with open("example",'a+') as file:
    file.write("using the with statement")