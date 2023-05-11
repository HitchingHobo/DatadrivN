import pandas as pd
import csv
from langdetect import detect


data = pd.read_csv('jobtech_temp2022Rall_UPDATED.csv', 
                   encoding=('UTF8'))
# data = data[['id', 'description.text', 'employer.name']]
data.info()
# data = pd.read_csv('jobtech_dataset2022.csv', encoding=('UTF8'), nrows=100)
# data = data[['id', 'description', 'employer']]
pd.set_option('display.max_colwidth', None)
data = data[ (data['occupation.label'].str.contains('Systemutvecklare|Mjukvaruutvecklare|Backend-utvecklare|Frontend-utvecklare|Applikationsutvecklare|Databasutvecklare', na=False))]
# print(data[['occupation.label', 'employer.name', 'id', 'headline', 'access', 'experience_required', 'description.text', 'description.text_formatted', 'description.company_information', 'description.needs', 'description.requirements', 'employment_type.concept_id', 'employment_type.label', 'scope_of_work.min', 'scope_of_work.max', 'employer.organization_number', 'employer.name', 'employer.workplace', 'occupation.label', 'occupation_group.label', ]])


# column_name = ["Titlar"] #The name of the columns

data.to_csv('utvecklare_lista.csv', 
            columns=['occupation.label', 
                     'employer.name',
                     'description.text'
                     ],
                     encoding=('UTF8'))


def is_english(text):
    # This function returns True if the input text is in English, False otherwise.
    try:
        lang = detect(text)
        return lang == 'en'
    except:
        return False

def filter_csv(input_file, output_file):
    with open(input_file, 'r', encoding=('UTF8')) as f_in, open(output_file, 'w', newline='', encoding=('UTF8')) as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        for row in reader:
            if len(row) == 0:
                continue
            text = ' '.join(row).strip()
            if not is_english(text):
                writer.writerow(row)

# Example usage:
input_file = 'Utvecklare_lista.csv'
output_file = 'Utvecklare_lista_svenska.csv'
filter_csv(input_file, output_file)


# with open('Utvecklare_lista.csv', 'a', encoding="UTF8") as f:
#     writer = csv.writer(f) #this is the writer object
#     writer.writerow(column_name) # this will list out the names of the columns which are always the first entrries
#     writer.writerow(data ['occupation.label' ]) #this is the data
#     writer.writerow(data ['employer.name' ]) #this is the data
#     writer.writerow(data ['description.text' ]) #this is the data