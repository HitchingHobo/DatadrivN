import pandas as pd

data = pd.read_csv('utvecklare_lista.csv', encoding=('UTF8'), nrows=100)

data.info()

print(data['employer.name'])