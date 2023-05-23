import pandas as pd
from funktioner import *


sample_annons = """Om jobbet Arbetsuppgifter - Programmering i alla dess former! 
T ex parprogrammering, mobprogrammering eller kanske något nytt kreativt som du vill utforska? 
- Aktivt delta i beslut gällande produkter, features, arkitektur och affärsmål.
- Lärande och kunskapsdelning i både team och organisation.
Är du redo för något intressant? På SBAB jobbar vi värderingsdrivet. Wow! Hoppas vi att du tänker. 
Våra värderingar är viktiga för oss på riktigt! De handlar om att jobba smart med fart, ta ansvar 
hela vägen, vara stolta proffs och att lyckas tillsammans. Faktum är att värderingarna hjälper oss 
att fatta kloka beslut och vi vill att du gör detsamma hos oss. De hjälper dig i rätt riktning, 
stöttar att ta egna initiativ, ha roligt tillsammans, jobba ihop och bidra till att våra kunder 
får en bättre boendeekonomi. Fortfarande intresserad? Välkommen! Att jobba som Utvecklare
Vill du vara en del i ett autonomt team som arbetar med aktuell teknik? Hos oss på SBAB får du 
möjlighet att vara med och utveckla bankens egna system och applikationer!
Du blir en del av ett nytänkande och självständigt team som har ett nära samarbete med andra team 
och våra användare. I denna roll får du även aktivt delta i utforskande och beslutstagande inom 
produkter, features, arkitektur och mål. Vi tror att du är en lagspelare som gillar att förvandla 
bra idéer till features och har en balans mellan kvalitet och tempo. Du är van vid agila arbetssätt, 
så som Scrum & Kanban - eller kanske en kombination av båda?
Varje team äger sin domän och ansvarar för de mikrotjänster som agerar inom den. Saknar du erfarenhet 
av några av våra tekniker eller har du kunskaper inom andra språk eller verktyg så är det inga problem, 
vi lär oss gärna och vill att du ska utvecklas med oss!
Vår teknikstack innehåller:  Mikrotjänster i Kotlin, Java och Spring Boot, som körs på Kubernetes
- Web-appar i TypeScript med olika ramverk som tex React - Design patterns som tex Event sourcing och CQRS
- Meddelande-driven kommunikation via Kafka och Avro - GraphQL och REST baserade APIer
Du får titeln ”Fullstack Developer”, men vi vet att ingen är expert på allt. Det vi menar är att 
man är en utvecklare som känner sig trygg inom backend eller frontend, men samtidigt är nyfiken 
och vill lära sig mer där man känner sig mindre trygg. Vi kommer att uppmuntra dig att gå utanför 
din komfortzon och pröva nya teknologier. Att växa som utvecklare ingår i vårt dagliga arbete, 
men även under mer kreativa former som Hackdays och Devjams.
I det här avsnittet gäster vi Kodsnack under ledning av Fredrik Björeman. Ni får träffa fyra 
utvecklare som börjar med att prata om likheter och skillnader mellan SBAB och Booli. Därefter 
om hur man avvecklar äldre monoliter på ett planerat och konstruktivt sätt, mikrotjänsters 
fördelar och problem och mycket mer. Låter det intressant, kontakta oss så berättar vi mer.
Har du check på allt? - Lagspelare - Nyfiken - Analytisk - Initiativtagande - Självdriven Annars då?
Gillar du oss, och tror att du kan bidra, är vårt tips att inte vänta för länge med att 
skicka in CV eller LinkedIn-profil. Har du andra idéer på hur du kan visa vem du är? 
Spännande! Hur du än ansöker så ser vi fram emot att lära känna dig mer."""
 
df = pd.read_csv('Final_output_sve.csv',
                 encoding='utf-8',
                 )









# Assuming you have a DataFrame named 'df' with columns 'employer.name', 'Genomsnitt_mask_ord', and 'Rank'


def get_rank(input_score):
    # Group the DataFrame by rank
    df['Rank'] = df['Genomsnitt_mask_ord'].rank(ascending=True, method='min')
    grouped_df = df.groupby('Rank').agg({
        'employer.name': 'first',
        'Genomsnitt_mask_ord': 'first'
    }).reset_index()

    # Fetch the rank for input_score
    rank = grouped_df.loc[grouped_df['Genomsnitt_mask_ord'] == input_score, 'Rank'].values[0]
    return rank




# Example usage
# input_score = 0
# rank = get_rank(input_score)

# print(f"The input score of {input_score} ranks as {int(rank)}")


# # Assuming you have a DataFrame named 'df' with columns 'Company', 'Description', 'Score', and 'Rank'

# print(df[['employer.name', 'Genomsnitt_mask_ord', 'Rank']].head(10))

# df = df[['employer.name', 'Genomsnitt_mask_ord', 'Rank', 'Annons_length']]


# df = df.groupby('employer.name').mean(numeric_only=True)
# df = df.sort_values(by=['Rank'], ascending=True)
group_df = get_group(df)
print(df)
print(group_df)