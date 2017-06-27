import pandas


df1=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["price","age","value"],index=["First","Second"])
df2=pandas.DataFrame([{"Name":"John"},{"Name":"Jack"}])

print(df1)
print(df2)

print(df1.price)
print(df2.Name)
# load in a csv file from an url
df3 = pandas.read_csv("http://pythonhow.com/supermarkets.csv")
df3 = df3.set_index("ID")
print(df3)
# Print selected Cells
print(df3.loc[1: 4, "Country":"Name"])

# Database accesing based on indexing use iloc most commen way
print(df3.iloc[1,:3])

print(df3.ix[1,4])
