
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd
import itertools
import lemmy
import re


def testa_annons(annons):
    gen_data = pd.read_csv('Lista Mask. och Fem. ord.csv', 
                        encoding=('UTF8'))
    gen_data.dropna(inplace=True)

    mask_list = []

    ## Sätter maskulina ord i listor
    for row in gen_data['Maskulint kodade ord']:
        mask_list.append(row)  

    ## Sätter stopwords
    stopwords_list = stopwords.words('swedish')
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


def top_20_ord():
    data = pd.read_csv('Final_output_sve.csv', encoding=('UTF8'))
    
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
    mask_vanligaste_ord = mask_counter.most_common(20)

    return mask_vanligaste_ord


def preprocessor(text):
    stemmer = SnowballStemmer(language='swedish')
    lemmatizer = lemmy.load("sv")

    text=str(text)
    text = text.lower()
    text=text.replace('{html}',"")
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', text)

    rem_url=re.sub(r'http\S+', '',cleantext)
    rem_num = re.sub('[0-9]+', '', rem_url)

    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(rem_num)

    filtered_words = [w for w in tokens if len(w) > 2 if not w in stopwords.words('swedish')]

    stem_words=[stemmer.stem(w) for w in filtered_words]

    lemma_words=[lemmatizer.lemmatize("",w) for w in stem_words]

    output = list(itertools.chain.from_iterable(lemma_words))
    return " ".join(output)

################# UNDER ÄNDRING #################
def cosine_check_df(text_to_compare):
    df = pd.read_csv('Final_output_sve.csv',
                 encoding='utf-8',
                 nrows=10)

    df['processed.text'] = df['description.text'].apply(preprocessor)   
    vectorizer = TfidfVectorizer()
    vectorizer.fit(df['processed.text'])

    vectors = vectorizer.transform(df['processed.text'])
    input_vector = vectorizer.transform([preprocessor(text_to_compare)])
    print(input_vector)
    similarity_scores = cosine_similarity(input_vector, vectors)[0]

    df['similarity_score'] = similarity_scores
    
    # Print the most similar text and its similarity score

    most_similar_index = similarity_scores.argsort()[-1]
    most_similar_text = df['processed.text'][most_similar_index]
    most_similar_employer = df['employer.name'][most_similar_index]
    similarity_score = similarity_scores[most_similar_index]

    return [most_similar_text, most_similar_employer, similarity_score]
################# UNDER ÄNDRING #################

