#plot the data of this file into a graph of x and y axis.

import matplotlib.pyplot as plt
import pandas


data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
plt.scatter(data["x"],data["y"], linestyle="r-")
plt.autoscale(enable=True)
plt.show()
