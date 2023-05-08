import pandas as pd

# read_csv function which is used to read the required CSV file
data = pd.read_csv('jobtech_dataset2022.csv')
data = data[['id', 'description', 'headline']]

print(data.head(4))