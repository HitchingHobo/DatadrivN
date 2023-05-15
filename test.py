import pandas as pd



data=pd.read_csv('Final_output.csv', encoding=('UTF8'))
data.info()

print(data.head(30))

print(data.head(30).sort_values(by=['Mask_score']))