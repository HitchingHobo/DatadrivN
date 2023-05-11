import pandas as pd
from nltk.corpus import stopwords

#pd.set_option('display.max_colwidth', None)

gen_data = pd.read_csv('Lista Mask. och Fem. ord.csv', encoding=('UTF8'))
gen_data.dropna(inplace=True)

mask_list = []
fem_list = []

## Sätter maskulina & feminina ord i listor
for row in gen_data['Maskulint kodade ord']:
    mask_list.append(row)
for row in gen_data['Feminint kodade ord']:
    fem_list.append(row)


data = pd.read_csv('utvecklare_lista.csv',
                    encoding=('UTF8'),
                    nrows=3000,)
data.info()
pos_word_list=[]
neu_word_list=[]
neg_word_list=[]
data['Mask_score'] = ''
data['Fem_score'] = ''
from nltk.stem.snowball import SwedishStemmer
stemmer = SwedishStemmer()

combined = '\t'.join(mask_list)

stopwords_list = stopwords.words('swedish')
stopwords_list += stopwords.words('english')
stopwords_list.extend(['academic', 'work', 'the', 'tiqqe', 'även'])

for index in data.index:
    row = data['description.text'][index]
    row = str(row).lower()   
    pos_word_list=[]
    neu_word_list=[]
    neg_word_list=[]
    
    for word in row.split():
        for i in mask_list:
            if word.startswith(i):
                pos_word_list.append(word) 
                #print(pos_word_list) 
        if word in stopwords_list:
            continue
        elif len(word) <4:
            continue
        # elif word in combined:
        #     pos_word_list.append(word)
        #    print(pos_word_list)
        elif word in fem_list:
            neg_word_list.append(word)
        else:
            neu_word_list.append(word)
    data['Mask_score'][index] = len(pos_word_list)
    data['Fem_score'][index] = len(neg_word_list)


print(data)