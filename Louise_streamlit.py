import streamlit as st
import pandas as pd
from funktioner import *
import altair as alt
from PIL import Image


logo = Image.open('logo.png')


df = pd.read_csv('Final_output_sve.csv')
st.set_page_config(page_title='Annonskollen', page_icon='', layout='wide')

column_top1, column_top2 = st.columns(2)
with column_top1:
    st.image(logo, width=250)
with column_top2:
    st.subheader("Lär dig att rekrytera kvinnliga utvecklare med vår tjänst! :computer:")
# lägga in en liten bild här? 
st.text("")
st.text("")
st.markdown("***Hur funkar det?***") #ändra färg på texten?
st.markdown(
    '''
    Idag består techbranschen av **70% män**. Samtidigt upplever arbetsgivare omfattande svårigheter med rekryteringen av kvinnliga utvecklare.
    Med vår databas bestående av 5432 jobbannonser har vi skapat en tjänst där rekryterare kan testa 
    hur pass inkluderande deras annons är genom analys, för att undvika manligt betingade ord. 
    På så vis kan man uppnå en mer jämställd arbetskår på företaget och gå i framkant för fler jämställda företag!
    
    **Annonshjälpen erbjuder vägledning i form av att:**
    - Få din annons analyserad
    - Se de vanligaste manliga orden i jobbannonser
    - Do's and dont's
    ''')

st.text("")
st.text("")
st.text("")
st.text("")

annons_input = st.text_area('Testa hur könsneutral din annons är: ',
                                height=250,
                                placeholder='Klistra in här...')
annons_results = testa_annons(annons_input)

st.text("")
st.text("")
st.text("")

#testa annons
if annons_input:
    if len(annons_results[0]) < 1:
        st.balloons() 
        st.success('Bra jobbat! Din annons innehåller inga manliga ord.')
        
    else:
        ##### DET KOMMER MED DUBBLETTER!!!!
        st.write('Din annons har ', len(annons_results[0]), 'manliga ord i sig')
        st.write('De maskulint vinklade orden är: ')
        for i in range(len(annons_results[0])):
            st.write('-', annons_results[0][i])
else:         
    top_5 = top_5_random(df, 'employer.name', 'Genomsnitt_mask_ord', 'Annons_length')
    st.write('''Här är fem företag som skriver annonser utan ett enda maskulint kodat ord, 
            **bra jobbat!**''')
    for i in top_5['employer.name']:
        st.write('-', i)
st.text("")
if annons_input:
    annons_cosine_dict = calc_similarity(annons_input, df, 'employer.name', 'description.text')
    perc_dist = (math.pi - math.acos(annons_cosine_dict['similarity_score']))  * 100 / math.pi
    st.write('Din annons är mest lik en annons från ', annons_cosine_dict['employer'], )
    st.write('Era annonsers liknar varandra till ungefär ', str(math.trunc(perc_dist)), '%')
    if st.checkbox('Klicka för att visa annonsen'):
        st.write('Deras annons ser ut såhär: ')
        st.write(annons_cosine_dict['similar_ad'])
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
#Do's and don'ts 
st.subheader("Do's & Dont's")
st.checkbox("Ord spelar roll")
st.markdown("Ordvalet har betydelse. Omedvetet kan vissa ord avskräcka vissa från att söka. Tonalitet, bildval, hur arbetet beskrivs och hur företaget presenteras är också viktigt.")
st.checkbox("Håll kravlistan kort")
st.markdown(''' Forskning visar att fler män än kvinnor svarar på 
jobbannonser med långa kravlistor. För många krav kan avskräcka även 
erfarna och kvalificerade kvinnor att söka.''')
st.checkbox("Uppmuntran")
st.markdown('''Att berätta att företaget strävar mot större mångfald 
är viktigt. Det är också bra att avsluta annonsen med att 
uppmuntra läsaren att söka tjänsten.''')
st.checkbox("Ge exempel")
st.markdown('''Om inkludering är ett av företagets kärnvärden, 
ge konkreta exempel på vad det innebär för medarbetarna; 
flexibel arbetstid, möjligheten att arbeta deltid kan vara exempel.
''')
st.checkbox("Störst effekt för vissa roller")
st.markdown('''Det är framför allt i roller som domineras av män
som utformningen av platsannonsen påverkar fler
 kvinnor att söka. När Tieto Evry reviderade platsannonser för 
 projektledare blev det ingen skillnad, men ansökningarna från
  kvinnor ökade kraftigt för programmeringsroller som 
  domineras av män.''')
#Utfyllnad
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

#Vanligste orden
st.subheader('Vanligaste manliga orden i jobbannonser')
barchart_data = pd.DataFrame(top_20_ord(df, 'Mask_ord'), columns=['Ord', 'Antal'])
#st.bar_chart(barchart_data, x='Antal', y='Ord')

source = barchart_data

base = alt.Chart(source).mark_bar().encode(
    x=alt.X('Antal'),
    y=alt.Y('Ord', sort='-x' ),
    )


st.altair_chart(base.mark_bar(), use_container_width=True)