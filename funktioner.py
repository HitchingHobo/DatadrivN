import pandas as pd
from nltk.corpus import stopwords


def testa_annons(annons):
    gen_data = pd.read_csv('Lista Mask. och Fem. ord.csv', 
                        encoding=('UTF8'))
    gen_data.dropna(inplace=True)

    mask_list = []

    ## Sätter maskulina & feminina ord i listor
    for row in gen_data['Maskulint kodade ord']:
        mask_list.append(row)
    for row in gen_data['Masculinecoded words']:
        mask_list.append(row)    

    ## Sätter stopwords
    stopwords_list = stopwords.words('swedish')
    stopwords_list += stopwords.words('english')
    stopwords_list.extend(['academic', 'work', 'the', 'tiqqe', 'även', 'analytics', 'analysera'])

    ## Preppar variabler
    antal_ord = 0
    mask_word_list = []


    ## Huvudloop
    for word in annons.split():
        antal_ord += 1
        if word not in stopwords_list:
            for i in mask_list:
                if word.startswith(i):
                    mask_word_list.append(i) 
        else:
            continue

    return [mask_word_list, antal_ord]



from collections import Counter

def top_30_ord():
    data = pd.read_csv('final_output.csv', encoding=('UTF8'))
    
    #data_mask = ','.join(list(data['Mask_ord'].values))
    data = data['Mask_ord']
    mask_list = []
    for index in data.index:
        row = data[index]
        row = str(row).lower()
        replacements = [("'", ""), ("[", ''), ("]",''), (" ", "")]

        for char, replacement in replacements:
            if char in row:
                row = row.replace(char, replacement)
        if row:        
            row = row.split(',')
            for i in row:
                mask_list.append(i)
        
    mask_counter = Counter(mask_list)
    mask_vanligaste_ord = mask_counter.most_common(30)

    return mask_vanligaste_ord



print(top_30_ord())
print(type(top_30_ord()))
print(type(top_30_ord()[0]))    

barchart_data = pd.DataFrame(top_30_ord(), columns=['Ord', 'Antal'])

barchart_data.info()
print(barchart_data)
