#Use Python to calculate the distance in kilometers
# between Jupiter and Sun on January 1, 1230.
from datetime import datetime as dt
import ephem



def PrintDistanceToPlanets():
    print("Distance to the sun")
    jupiter = ephem.Jupiter()
    jupiter.compute(dt.now())
    distance_au_units = jupiter.sun_distance
    distance_km = distance_au_units * 149597870.691
    print("Jupiter: " + str(round(distance_km,4)))

    moon = ephem.Moon()
    moon.compute(dt.now())
    distance_au_units = moon.sun_distance
    distance_km = distance_au_units * 149597870.691
    print("Moon: " + str(round(distance_km,4))+"\n")

    #next full moon
    fullmoon = ephem.next_full_moon(dt.now())
    print("Time of next full moon")
    print(fullmoon)

PrintDistanceToPlanets()