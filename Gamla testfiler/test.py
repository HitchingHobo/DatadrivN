import pandas as pd

data = pd.read_csv('utvecklare_lista.csv', encoding=('UTF8'), nrows=10)

data.info()

for i in data['occupation.label']:
    data['description.text'] = data['description.text'].str.lower()

print(data['description.text'])