import requests
import streamlit as st
from streamlit_lottie import st_lottie
import random
import pandas as pd


st.set_page_config(page_title='Mindmakerz', page_icon='', layout='wide')


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_job_ad = load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_g7ayoegc.json')


with st.container():
    st.subheader('Mindmakerzzz')
    st.title('Annons-scoreboard ')
    st.write('Vi vill hjälpa dig att göra din jobbannons så neutral som möjligt för att du ska kunna locka rätt kompetenser')
    

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('Hur funkar det?')
        st.write('##')
        st.write(
            '''
            Genom en databas med jobbannonser och ord som klassas som köns-kodade
            så kan vi visa hur mycket av en annons är vinklad mot att locka ett
            visst kön, och kan riskera att missa god kompetens av det motsatta
            könet. Syftet är att visa hur en bra och sämre annons ser ut, 
            kommer du kunna göra en mer jämlik annons
            ''')
    with right_column:
        st_lottie(lottie_job_ad, height=300, key='coding')


    # Read the CSV file
df = pd.read_csv('Final_output.csv')



def check_text(input_text, word_list):
    matches = []
    for col, word_column in enumerate(word_list):
        for word in word_column:
            if word.lower() in input_text.lower():
                matches.append((word, col+1))
    return matches

# Load the CSV file
word_data = pd.read_csv('Lista Mask. och Fem. ord.csv')

# Convert each column to lowercase and store as a list of lists
word_list = []
for col in range(4):
    words = word_data.iloc[:, col].astype(str).str.lower().tolist()
    word_list.append(words)


# Remove missing values ("nan") from the word list
word_list = [[word for word in words if word != 'nan'] for words in word_list]


# Streamlit app layout
st.title("Kolla din annons om den innehåller något kodat ord")

with st.container():
    st.subheader("Skriv in din text:")
    input_text = st.text_input("Text")

    if st.button("Kolla!"):
        matching_words = check_text(input_text, word_list)
        if matching_words:
            st.subheader("Matching keyword(s):")
            for word, col in matching_words:
                if col in [1, 3]:
                    column_label = "Maskulint"
                else:
                    column_label = "Feminint"
                st.write(f"Könskodat ord: {word}, {column_label}")
        else:
            st.write("Inga maskulint eller feminint kodade ord hittades.")
