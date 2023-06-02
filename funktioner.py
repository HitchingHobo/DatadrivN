
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
import math
import re
import nltk

nltk.download('stopwords')
nltk.download('SnowballStemmer')

## Regelbaserad ai som räknar maskulina ord (2 st.)
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
    ## Hämtar maskulina ord
    gen_data = pd.read_csv('Lista Mask. och Fem. ord.csv', encoding='UTF8')
    gen_data.dropna(inplace=True)

    ## Sätter maskulina ord i listor och preppar dataframe's nya kolumner
    mask_list = []
    for row in gen_data['Maskulint kodade ord']:
        mask_list.append(row)

    data['Mask_score'] = ''
    data['Mask_ord'] = ''
    data['Annons_length'] = ''

    ## Sätter stopwords
    stopwords_list = stopwords.words('swedish')
    stopwords_list.extend(['analytics', 'analysera', 'aktiviteter', 'kraftnät', 'kraftsystem', 'försvarsmakten'])

    ## Huvudloop
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

## Uträkningar med df (4 st.)
def calculate_avg_df(df, group_by, column_to_avg):

    ## Räknar ut summan och medelvärdet av maskulina ord per företag
    calc_df = df.groupby(group_by)[column_to_avg].agg(['sum', 'mean'])

    ## Slår ihop och snyggar till kolumnerna
    Named_df = df.merge(calc_df, left_on=group_by, right_index=True)
    Named_df.rename(columns={"sum": "Totala_mask_ord"}, inplace=True)
    Named_df.rename(columns={"mean": "Genomsnitt_mask_ord"}, inplace=True)

    return Named_df


def top_5_random(df, employer_name, genomsnitt_mask_ord, annons_length):
    ## Grupperar df efter företag
    grouped_df = df.groupby(employer_name).mean(numeric_only=True)

    target_value = 8

    ## Räknar ut skillnaden mellan genomsnittet och target_value
    grouped_df['difference'] = abs(grouped_df[genomsnitt_mask_ord] - target_value)

    ## Sorterar och tar bort alla annonser som är kortare än 150 ord
    df_sorted = grouped_df.sort_values(genomsnitt_mask_ord, ascending=True).reset_index(drop=False)
    df_sorted = df_sorted.drop(df_sorted[df_sorted[annons_length] < 150].index)

    ## Tar fram 5 slumpmässiga annonser som har ett genomsnitt på 0 maskulina ord
    top_5_random = df_sorted[df_sorted[genomsnitt_mask_ord] == 0].sample(n=5)

    return top_5_random


def top_20_ord(df, mask_ord):
    
    ## Hämtar bara de maskulina orden från annonserna
    df = df[mask_ord]
    mask_list = []
    df = df.dropna()

    ## Preppar strängarna och lägger orden i en lista
    for index in df.index:
        row = df[index]
        row = str(row).lower()
        replacements = [("'", ""), ("[", ''), ("]",''), (" ", "")]

        for char, replacement in replacements:
            if char in row:
                row = row.replace(char, replacement)
        
        if row:        
            row = row.split(',')
            for i in row:
                mask_list.append(i)

    ## Räknar totalen och skickar tillbaka top 20 använda maskulina ord  
    mask_counter = Counter(mask_list)
    mask_vanligaste_ord = mask_counter.most_common(18)

    return mask_vanligaste_ord


def get_rank(df, score, value):  

    ## Grupperar df efter antal maskulina ord
    grouped_df = df.groupby(score).mean(numeric_only=True)
    df_sorted = grouped_df.sort_values(score, ascending=True).reset_index(drop=False)
    df_sorted = df_sorted[score] 
    
    ## Räknar ut ranken för en viss annons
    for i in range(len(df_sorted)):
        if value <= df_sorted[i]:
            rank = (i+1)
            break
    return rank

## Cosine funktioner (4 st.)
def preprocessor(text):
    
    stemmer = SnowballStemmer(language='swedish')
    lemmatizer = lemmy.load("sv")

    ## Klassisk textprepp
    text=str(text)
    text = text.lower()
    text=text.replace('{html}',"")
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', text)

    rem_url=re.sub(r'http\S+', '',cleantext)
    rem_num = re.sub('[0-9]+', '', rem_url)

    ## Tokenizing
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(rem_num)

    ## Tar bort stoppord och ord under 2 bokstäver
    filtered_words = [w for w in tokens if len(w) > 2 if not w in stopwords.words('swedish')]

    ## Stemmar och lemmar
    stem_words=[stemmer.stem(w) for w in filtered_words]
    lemma_words=[lemmatizer.lemmatize("",w) for w in stem_words]

    ## Returnerar en sträng
    output = list(itertools.chain.from_iterable(lemma_words))
    return " ".join(output)


def vectorize_texts(texts):

    ## Vectorizerar en text
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    return vectors, vectorizer


def prepare_df_for_cosine_no_mask(df, text_column):
    
    ## Tar bort alla annonser som har maskulina ord
    df_no_mask = df[df.Mask_score == 0]

    ## Preppar en texten från df för cosine similarity
    preprocessed_texts = df_no_mask[text_column].apply(preprocessor)
    vectors, vectorizer = vectorize_texts(preprocessed_texts)
    
    ## Sparar vectorized data med pickle för bättre prestanda för användaren
    vectorized_data = {
        'vectors': vectors,
        'vectorizer': vectorizer}
    
    with open('vectorized_data_no_mask.pkl', 'wb') as f:
        pickle.dump(vectorized_data, f)


def calc_similarity2(input_annons, data, employer_name, annons_text):

    ## Hämtar sparade vectorized data med pickle
    with open('vectorized_data_no_mask.pkl', 'rb') as f:
        vectorized_data = pickle.load(f)

    ## Preppar input annonsen och vectorizerar den
    input_vector = vectorized_data['vectorizer'].transform([preprocessor(input_annons)])
    sim_scores = cosine_similarity(input_vector, vectorized_data['vectors']).flatten()
    
    ## Sorterar och hämtar mest liknande annons och företag
    most_similar_index = sim_scores.argsort()[-1]
    most_similar_other_column = data[employer_name][most_similar_index]
    sim_score = sim_scores[most_similar_index]
    

    ## Skapar en dict som output
    output_dict = {}
    output_dict['similarity_score'] = sim_score
    output_dict['employer'] = most_similar_other_column
    output_dict['similar_ad'] = data[annons_text][most_similar_index]
    
    return output_dict

## Utbytta funktioner, anänds ej längre (2 st.)
def prepare_df_for_cosine(df, text_column):

    ## Preppar en texten från df för cosine similarity
    preprocessed_texts = df[text_column].apply(preprocessor)
    vectors, vectorizer = vectorize_texts(preprocessed_texts)
    
    ## Sparar vectorized data med pickle för framtida jämförelse med cosine
    vectorized_data = {
        'vectors': vectors,
        'vectorizer': vectorizer}
    
    with open('vectorized_data.pkl', 'wb') as f:
        pickle.dump(vectorized_data, f)

    df_no_mask = df[df.Mask_score == 0]


def calc_similarity(input_annons, data, employer_name, annons_text):

    ## Hämtar sparade vectorized data med pickle
    with open('vectorized_data.pkl', 'rb') as f:
        vectorized_data = pickle.load(f)

    ## Preppar input annonsen och vectorizerar den
    input_vector = vectorized_data['vectorizer'].transform([preprocessor(input_annons)])
    sim_scores = cosine_similarity(input_vector, vectorized_data['vectors']).flatten()
    
    ## Sorterar och hämtar mest liknande annons och företag
    most_similar_index = sim_scores.argsort()[-1]
    most_similar_other_column = data[employer_name][most_similar_index]
    sim_score = sim_scores[most_similar_index]
    

    ## Skapar en dict som output
    output_dict = {}
    output_dict['similarity_score'] = sim_score
    output_dict['employer'] = most_similar_other_column
    output_dict['similar_ad'] = data[annons_text][most_similar_index]
    
    return output_dict