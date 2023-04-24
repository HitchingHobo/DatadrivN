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


from geopy import geocoders
from geopy.geocoders import Nominatim

gn = geocoders.GeoNames(username='Hitchinghobo')

geolocator = Nominatim(user_agent="CSV_extractor.py")
#location = geolocator.geocode("Göteborg")


#print(location.latitude, location.longitude)

dict_long = {}
dict_lat = {}

# for i in city_count:
    
#     location = geolocator.geocode(i)
#     dict_long[i] = location.longitude
#     dict_lat[i] = location.latitude

# print(city_count)
# print(dict_long)
# print(dict_lat)

header = ['city', 'longitude', 'latitude']
master_list = [['Stockholm', 18.0710935, 59.3251172], ['Uppsala', 17.6387436, 59.8586126], ['Göteborg', 11.9670171, 57.7072326], ['Gävle', 17.1467019, 60.6750132], ['Varberg', 12.2502949, 57.1057412], ['Uddevalla', 11.9382855, 58.3490555], ['Sundsvall', 17.3071024, 62.3907552], ['Hudiksvall', 17.105575, 61.7281607], ['None', 7.540121, 44.933143], ['Kiruna', 20.302778, 67.848889], ['Gällivare', 20.25, 67.3], ['Helsingborg', 12.703706, 56.0442098], ['Västerås', 16.5463679, 59.6110992], ['Malmö', 13.0001566, 55.6052931], ['Partille', 12.1166649, 57.7333362], ['Kristianstad', 14.1566859, 56.0293778], ['Hultsfred', 15.8, 57.4], ['Lerum', 12.3, 57.833333], ['Sundbyberg', 17.9681359, 59.3628802], ['Trelleborg', 13.1461522, 55.37592], ['Lund', 13.1929449, 55.7029296], ['Växjö', 14.8094385, 56.8787183], ['Högsby', 16.0321284, 57.1664483], ['Örkelljunga', 13.2828212, 56.2827878], ['Båstad', 12.8607151, 
56.4267895], ['Ängelholm', 12.8619375, 56.2429224], ['Osby', 14.083333, 56.416667], ['Perstorp', 13.366667, 56.2], ['Hässleholm', 13.733333, 56.216667], ['Markaryd', 13.6, 56.55], ['Halmstad', 12.8574827, 56.6739826], ['Laholm', 13.233333, 56.5], ['Alvesta', 14.5, 56.916667], ['Tingsryd', 14.966667, 56.533333], ['Mullsjö', 13.8, 57.95], ['Värnamo', 14.0410977, 57.184902], ['Falköping', 13.516667, 58.2], ['Trollhättan', 12.2908612, 58.2827931], ['Skara', 13.4397675, 58.3846075], ['Lidköping', 13.1576427, 58.5037196], ['Skövde', 13.8443792, 58.3898453], ['Vimmerby', 15.833333, 57.683333], ['Ljungby', 13.933333, 56.85], ['Linköping', 15.6245252, 58.4098135], ['Norrköping', 16.1903511, 58.5909124], ['Mölndal', 12.0153085, 57.6564918], ['Eskilstuna', 16.5051474, 59.3717379], ['Jönköping', 14.165719, 57.7825634], ['Södertälje', 17.6271663, 59.1964289], ['Söderhamn', 17.0607599, 61.2998501], ['Nacka', 18.2073591, 59.3120997], ['Älmhult', 14.116667, 56.55], ['Lessebo', 15.266667, 56.766667], ['Emmaboda', 15.5366179, 56.6302659], ['Värmdö', 18.583333, 59.3], ['Lindesberg', 15.25, 59.666667], ['Upplands Väsby', 17.916667, 59.516667], ['Karlskrona', 15.5866422, 56.1621073], ['Solna', 18.0013693, 59.361367], ['Uppvidinge', 15.666667, 57.0], ['Kalmar', 16.575102000807693, 57.02784235], ['Vetlanda', 15.167830505066155, 57.36554305], ['Oskarshamn', 16.4443478, 57.2632811], ['Mönsterås', 16.416667, 57.066667], ['Falkenberg', 12.4912926, 56.904894], ['Hylte', 13.25, 56.95], ['Sävsjö', 14.666667, 57.333333], ['Borås', 12.9407407, 57.7210839], ['Västervik', 16.6385035, 57.7594186], ['Tyresö', 18.333333, 59.216667], ['Valdemarsvik', 16.6, 58.2], ['Luleå', 22.1459535, 65.5831187], ['Umeå', 20.2630745, 63.8256568], ['Örebro', 15.2151181, 59.2747287], ['Karlstad', 13.5027631, 
59.3809146], ['Borlänge', 15.4234561, 60.4856426], ['Gislaved', 13.45, 57.25], ['Gnosjö', 13.783333, 57.366667], ['Vaggeryd', 14.083333, 57.55], ['Storuman', 16.416667, 65.4], ['Katrineholm', 16.2067589, 58.9960335], ['Vingåker', 15.883333, 59.066667], ['Flen', 16.716667, 59.05], ['Järfälla', 17.8285472, 59.4204736], ['Upplands-Bro', 17.67388804328231, 59.5357323], ['Täby', 18.0658494, 59.4670482], ['Vallentuna', 18.216667, 59.583333], ['Tierp', 17.616667, 60.333333], ['Borgholm', 16.666667, 56.883056], ['Enköping', 17.077856, 59.6356115], ['Karlskoga', 14.5176911, 59.3291667], ['Gotland', 18.536957927499856, 57.4174802], ['Ulricehamn', 13.383333, 57.8], ['Lidingö', 18.1820897, 59.3669445], ['Motala', 15.041261, 58.5420395], ['Tomelilla', 13.9329289, 55.5447478], ['Kävlinge', 13.0337618, 55.7795769], ['Svalöv', 13.1069825, 55.9136519], ['Mark', 21.8422843, 48.5914169], ['Bollnäs', 16.3972013, 61.3513005], ['Sandviken', 16.7724214, 60.619422], ['Landskrona', 12.8296734, 55.8698007], ['Huddinge', 17.9748815, 59.2293827], ['Sollentuna', 17.9500556, 59.4293164], ['Boden', 7.8558961, 50.4721829], ['Ljusdal', 15.7, 61.866667], ['Höganäs', 12.566667, 56.2], ['Botkyrka', 17.8545982, 59.2034494], ['Lilla Edet', 12.166667, 58.133333], ['Norrtälje', 18.7, 59.766667], ['Örnsköldsvik', 18.7160209, 63.2888613], ['Torsby', 13.083333, 60.5], ['Strömstad', 11.1736096, 58.9377567], ['Eksjö', 14.9735595, 57.6674439], ['Köping', 15.9970475, 59.5137434], ['Kungsbacka', 12.166667, 57.466667], ['Ystad', 13.8196555, 55.4329849], ['Danderyd', 18.0358505, 59.4043647], ['Alingsås', 12.5329678, 57.9299658], ['Burlöv', 13.116667, 55.65], ['Falun', 15.6323059, 60.6070068], ['Vårgårda', 12.7769271, 58.0340071], ['Arboga', 15.8396643, 59.394187], ['Skellefteå', 20.959339, 64.7520185], 
['Nynäshamn', 17.9470987, 58.9056457], ['Staffanstorp', 13.2, 55.65], ['Lekeberg', 14.758333, 59.191667], ['Strängnäs', 17.0268194, 59.3763155], ['Åstorp', 12.9462464, 56.1351211], ['Vellinge', 13.033333, 55.466667], ['Hallsberg', 15.25, 59.05], ['Ale', 3.163882848311948, 46.36746405], ['Haninge', 18.266667, 59.049722], ['Stenungsund', 11.916667, 58.083333], ['Kumla', 15.1435463, 59.1272047], ['Sala', 126.9782914, 37.5666791], ['Kungsör', 16.1, 59.433333], ['Oxelösund', 17.083056, 58.666667], ['Orsa', 14.75, 61.3], ['Älvkarleby', 17.416667, 60.583333], ['Rättvik', 15.383333, 60.966667], ['Ockelbo', 16.583333, 60.883333], ['Säffle', 12.85, 59.116667], ['Leksand', 15.0, 60.716667], ['Gagnef', 15.0, 60.5], ['Timrå', 17.2995411, 62.4922058], ['Malung-Sälen', 13.666667, 60.566667], ['Sollefteå', 16.916667, 63.383333], ['Ånge', 15.64108973113128, 62.4733988], ['Älvdalen', 13.75, 61.333333], ['Härnösand', 17.9379914, 62.6323084], ['Ragunda', 16.3, 63.166667], ['Härjedalen', 13.95, 62.25], ['Kramfors', 17.666667, 62.916667], ['Arvika', 12.65, 59.766667], ['Sigtuna', 17.7236301, 59.6165201], ['Haparanda', 24.1357213, 65.835667], ['Östersund', 14.6357061, 63.1793655], ['Finspång', 15.833333, 58.8], ['Nyköping', 17.0120656, 58.7545409], ['Skinnskatteberg', 15.75, 59.816667], ['Höör', 13.533333, 55.933333], ['Fagersta', 15.833333, 59.966667], ['Kungälv', 11.916667, 57.9], ['Götene', 13.533333, 58.55], ['Avesta', 16.333333, 60.216667]]

print(type(master_list[0]))
print(master_list[0])


import csv

with open("rensad_JBT.csv", "w", encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(master_list)

# with open('rensad_JBT.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
#     for item in master_list:
#         writer.writerow([item])
        
       
# for item in city_count:
#     dict_long[item]=geolocator.geocode(item).longitude
#     dict_lat[item]=geolocator.geocode(item).latitude


# merge_list = []
# for i in city_count:
#     merge_list.append([i, dict_long[i], dict_lat[i]])




