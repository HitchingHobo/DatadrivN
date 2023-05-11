from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

sentiment = SentimentIntensityAnalyzer()

text_1 = ' Intellektuell Vi tror att du agerar relationsskapande i samarbetet med andra, är serviceinriktad och besitter ett stort intresse och en stor vilja att hjälpa andra. Du är tydlig i din kommunikation och har en förmåga att fatta snabba besluta' 
text_1 = text_1.lower()


data = pd.read_csv('utvecklare_lista.csv', encoding=('UTF8'), nrows=20)
data = data[ (data['description.text'].str.contains('utvecklare', na=False))]
data = data[['occupation.label',  'employer.name', 'description.text']]

## Gör alla bokstäver små
for i in data['occupation.label']:
    data['description.text'] = data['description.text'].str.lower()


gen_data = pd.read_csv('Lista Mask. och Fem. ord.csv', encoding=('UTF8'))
mask_data = gen_data['Maskulint kodade ord']
mask_data = mask_data.dropna()
fem_data = gen_data['Feminint kodade ord']
fem_data = fem_data.dropna()

## Ploppar in våra svenska ord i VADER lexicon
new_words = {}

for word in mask_data:
    new_words[word] = -1.5

for word in fem_data:
    new_words[word] = 1.5

sentiment.lexicon.update(new_words)

sent_1 = sentiment.polarity_scores(text_1)

print("Sentiment of text 3:", sent_1)


pos_word_list=[]
neu_word_list=[]
neg_word_list=[]
for word in text_1.split():
    if (sentiment.polarity_scores(word)['compound']) >= 0.1:
        pos_word_list.append(word)
    elif (sentiment.polarity_scores(word)['compound']) <= -0.1:
        neg_word_list.append(word)
    else:
        neu_word_list.append(word)  

print('Positive:',pos_word_list)
print('Neutral:',neu_word_list)
print('Negative:',neg_word_list)         


from nltk.stem.snowball import SwedishStemmer
stemmer = SwedishStemmer()

## Svensk stemming
# text_1_stemmed = ''
# for i in text_1.split():
#     i = stemmer.stem(i)
#     text_1_stemmed = text_1_stemmed + ' ' + i

# print(text_1_stemmed)
data['Antal_mask'] = 0
data['Antal_fem'] = 0
## TRASIG stemmar all text
# for row in data['description.text']:
#     new_row=''
#     for i in row.split():
#         i = stemmer.stem(i)
#         new_row = new_row + ' ' + i
#     data['description.text'] = new_row


## Loopar genom data, testa mer effektiv teknik, tar lång tid
# for row in data['description.text']:
#     sia = sentiment.polarity_scores(data['description.text'])
#     print(sia)
#     # data['Sentiment'] = sia['compound']
#     pos_word_list=[]
#     neu_word_list=[]
#     neg_word_list=[]
#     for word in row.split():
#         word = stemmer.stem(word)
#         if (sentiment.polarity_scores(word)['compound']) >= 0.1:
#             pos_word_list.append(word)
#             data['Antal_fem'] += 1
#         elif (sentiment.polarity_scores(word)['compound']) <= -0.1:
#             neg_word_list.append(word)
            
#         else:
#             neu_word_list.append(word)  
#     print('Positive:',pos_word_list)
#     print('Neutral:',neu_word_list)
#     print('Negative:',neg_word_list)

    # data['Antal_mask'] = len(pos_word_list)
    # data['Antal_fem'] = len(neg_word_list)         


# stemmar alla ord i mask_data och lägger i lista
# mask_data_stemmed = []

# for i in mask_data:
#     # stem word
#     i = stemmer.stem(i)
#     # append word to list
#     mask_data_stemmed.append(i)
print(data)
