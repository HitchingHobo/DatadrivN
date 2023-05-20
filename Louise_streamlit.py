import streamlit as st
import pandas as pd
from funktioner import *
import altair as alt
from PIL import Image 
## return [mask_word_list, fem_word_list, antal_ord]

data = pd.read_csv('Final_output_sve.csv')
st.set_page_config(page_title='Annonskollen', page_icon='', layout='wide')

st.header("Annonskollen") 
st.subheader("Lär dig att rekrytera kvinnliga utvecklare med vår tjänst! :computer:")
# lägga in en liten bild här? 
st.text("")
st.text("")
st.markdown("***Hur funkar det?***") #ändra färg på texten?
st.markdown(
    '''
    Idag består techbranschen av **70% män**. Enligt kvalitativ data finns det en stor 
    problematik kring att rekrytera kvinnliga utvecklare. 
    Genom en databas med xxx jobbannonser har vi skapat en tjänst
    för rekryterare som hjälper rekryterare att undvika manligt betingade ord i syfte
    att attrahera kvinnliga kandidater. 

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
                                height=250,
                                placeholder='Klistra in här...')
    annons_results = testa_annons(annons_input)
    
# Create a text input box
with col2:
    st.text("")
    st.text("")
    st.text("")
    if len(annons_results[0]) < 1:
        st.balloons() 
        st.success('Bra jobbat! Din annons innehåller inga manliga ord.')
        
    else:
       st.write('Din annons har ', len(annons_results[0]), 'manliga ord i sig')
       st.write('De maskulint vinklade orden är: ')
       for i in range(len(annons_results[0])):
           st.write('-', annons_results[0][i])

#if annons_input:
 #   st.subheader('Testa')      


# col3, col4 = st.columns(2)
# with col1:
    #Utfyllnad
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.subheader('Vanligaste manliga orden i jobbannonser')
barchart_data = pd.DataFrame(top_20_ord(), columns=['Ord', 'Antal'])
#st.bar_chart(barchart_data, x='Antal', y='Ord')

source = barchart_data

base = alt.Chart(source).mark_bar().encode(
    x=alt.X('Antal'),
    y=alt.Y('Ord', sort='-x' ),
    )


st.altair_chart(base.mark_bar(), use_container_width=True)