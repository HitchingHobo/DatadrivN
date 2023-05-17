import pandas as pd
import nltk
import re

pd.set_option('display.max_colwidth', None)


## Importerar data och slöpper NaN
gen_data = pd.read_csv('Lista Mask. och Fem. ord.csv', encoding=('UTF8'))
gen_data.dropna(inplace=True)

mask_list = []
fem_list = []

## Sätter maskulina & feminina ord i listor
for row in gen_data['Maskulint kodade ord']:
    mask_list.append(row)
for row in gen_data['Feminint kodade ord']:
    fem_list.append(row)

## Importerar JBT-data
data = pd.read_csv('utvecklare_lista.csv',
                    encoding=('UTF8'),
                    nrows=10,)
data = data[['description.text', 'employer.name']]
data = data.dropna()


def text_preprocessing(text):
    
    # Convert words to lower case
    text = text.lower()

    # Format words and remove unwanted characters
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\<a href', ' ', text)
    text = re.sub(r'&amp;', '', text) 
    text = re.sub(r'[_"\-;%()|+&=*%.,!?:#$@\[\]/]', ' ', text)
    text = re.sub(r'<br />', ' ', text)
    text = re.sub(r'\'', ' ', text) 

    # Tokenize each word
    text = nltk.WordPunctTokenizer().tokenize(text)

    # Lemmatize each word
    text = [nltk.stem.WordNetLemmatizer().lemmatize(token, pos='v') for token in text if len(token)>1]
    
    return text

def to_string(text):
    # Convert list to string
    text = ' '.join(map(str, text))

    return text

# Create a list of data by applying text_preprocessing function
data['Data_Clean_List'] = list(map(text_preprocessing, data['description.text']))

# Return to string with to_string function
data['Data_Clean'] = list(map(to_string, data['Data_Clean_List']))


from nltk.corpus import stopwords
stopwords_list = stopwords.words('swedish')
stopwords_list.extend(['academic', 'work', 'the'])

import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

# Import Counter 
from collections import Counter

stopwords_list = stopwords.words('swedish')
stopwords_list.extend(['academic', 'work', 'the', 'tiqqe'])

data['Data_Clean_List'] = [[word for word in line if word not in stopwords_list] for line in data['Data_Clean_List']]
data['Data_Clean'] = list(map(to_string, data['Data_Clean_List']))

# Join all word corpus
data_words = ','.join(list(data['Data_Clean'].values))

# Count and find the 30 most frequent
Counter = Counter(data_words.split())
most_frequent = Counter.most_common(30)

##Bar plot of frequent words
# fig = plt.figure(1, figsize = (20,10))
# _ = pd.DataFrame(most_frequent, columns=("words","count"))
# sns.barplot(x = 'words', y = 'count', data = _, palette = 'winter')
# plt.xticks(rotation=45);
# plt.show()

from wordcloud import WordCloud

# wordcloud = WordCloud(background_color="white",
#                       max_words= 200,
#                       contour_width = 8,
#                       contour_color = "steelblue",
#                       collocations=False).generate(data_words)
                      
# # Visualize the word cloud
# fig = plt.figure(1, figsize = (10, 10))
# plt.axis('off')
# plt.imshow(wordcloud)
# plt.show()

import gensim
# Create Dictionary
id2word = gensim.corpora.Dictionary(data['Data_Clean_List'])

# Create Corpus: Term Document Frequency
corpus = [id2word.doc2bow(text) for text in data['Data_Clean_List']]

# Define the number of topics 
n_topics = 2

# Run the LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=n_topics, 
                                           random_state=100,
                                           update_every=1,
                                           chunksize=10,
                                           passes=10,
                                           alpha='symmetric',
                                           iterations=100,
                                           per_word_topics=True)

for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} Word: {}".format(idx, topic))