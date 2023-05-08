import pandas as pd

# read_csv function which is used to read the required CSV file
data = pd.read_csv('jobtech_temp2022Rall_UPDATED.csv', encoding=('UTF8'))
data = data['id']

print(data.head(4))