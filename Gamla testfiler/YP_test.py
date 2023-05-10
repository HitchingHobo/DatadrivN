import pandas as pd  
  
# read_csv function which is used to read the required CSV file
data = pd.read_csv('YP_med_texter.csv')
  
# drop function which is used in removing or deleting rows or columns from the CSV files
data.drop('concept_id', inplace=True, axis=1)
#data.drop('ar', inplace=True, axis=1)
data.drop('datatyp', inplace=True, axis=1)
data.drop('ssyk', inplace=True, axis=1)
data.drop('geografi', inplace=True, axis=1)
data.drop('stycke3', inplace=True, axis=1)


data = data[ (data['ar'] == 2022)]


data = data.rename({'ingress':'Procent', 'stycke1':'Jobbmöjlighet', 'stycke2':'5 års sikt'}, axis='columns')

print(data.head(4))

