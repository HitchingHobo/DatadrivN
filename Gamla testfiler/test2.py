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


df.info()

value = 2
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


annons_res = testa_annons(sample_annons)

