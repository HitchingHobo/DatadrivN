from funktioner import *

## Prepp i sex steg
## 1. Läs in data från csv, bara svenska annonser som söker utvecklare
## 2. Analyserar annonsen för maskulina ord och sätter info i nya df-kolumner
## 3. Räknar ut medelvärde för maskulina ord per företag
## 4. Preppar df för cosine similarity, endast annonser utan maskulina ord
## 5. Sparar df i en csv med all info

############# OBS Preppsteg, körs bara 1 gång (redan körd) #############

# df = pd.read_csv('Utvecklare_lista_svenska.csv',
#                     encoding='utf-8',)

# df = testa_annons_df(df, 'description.text')

# df = calculate_avg_df(df, 'employer.name', 'Mask_score')

# prepare_df_for_cosine_no_mask(df, 'description.text')

# df.to_csv('Final_output_sve.csv', index=False)

############# OBS Preppsteg, körs bara 1 gång (redan körd) #############

