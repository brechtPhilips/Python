import pandas
from geopy.geocoders import Nominatim

df = pandas.read_csv("http://pythonhow.com/supermarkets.csv")

# create a nominatim variable must set scheme to http
geolocator = Nominatim(scheme="http")

# get the location of the adress
location = geolocator.geocode("3666 21st St,San Francisco, CA 94114, USA ")
# print latitude and longitude
# print(location.latitude, location.longitude)

# modifying a colum to the database
df["Address"] = df["Address"] + "," + df["City"] + "," + df["State"] + "," + df["Country"]

# adding a colum to the database
df["Coordinates"] = df["Address"].apply(geolocator.geocode)
df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x is not None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x is not None else None)
print(df)
