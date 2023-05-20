import pandas as pd


pd.set_option('display.max_rows', None)
data=pd.read_csv('KMEANS_output.csv', 
                 encoding=('UTF8'),
                 nrows=100)

data=data[['cluster_label', 'employer.name']]
data.sort_values(by=['employer.name'], inplace=True)
print(data)
