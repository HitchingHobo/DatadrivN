import pandas as pd
import json
from urllib.request import urlopen

with urlopen ("https://jobsearch.api.jobtechdev.se/search?q=distans&offset=0&limit=10") as webpage: 
    data=json.loads(webpage.read().decode())
print(data)
    #df=pd.DataFrame(data["results"])


