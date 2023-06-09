import streamlit as st
import pandas as pd
from funktioner import *
import altair as alt
from PIL import Image
## return [mask_word_list, fem_word_list, antal_ord]

logo = Image.open('logo.png')



#[theme]
primaryColor="#ec0b0b"
backgroundColor="#fdfdfd"
secondaryBackgroundColor="#c3c3c3"
textColor="#000000"




data = pd.read_csv('Final_output.csv')
st.set_page_config(page_title='Annonskollen', page_icon='', layout='wide')

column_top1, column_top2 = st.columns(2)
with column_top1:
    st.image(logo, width=250)
with column_top2:
    st.header("MindMakerz")
st.subheader("Lär dig att rekrytera kvinnliga utvecklare med vår tjänst!")
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
    st.write('Din annons har ', len(annons_results[0]), 'manliga ord i sig')
    st.write('De maskulint vinklade orden är: ')

    for i in range(len(annons_results[0])):
        st.write(annons_results[0][i])
        if len(annons_results) == 1:
             st.write('Du har inga kodade ord')
        elif len(annons_results) == 2:
            st.write('Du har 1 kodat ord')
        elif len(annons_results) == 3:
            st.write('Du har två kodade ord')
        else:
            st.write('Du har tre eller fler kodade ord')
        

if annons_input:
    st.subheader('Testa')      


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