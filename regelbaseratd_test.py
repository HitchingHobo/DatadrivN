import pandas as pd
from nltk.corpus import stopwords

#pd.set_option('display.max_colwidth', None)

gen_data = pd.read_csv('Lista Mask. och Fem. ord.csv', 
                       encoding=('UTF8'))
gen_data.dropna(inplace=True)

mask_list = []
fem_list = []

## Sätter maskulina & feminina ord i listor
for row in gen_data['Maskulint kodade ord']:
    mask_list.append(row)
for row in gen_data['Masculinecoded words']:
    mask_list.append(row)    
for row in gen_data['Feminint kodade ord']:
    fem_list.append(row)
for row in gen_data['Femininecoded words']:
    fem_list.append(row)

## Importerar datan och preppar listor
data = pd.read_csv('utvecklare_lista.csv',
                    encoding=('UTF8'))

mask_word_list=[]
fem_word_list=[]
data['Mask_score'] = ''
data['Fem_score'] = ''
data['Mask_ord'] = ''
data['Fem_ord'] = ''
data['Annons_length'] = ''

## Sätter stopwords
stopwords_list = stopwords.words('swedish')
stopwords_list += stopwords.words('english')
stopwords_list.extend(['academic', 'work', 'the', 'tiqqe', 'även'])

## Huvudloop
for index in data.index:
    row = data['description.text'][index]
    row = str(row).lower()   
    mask_word_list=[]
    fem_word_list=[]
    x = 0
    for word in row.split():
        x += 1
        if word not in stopwords_list:
            for i in mask_list:
                if word.startswith(i):
                    mask_word_list.append(i) 
                    ##print(mask_word_list)
            for i in fem_list:
                if word.startswith(i):
                    fem_word_list.append(i)
                    ##print(fem_word_list)
        else:
            continue
    data['Mask_ord'][index] = mask_word_list
    data['Mask_score'][index] = len(mask_word_list)
    data['Fem_ord'][index] = fem_word_list
    data['Fem_score'][index] = len(fem_word_list)
    data['Annons_length'][index] = x



print(data[['employer.name', 'Mask_score', 'Fem_score', 'Annons_length']].head(30).sort_values(by=['Mask_score']))
#data.to_csv('Final_output.csv'),

data.info()