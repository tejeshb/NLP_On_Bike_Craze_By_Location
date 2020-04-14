import wiki
from  geopy.geocoders import Nominatim
import geocoder
from geopy.distance import geodesic as dist
#wiki

print("Wiki page successfully extracted ... and imported")
print("Getting location details")

location = list(wiki.country_bike.keys())

location = [x.replace('_', ' ') for x in location]
location = location[:32]


geolocator = Nominatim(user_agent="bike_craze")
#city ="London"
loc = geolocator.geocode("India")
print( "location of india: ", "\nlatitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)

lat_lon = {}
from time import sleep

#getting lat_lon of countries in wikipedia page

for place in location:
    #print(place)
    sleep(0.5)
    loc = geolocator.geocode(place)
    lat_lon[place] = (loc.latitude,loc.longitude)
    #print("okay")

#getting your location based on ip address

g = geocoder.ip('me')
c = geolocator.reverse((g.latlng))
print("your location: " + str(c.raw['address']['country']))
loc = geolocator.geocode(c.raw['address']['country'])
my_loc = tuple(g.latlng)

#calculating nearest country in wikipedia page to your country

print("calculating nearest country in wikipedia page to your country")

distances = {}

for loc,coord in lat_lon.items():
    sleep(1)
    distance =  dist(coord,my_loc).km
    distances[loc] = distance

x =min(distances.values())

your_place = ""
for name, d in distances.items():
    if d == x:
        print("nearest country: " ,name)
        your_location = name.replace(" ","_")
        your_place = name

