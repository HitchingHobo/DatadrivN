import pandas as pd
import csv
from langdetect import detect


data = pd.read_csv('jobtech_temp2022Rall_UPDATED.csv', 
                   encoding=('UTF8'))

data = data[ (data['occupation.label'].str.contains('Systemutvecklare|Mjukvaruutvecklare|Backend-utvecklare|Frontend-utvecklare|Applikationsutvecklare|Databasutvecklare', na=False))]

data.to_csv('utvecklare_lista.csv', 
            columns=['occupation.label', 
                     'employer.name',
                     'description.text'
                     ],
                     encoding=('UTF8'))


def is_english(text):

    try:
        lang = detect(text)
        return lang == 'en'
    except:
        return False

def filter_csv(input_file, output_file):
    x = 0
    with open(input_file, 'r', encoding=('UTF8')) as f_in, open(output_file, 'w', newline='', encoding=('UTF8')) as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)
        for row in reader:
            if len(row) == 0:
                continue
            text = ' '.join(row).strip()

            if not is_english(text):
                x += 1
                writer.writerow(row)


input_file = 'Utvecklare_lista.csv'
output_file = 'Utvecklare_lista_svenska.csv'
filter_csv(input_file, output_file)

