import pandas as pd
import csv

# read first 1000 rows of csv file
df = pd.read_csv('jobtech_dataset2022.csv', nrows=1000)


x = 0
dist_list = []

# for index, row in df.iterrows():
#     if "distans" in row['description']:
#         dist_list.append(row['description'])
#         x +=1
# print(x)
# print(dist_list)



big_list = []

for index, row in df.iterrows():
    b = row['workplace_address']
    b = b.split(',')[0]
    b = b.split(':')[1]
    b = b.replace("'", '')
    b = b.strip()

    big_list.append(b)
    #print(b)
    #print(type(b))

#print(a)



# counting each city
city_count = {}

for city in big_list:
    if city in city_count:
        city_count[city] += 1
    else:
        city_count[city] = 1

#print(city_count)

header = ['city']

with open('rensad_JBT.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for item in big_list:
        writer.writerow([item])


