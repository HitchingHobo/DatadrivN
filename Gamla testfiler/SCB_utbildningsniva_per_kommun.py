#import urllib library
from urllib.request import urlopen
import pandas as pd
import json
url="https://api.scb.se/OV0104/v1/doris/sv/ssd/START/UF/UF0506/UF0506B/Utbildning"
#store the response of url
response=urlopen(url)

data_json=json.loads(response.read())

print(data_json)

