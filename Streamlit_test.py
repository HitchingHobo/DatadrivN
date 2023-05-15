import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title='Mindmakerz', page_icon='', layout='wide')


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.jason()

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

# VARFÖR VISAS INTE KODEN