import pandas as pd


data = pd.read_csv('jobtech_temp2022Rall_UPDATED.csv', 
                   encoding=('UTF8'), 
                   nrows=356000)

# data = data[['id', 'description.text', 'employer.name']]
data.info()
# data = pd.read_csv('jobtech_dataset2022.csv', encoding=('UTF8'), nrows=100)
# data = data[['id', 'description', 'employer']]
pd.set_option('display.max_colwidth', None)

data = data[ (data['occupation.label'].str.contains('utvecklare', na=False))]
print(data[['occupation.label', 'employer.name']])




import csv

column_name = ["Titlar"] #The name of the columns

with open('Utvecklare_lista.csv', 'a', encoding="UTF8") as f:
    writer = csv.writer(f) #this is the writer object
    writer.writerow(column_name) # this will list out the names of the columns which are always the first entrries
    writer.writerow(data['occupation.label']) #this is the data
# print(data.info)
# print(data.columns)

# search for 'utvecklare' in description in dataframe





#data.to_csv('rensad_2022.csv', encoding=('UTF8'))

# with open("rensad_2022.csv", "w", encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(data.columns)
#     for row in data:
#         writer.writerow(row)