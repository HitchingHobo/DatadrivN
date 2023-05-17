import streamlit as st
import pandas as pd
from funktioner import *
import altair as alt
## return [mask_word_list, fem_word_list, antal_ord]

data = pd.read_csv('Final_output.csv')
st.set_page_config(page_title='Mindmakerzzz', page_icon='', layout='wide')

st.header("MindMakerz")
st.subheader("Lär dig att rekrytera kvinnliga utvecklare med vår tjänst!")

# Create a text input box
col1, col2 = st.columns(2)
with col1:
    st.subheader('Se hur könsneutral din annons är!')
    
    annons_input = st.text_input("Testa din annons här: ", "Klistra in här...")
    annons_results = testa_annons(annons_input)
    st.write('Din annons har ', len(annons_results[0]), 'manliga')
with col2:
    st.subheader("Do's and dont's")
    st.text("Do's:")
    manligt = st.checkbox('Kolla igenom de manligt betingade orden')
    check_lista = st.checkbox('Utseslut kravspecifikationer')
    #fylla på här 
    st.text("Dont's")


# col3, col4 = st.columns(2)
# with col1:
    #Utfyllnad
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

st.subheader('Vanligaste manliga orden i jobbannonser')
barchart_data = pd.DataFrame(top_30_ord(), columns=['Ord', 'Antal'])
#st.bar_chart(barchart_data, x='Antal', y='Ord')

source = barchart_data

base = alt.Chart(source).mark_bar().encode(
    x=alt.X('Antal', sort='-x'),
    y=alt.Y('Ord'),
    )


st.altair_chart(base.mark_bar() + base.mark_text(align='left', dx=2), use_container_width=True)