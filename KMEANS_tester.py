import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np  

## Laddar och preppar data samt de maskulina orden
df = pd.read_csv('Final_output.csv', encoding='UTF8', nrows=1000)

mask_data = pd.read_csv('Lista Mask. och Fem. ord.csv', encoding='UTF8')
mask_data = mask_data.dropna()
mask_ord = mask_data['Maskulint kodade ord'].tolist()
df['har_mask_ord'] = df['Mask_ord'].apply(lambda text: any(word in text for word in mask_ord))


## Delar upp annonser som inte har några manliga ord i sig inför klusteringen
annons_med_mask = df[df['har_mask_ord']]['Mask_ord'].tolist()
annons_utan_mask = df[~df['har_mask_ord']]['Mask_ord'].tolist()

## Preppar med TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(annons_med_mask)

## Kör K-means och sätter labels, speciell label för annonser utan maskulina ord
num_clusters = 4
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X)

cluster_labels = kmeans.labels_
df.loc[df['har_mask_ord'], 'cluster_label'] = cluster_labels
df.loc[~df['har_mask_ord'], 'cluster_label'] = -1

## Testprint
print(df.head(10))
df.info()





## Visualisering


## Använder PCA för visualisering
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X.toarray())

## Scatterplot
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df[df['har_mask_ord']]['cluster_label'])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA resultat')
plt.show()



## Visar top bidragande ord till varje cluster
pc1_loadings = pca.components_[0]
pc2_loadings = pca.components_[1]

top_features_pc1 = pc1_loadings.argsort()[::-1][:5]
top_features_pc2 = pc2_loadings.argsort()[::-1][:5]

feature_names = vectorizer.get_feature_names_out()

## Printar topp 5 ord
print("Topp 5 ord för Principal Component 1:")
for feature_idx in top_features_pc1:
    print(feature_names[feature_idx])
    
print("\nTopp 5 ord för Principal Component 2:")
for feature_idx in top_features_pc2:
    print(feature_names[feature_idx])




## Visualisering i 3D
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X.toarray())


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(X_pca[:, 0], X_pca[:, 1], X_pca[:, 2], c=cluster_labels, cmap='viridis')

ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
ax.set_title('Clustering Results (PCA)')

legend_elements = scatter.legend_elements()
labels = [f'Cluster {label}' for label in np.unique(cluster_labels)]
legend = ax.legend(legend_elements[0], labels, loc='upper right', title='Clusters')


plt.setp(legend.get_title(), fontsize='11')

plt.show()



