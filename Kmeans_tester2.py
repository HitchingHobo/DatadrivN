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
from sklearn.cluster import KMeans
import numpy as np

pd.set_option('display.max_rows', None)

df = pd.read_csv('Final_output.csv', 
                 encoding='UTF8', 
                 nrows=1000)

# mask_df = pd.read_csv('mask_ord_kategorier.csv',
#                       encoding='UTF8')

# col1 = mask_df['hard'].tolist()
# col2 = mask_df['attribut'].tolist()
# col3 = mask_df['makt'].tolist()

# mask_list = col1, col2, col3
mask_list = [['agress', 'envis', 'fientlig', 'envis', 'tjurig', 'hänsynslös', 'försvar',
               'förkämpa', 'grym', 'kämp', 'utman', 'kraft', 'vass', 'manlig', 'hungrig',
               'beslut', 'bestäm', 'ledare', 'åsikt', 'domin', 'hierarki', 'maskulin'], 
             ['aktiv', 'ambiti', 'analytisk', 'atlet', 'frispråkig', 'girig', 'individ',
               'intellekt', 'intelligen', 'impulsiv', 'kompetent', 'logisk', 'logik', 'objektiv', 'äventyr',
               'autonomi', 'självsäker', 'leda', 'modig', 'självöförtroende', 'självständig', 'självgå']] 

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['Mask_ord'])




# Assuming 'category_lists' is a list of three category lists and 'list_weights' is a list of three weights
weights = [1.0, 1.0]
for i, category_list in enumerate(mask_list):
    for category_word in category_list:
        word_index = vectorizer.vocabulary_.get(category_word)
        if word_index is not None:
            X[:, word_index] *= weights[i]


##### KMEAAAAAAAAAAANS
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X)
cluster_labels = kmeans.labels_


representative_lists = []
for i in range(num_clusters):
    cluster_indices = np.where(cluster_labels == i)[0]
    cluster_texts = df.loc[cluster_indices, 'Mask_ord']
    list_counts = [sum(any(word in text for word in category_list) for text in cluster_texts) for category_list in mask_list]
    representative_list = mask_list[np.argmax(list_counts)]
    representative_lists.append(representative_list)






###### VIZZZZZZZ


import matplotlib.pyplot as plt

# Create a dictionary to store the top contributors for each cluster
# top_contributors = {}

# # Iterate over each cluster
# for i, representative_list in enumerate(representative_lists):
#     cluster_indices = np.where(cluster_labels == i)[0]
#     cluster_texts = df.loc[cluster_indices, 'Mask_ord']
#     cluster_word_counts = []
#     for word_list in representative_list:
#         word_counts = sum(any(word in text for word in word_list) for text in cluster_texts)
#         cluster_word_counts.append((word_list, word_counts))
    
#     # Sort the word counts in descending order
#     cluster_word_counts.sort(key=lambda x: x[1], reverse=True)
    
#     # Store the top contributors for the cluster
#     top_contributors[i] = cluster_word_counts[:10]  # Change the number 10 to display more or fewer top contributors
    
#     # Print the cluster number and its top contributors
#     print(f"Cluster {i} Top Contributors:")
#     for word, count in cluster_word_counts:
#         print(f"- {word}: {count}")
    
#     # Plot a bar chart of the word counts
#     words = [word for word, count in cluster_word_counts]
#     counts = [count for word, count in cluster_word_counts]
#     plt.figure(figsize=(10, 6))
#     plt.bar(words, counts)
#     plt.title(f"Cluster {i} Top Contributors")
#     plt.xlabel("Words")
#     plt.ylabel("Counts")
#     plt.xticks(rotation=45)
#     plt.show()

# # Print the top contributors for each cluster
# print("\nTop Contributors for Each Cluster:")
# for cluster, contributors in top_contributors.items():
#     print(f"Cluster {cluster}:")
#     for word, count in contributors:
#         print(f"- {word}: {count}")


import matplotlib.pyplot as plt

# Create a dictionary to store the top contributors for each cluster
top_contributors = {}

# Iterate over each cluster
for i in range(num_clusters):
    cluster_indices = np.where(cluster_labels == i)[0]
    cluster_texts = df.loc[cluster_indices, 'Mask_ord']
    cluster_word_counts = {}

    # Calculate word counts for each unique word in the cluster
    for text in cluster_texts:
        words = set(text.split())
        for word in words:
            cluster_word_counts[word] = cluster_word_counts.get(word, 0) + 1

    # Sort the word counts in descending order
    sorted_word_counts = sorted(cluster_word_counts.items(), key=lambda x: x[1], reverse=True)

    # Store the top contributors for the cluster
    top_contributors[i] = sorted_word_counts[:10]  # Change the number 10 to display more or fewer top contributors

    # Print the cluster number and its top contributors
    print(f"Cluster {i} Top Contributors:")
    for word, count in sorted_word_counts:
        print(f"- {word}: {count}")

    # Plot a bar chart of the word counts
    words = [word for word, count in sorted_word_counts]
    counts = [count for word, count in sorted_word_counts]
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.title(f"Cluster {i} Top Contributors")
    plt.xlabel("Words")
    plt.ylabel("Counts")
    plt.xticks(rotation=45)
    plt.show()

# Print the top contributors for each cluster
print("\nTop Contributors for Each Cluster:")
for cluster, contributors in top_contributors.items():
    print(f"Cluster {cluster}:")
    for word, count in contributors:
        print(f"- {word}: {count}")

