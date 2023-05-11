from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd


SIA = SentimentIntensityAnalyzer()
SIA.lexicon.clear()

## Hämtar våra svenska ord och lägger i listor
gen_data = pd.read_csv('Lista Mask. och Fem. ord.csv', encoding=('UTF8'))
mask_data = gen_data['Maskulint kodade ord'].dropna()
fem_data = gen_data['Feminint kodade ord'].dropna()

## Ploppar in våra svenska ord i VADER lexicon
new_words = {}
for word in mask_data:
    new_words[word] = -1.5
for word in fem_data:
    new_words[word] = 1.5

SIA.lexicon.update(new_words)
print(SIA.lexicon)

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
sentence = 'Vi har logik stort engagemang för det individ intelligen vi gör och tar på stort allvar att vi utvecklar en produkt som har stor effekt för många. Detta samtidigt som vi driver utvecklingen framåt och har väldigt roligt'
pos_word_list=[]
neu_word_list=[]
neg_word_list=[]
for word in sentence.split():
    if (SIA.polarity_scores(word)['compound']) >= 0.1:
        pos_word_list.append(word)
    elif (SIA.polarity_scores(word)['compound']) <= -0.1:
        neg_word_list.append(word)
    else:
        neu_word_list.append(word)                
print('Positive:',pos_word_list)
print('Neutral:',neu_word_list)
print('Negative:',neg_word_list) 
score = SIA.polarity_scores(sentence)
print('\nScores:', score)