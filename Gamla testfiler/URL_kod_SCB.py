#import urllib library
from urllib.request import urlopen
import pandas as pd
import json
#url="https://api.scb.se/OV0104/v1/doris/sv/ssd/START/UF/UF0701/UF0701B/YHStudT1dN"
url="https://historical.api.jobtechdev.se/search?parttime.min=100&parttime.max=100&driving-license-required=false&driving-license=string&experience=false&unspecified-sweden-workplace=true&abroad=true&remote=true&open_for_all=true&trainee=false&larling=false&franchise=false&hire-work-place=false&offset=0&limit=50&request-timeout=300"
#store the response of url
response=urlopen(url)

data_json=json.loads(response.read())

print(data_json)

