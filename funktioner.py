
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd
import itertools
import pickle
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
    stopwords_list.extend(['analytics', 'analysera'])

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



def testa_annons_df(data, text_column):
    gen_data = pd.read_csv('Lista Mask. och Fem. ord.csv', encoding='UTF8')
    gen_data.dropna(inplace=True)

    mask_list = []
    for row in gen_data['Maskulint kodade ord']:
        mask_list.append(row)

    data['Mask_score'] = ''
    data['Mask_ord'] = ''
    data['Annons_length'] = ''

    stopwords_list = stopwords.words('swedish')
    stopwords_list.extend(['analytics', 'analysera'])

    for index, row in data.iterrows():
        text = str(row[text_column]).lower()
        mask_word_list = []
        x = 0
        for word in text.split():
            x += 1
            if word not in stopwords_list:
                for i in mask_list:
                    if word.startswith(i):
                        mask_word_list.append(i)
            else:
                continue
        data.loc[index, 'Mask_ord'] = ', '.join(mask_word_list)
        data.loc[index, 'Mask_score'] = len(mask_word_list)
        data.loc[index, 'Annons_length'] = x

    return data



def calculate_avg_df(df, group_by, column_to_avg):

    calc_df = df.groupby(group_by)[column_to_avg].agg(['sum', 'mean'])

    Named_df = df.merge(calc_df, left_on=group_by, right_index=True)
    Named_df.rename(columns={"sum": "Totala_mask_ord"}, inplace=True)
    Named_df.rename(columns={"mean": "Genomsnitt_mask_ord"}, inplace=True)

    return Named_df

def top_20_ord():
    data = pd.read_csv('Final_output_sve.csv', encoding=('UTF8'))
    
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


# def cosine_check_df(text_to_compare):
#     df = pd.read_csv('Final_output_sve.csv',
#                  encoding='utf-8',
#                  nrows=10)

#     df['processed.text'] = df['description.text'].apply(preprocessor)   
#     vectorizer = TfidfVectorizer()
#     vectorizer.fit(df['processed.text'])

#     vectors = vectorizer.transform(df['processed.text'])
#     input_vector = vectorizer.transform([preprocessor(text_to_compare)])
#     print(input_vector)
#     similarity_scores = cosine_similarity(input_vector, vectors)[0]

#     df['similarity_score'] = similarity_scores
    
#     # Print the most similar text and its similarity score

#     most_similar_index = similarity_scores.argsort()[-1]
#     most_similar_text = df['processed.text'][most_similar_index]
#     most_similar_employer = df['employer.name'][most_similar_index]
#     similarity_score = similarity_scores[most_similar_index]

#     return [most_similar_text, most_similar_employer, similarity_score]


################# UNDER ÄNDRING #################

def vectorize_texts(texts):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)
    return vectors, vectorizer

def prepare_df_for_cosine(df, text_column):
    preprocessed_texts = df[text_column].apply(preprocessor)
    vectors, vectorizer = vectorize_texts(preprocessed_texts)
    
    # Store the vectorized representations and corresponding index/identifier
    vectorized_data = {
        'vectors': vectors,
        'vectorizer': vectorizer}
    
    with open('vectorized_data.pkl', 'wb') as f:
        pickle.dump(vectorized_data, f)

def calculate_similarity(vectorized_data, sample_text):
    input_vector = vectorized_data['vectorizer'].transform([preprocessor(sample_text)])
    similarity_scores = cosine_similarity(input_vector, vectorized_data['vectors']).flatten()
    
    return similarity_scores

def load_vectorized_data():
    # Load the vectorized data and vectorizer object
    with open('vectorized_data.pkl', 'rb') as f:
        vectorized_data = pickle.load(f)
    return vectorized_data

# # Exemepl på 5 rader
# df = pd.read_csv('Utvecklare_lista_svenska.csv',nrows=10)

# # Preprocess and vectorize the text column
# prepare_df_for_cosine(df, 'description.text')

# #Loading vectorized data from file
# vectorized_data = load_vectorized_data()

# # Loads vectorizer and preprocesses incoming annons
# input_vector = vectorized_data['vectorizer'].transform([preprocessor(sample_annons)])

# # Calculates cosine simulatiry
# similarity_scores = cosine_similarity(input_vector, vectorized_data['vectors']).flatten()