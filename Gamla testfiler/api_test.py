import pandas as pd
import json
from urllib.request import urlopen


with urlopen("https://jobsearch.api.jobtechdev.se/search?q=distans&offset=0&limit=10") as webpage: # webpage is just a variable 
   
    #read JSON file & extract data  
    data = json.loads(webpage.read().decode()) 
   
    print(data)


