import folium
import pandas


'''Read the csv file'''
df = pandas.read_csv("zipcodes.csv")


'''Variables'''
minimum = int(min(df["zip"]))
maximum = int(max(df["zip"]))
step = int((maximum-minimum)/3)

'''Definitions'''
def color(zipcode):
    if zipcode in range(minimum,minimum+step):
        return "orange"
    elif zipcode in range(minimum+step, minimum+step*2):
        return "blue"
    else:
        return "green"

'''create a map object'''
mapi = folium.Map(location=[df["lat"].mean(), df["lng"].mean()],
                  zoom_start=10, tiles="Stamen Terrain")

'''Create a cluster of markers'''
cluster_marker = folium.MarkerCluster("Villages").add_to(mapi)


'''Create markers with a csv file and a for loop'''
for lat, lon, name, zipcode in zip(df["lat"], df["lng"], df["city"], df["zip"]):

    '''Create simple markers on the map'''
    folium.Marker(location=[lat, lon], popup="{}\n{}".format(name, zipcode),
                  icon=folium.Icon(
                      color=color(zipcode),
                      icon='star'
                  )).add_to(cluster_marker)


'''Save map object to an html file'''
mapi.save(outfile="Limburg.html")
