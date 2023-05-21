import pandas as pd
from funktioner import *

df = pd.read_csv('Final_output_sve.csv',
                    encoding='utf-8',
                    nrows=10)


calc_df = df.groupby('employer.name')['Mask_score'].agg(['sum', 'mean'])

Named_df = df.merge(calc_df, left_on='employer.name', right_index=True)
Named_df.rename(columns={"sum": "Totala_mask_ord"}, inplace=True)
Named_df.rename(columns={"mean": "Genomsnitt_mask_ord"}, inplace=True)

df['processed.text'] = df['description.text'].apply(preprocessor)



vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(df['processed.text'])

df['Vectorized_processed_text'] = [vector.toarray() for vector in vectors]




df.info()
print(df.head(10))


df.to_csv('TRYME.csv', index=False, encoding='utf-8')
