import streamlit as st
import pandas as pd
from funktioner import *
import altair as alt

df = pd.read_csv('Final_output_sve.csv')
st.set_page_config(page_title='Annonskollen', page_icon='', layout='wide')

st.header("Annonskollen") 
st.subheader("Lär dig att rekrytera kvinnliga utvecklare med vår tjänst! :computer:")
# lägga in en liten bild här? 
st.text("")
st.text("")
st.markdown("***Hur funkar det?***") #ändra färg på texten?
st.markdown(
    '''
    Idag består techbranschen av **70% män**. Samtidigt upplever arbetsgivare omfattande svårigheter med rekryteringen av kvinnliga utvecklare.
    Med vår databas bestående av XXX jobbannonser har vi skapat en tjänst där rekryterare kan testa 
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

col1, col2 = st.columns(2)
with col1:
    annons_input = st.text_area('Testa hur könsneutral din annons är: ',
                                height=300,
                                placeholder='Klistra in här...')
    annons_results = testa_annons(annons_input)

# Create a text input box
with col2:
    st.text("")
    st.text("")
    st.text("")

    if annons_input:
        if len(annons_results[0]) < 1:
            st.balloons() 
            st.success('Bra jobbat! Din annons innehåller inga manliga ord.')
        else:
            st.write('Din annons har ', len(annons_results[0]), 'manliga ord i sig')
            st.write('De maskulint vinklade orden är: ')
            annons_results.append(set(annons_results[0]))
            for ord in annons_results[2]:
                count = annons_results[0].count(ord)
                if count > 1:
                    st.write(f"{ord} ({count} gånger)")
                else:
                    st.write(ord)


    else:         
        top_5 = top_5_random(df, 'employer.name', 'Genomsnitt_mask_ord', 'Annons_length')
        st.write('''Här är fem företag som skriver annonser utan ett enda maskulint kodat ord, 
                 **bra jobbat!**''')
        for i in top_5['employer.name']:
            st.write('-', i)


st.text("")
if annons_input:
    annons_cosine_dict = calc_similarity(annons_input, df, 'employer.name', 'description.text')
    
    ## Räknar ut en ungefärlig procent av Cosine Similarity Score
    perc_dist = (math.pi - math.acos(annons_cosine_dict['similarity_score']))  * 100 / math.pi
    st.write('Din annons är mest lik en annons från ', annons_cosine_dict['employer'], )
    st.write('Era annonsers liknar varandra till ungefär ', str(math.trunc(perc_dist)), '%')
    if st.checkbox('Klicka för att visa annonsen'):
        st.write('Deras annons ser ut såhär: ')
        st.write(annons_cosine_dict['similar_ad'])

#Utfyllnad
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.subheader('Vanligaste manliga orden i jobbannonser')
barchart_data = pd.DataFrame(top_20_ord(df, 'Mask_ord'), columns=['Ord', 'Antal'])
barchart_data.dropna(inplace=False)

base = alt.Chart(barchart_data).mark_bar().encode(
    x=alt.X('Antal'),
    y=alt.Y('Ord', sort='-x' ),
    )


st.altair_chart(base.mark_bar(), use_container_width=True)