import pandas as pd
import csv


data = pd.read_csv('jobtech_temp2022Rall_UPDATED.csv', 
                   encoding=('UTF8'), 
                   nrows=100)
# data = data[['id', 'description.text', 'employer.name']]

# data = pd.read_csv('jobtech_dataset2022.csv', encoding=('UTF8'), nrows=100)
# data = data[['id', 'description', 'employer']]
pd.set_option('display.max_colwidth', None)
data = data[ (data['description.text'].str.contains('utvecklare'))]
print(data[['description.text', 'employer.name']])

# print(data.info)
# print(data.columns)

# search for 'utvecklare' in description in dataframe






#data.to_csv('rensad_2022.csv', encoding=('UTF8'))

# with open("rensad_2022.csv", "w", encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(data.columns)
#     for row in data:
#         writer.writerow(row)
