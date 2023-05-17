import pandas as pd
from nltk.corpus import stopwords


def testa_annons(annons):
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


    ## Sätter stopwords
    stopwords_list = stopwords.words('swedish')
    stopwords_list += stopwords.words('english')
    stopwords_list.extend(['academic', 'work', 'the', 'tiqqe', 'även', 'analytics', 'analysera'])

    ## Preppar variabler
    antal_ord = 0
    mask_word_list = []
    fem_word_list = []


    ## Huvudloop
    for word in annons.split():
        antal_ord += 1
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

    return [mask_word_list, fem_word_list, antal_ord]


## Testing
# text1 = 'Winningtemps vision är att förändra hur vi har effektiva samarbeten på arbetsplatsen. Genom en gedigen vetenskaplig grund skapar Winningtemp en plattform för direkt uppföljning av välbefinnande och motivation hos sina kundanställda. Genom att  ""mäta temperaturen""  för sina anställda genom AI-baserad programvara kan kunderna arbeta både proaktivt och reaktivt för att motverka stress och arbeta för en förbättrad arbetsmiljö. Detta görs genom en stor förståelse för det mänskliga perspektivet i utveckling, med fokus på vad som gynnar  personen  bakom resultaten.'

# results = testa_annons(text1)

# print(results)
from collections import Counter

def totalt_antal_ord():
    data = pd.read_csv('final_output.csv', encoding=('UTF8'))
    data_mask = ','.join(list(data['Mask_ord'].values))

    mask_counter = Counter(data_mask.split())
    mask_vanligaste_ord = mask_counter.most_common(30)

    return mask_vanligaste_ord

import seaborn as sns
import matplotlib.pyplot as plt

most_frequent = totalt_antal_ord()

fig = plt.figure(1, figsize = (20,10))
_ = pd.DataFrame(most_frequent, columns=("words","count"))
sns.barplot(x = 'words', y = 'count', data = _, palette = 'winter')
plt.xticks(rotation=45);
plt.show()