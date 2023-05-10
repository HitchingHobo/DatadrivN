from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentiment = SentimentIntensityAnalyzer()

text_1 = 'Vi tror att du agerar relationsskapande i samarbetet med andra, är serviceinriktad och besitter ett stort intresse och en stor vilja att hjälpa andra. Du är tydlig i din kommunikation och har en förmåga att fatta snabba beslut' 
text_1 = text_1.lower()

import pandas as pd

data = pd.read_csv('Lista Mask. och Fem. ord.csv', encoding=('UTF8'))
mask_data = data['Maskulint kodade ord']
fem_data = data['Feminint kodade ord']

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