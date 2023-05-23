from funktioner import *



############# OBS Preppsteg, körs bara 1 gång (redan körd) #############

df = pd.read_csv('Utvecklare_lista_svenska.csv',
                    encoding='utf-8',)

df = testa_annons_df(df, 'description.text')

df = calculate_avg_df(df, 'employer.name', 'Mask_score')

prepare_df_for_cosine(df, 'description.text')

df.to_csv('Final_output_sve.csv', index=False)

############# OBS Preppsteg, körs bara 1 gång (redan körd) #############

