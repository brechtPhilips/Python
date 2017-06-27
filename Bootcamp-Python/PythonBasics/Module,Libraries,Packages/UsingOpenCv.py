import cv2
import numpy

# Read the image and store the data in a numpy array 0 is read in gray and 1 is read in BRG
gray_image_array = cv2.imread("smallgray.png",0)
print(gray_image_array)
print()
# make an image of a fill numpy array
cv2.imwrite("newsmallgray.png",gray_image_array)

# indexing in a numpy array
print(gray_image_array[2,4])
print(gray_image_array[0:2])
print(gray_image_array[0:2,2:4])
print(gray_image_array.shape)
print()
print("Iterating threw a numpy array")
# Iterating threw a numpy array
print()
print("Threw all the rows")
# Threw rows
for i in gray_image_array:
    print(i)
print()
print("Threw all the columns")
# Threw Columns
for i in gray_image_array.T:
    print(i)
print("Loop Threw all the values separate")
# Threw all the values separate
for j in gray_image_array.flat:
    print(j)

print()
print("Concatenate arrays with numpy.hstack")
# Concatenate numpy array or turn 1 big array to 2 smaller arrays
# place a tuple in the functions it only takes 1 parameter
big_array = numpy.vstack((gray_image_array,gray_image_array))
print(big_array)
print()
# Splitting an array in to mulitple arrays
print("Splitting an array in to mulitple arrays")
small_array_list = numpy.split(big_array,3)
print(small_array_list)

