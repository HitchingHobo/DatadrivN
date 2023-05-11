import pandas as pd
import csv


data = pd.read_csv('jobtech_temp2022Rall_UPDATED.csv', 
                   encoding=('UTF8'),
                   nrows=10000)
# data = data[['id', 'description.text', 'employer.name']]
data.info()
# data = pd.read_csv('jobtech_dataset2022.csv', encoding=('UTF8'), nrows=100)
# data = data[['id', 'description', 'employer']]
pd.set_option('display.max_colwidth', None)
data = data[ (data['occupation.label'].str.contains('Systemutvecklare|Mjukvaruutvecklare', na=False))]
# print(data[['occupation.label', 'employer.name', 'id', 'headline', 'access', 'experience_required', 'description.text', 'description.text_formatted', 'description.company_information', 'description.needs', 'description.requirements', 'employment_type.concept_id', 'employment_type.label', 'scope_of_work.min', 'scope_of_work.max', 'employer.organization_number', 'employer.name', 'employer.workplace', 'occupation.label', 'occupation_group.label', ]])

import csv

column_name = ["Titlar"] #The name of the columns

data.to_csv('utvecklare_lista.csv', 
            columns=['occupation.label', 
                     'employer.name',
                     'description.text'
                     ],
                     encoding=('UTF8'))

# with open('Utvecklare_lista.csv', 'a', encoding="UTF8") as f:
#     writer = csv.writer(f) #this is the writer object
#     writer.writerow(column_name) # this will list out the names of the columns which are always the first entrries
#     writer.writerow(data ['occupation.label' ]) #this is the data
#     writer.writerow(data ['employer.name' ]) #this is the data
#     writer.writerow(data ['description.text' ]) #this is the data