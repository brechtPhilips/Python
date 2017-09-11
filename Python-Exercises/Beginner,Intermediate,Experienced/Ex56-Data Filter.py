import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("Files/countries-by-area.txt")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density",ascending=False)

for index, row in data[:5].iterrows():
    print(row["country"])
