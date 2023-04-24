from geopy import geocoders
from geopy.geocoders import Nominatim

gn = geocoders.GeoNames(username='Hitchinghobo')

geolocator = Nominatim(user_agent="geocode_test.py")
location = geolocator.geocode("Göteborg")


print(location.latitude, location.longitude)

from CSV_extractor import city_count

dict_long = {}
dict_lat = {}

for i in city_count:
    
    location = geolocator.geocode(i)
    dict_long[i] = location.longitude
    dict_lat[i] = location.latitude

print(city_count)
print(dict_long)
print(dict_lat)