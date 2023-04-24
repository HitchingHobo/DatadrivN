import pandas as pd
import json

# read first 1000 rows of csv file
df = pd.read_csv('jobtech_dataset2022.csv', nrows=1000)


x = 0
dist_list = []

# for index, row in df.iterrows():
#     if "distans" in row['description']:
#         dist_list.append(row['description'])
#         x +=1
# print(x)

# print each column title
# for col in df.columns:
#      print(col)

# print workpalce_address for each row
# for index, row in df.iterrows():
#     print(type(['workplace_address']))

a = []

for index, row in df.iterrows():
    b = row['workplace_address']
    b = b.split(',')[0]
    b = b.split(':')[1]
    b = b.replace("'", '')
    b = b.strip()

    a.append(b)
    #print(b)
    #print(type(b))

#print(a)



city_count = {}

# count each occurance of word in list and add to dictionary
for city in a:
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

print(city_count)



