# import pandas as pd


# pd.set_option('display.max_rows', None)
# data=pd.read_csv('KMEANS_output.csv', 
#                  encoding=('UTF8'),
#                  nrows=100)

# data=data[['cluster_label', 'employer.name']]
# data.sort_values(by=['employer.name'], inplace=True)
# print(data)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

pd.set_option('display.max_rows', None)

df = pd.read_csv('Final_output.csv', 
                 encoding='UTF8', 
                 nrows=1000)

mask_data = pd.read_csv('Lista Mask. och Fem. ord.csv',
                        encoding='UTF8')
mask_data = mask_data['Maskulint kodade ord']
mask_data = mask_data.dropna()
print(mask_data)


# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(df['description.text'])

# import numpy as np

# # Assuming 'category_lists' is a list of three category lists and 'list_weights' is a list of three weights
# for i, category_list in enumerate(category_lists):
#     for category_word in category_list:
#         word_index = vectorizer.vocabulary_.get(category_word)
#         if word_index is not None:
#             X[:, word_index] *= list_weights[i]
