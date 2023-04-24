from geopy import geocoders
from geopy.geocoders import Nominatim

gn = geocoders.GeoNames(username='Hitchinghobo')

geolocator = Nominatim(user_agent="geocode_test.py")
location = geolocator.geocode("Göteborg")


print(location.latitude, location.longitude)