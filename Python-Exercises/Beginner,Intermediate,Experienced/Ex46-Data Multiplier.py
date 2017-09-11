import pandas
#Get the data from the site and create a dataframe
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = data * 2
data2.to_csv("Files/sampledata_x_2.txt",index=None)

#Concatenator
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data1 = pandas.read_csv("Files/sampledata_x_2.txt")

data3 = pandas.concat([data,data1])

data3.to_csv("Files/concatenate2datatables.txt",index=None)
