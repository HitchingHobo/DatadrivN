import streamlit as st
import pandas as pd
from funktioner import *
import altair as alt
from PIL import Image
from streamlit_lottie import st_lottie
import requests 


logo = Image.open('Logo.png')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_celebrate = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_kfl4ksd9.json')


df = pd.read_csv('Final_output_sve.csv')
st.set_page_config(page_title='BiasBlaster | by MindMakers', page_icon='', layout='centered')

st.image(logo)

st.write('')
st.write('')
st.write('')


tab1, tab2 = st.tabs(['Hur funkar det?', 'Testa din annons'])


with tab1:
    st.markdown("***Hur funkar det?***") 
    st.markdown(
        '''
        Idag består techbranschen av **70% män**. Samtidigt upplever arbetsgivare omfattande svårigheter med rekryteringen av kvinnliga utvecklare.
        Med vår databas bestående av 5432 jobbannonser har vi skapat en tjänst där rekryterare kan testa 
        hur pass inkluderande deras annons är genom analys, för att undvika manligt betingade ord. 
        På så vis kan man uppnå en mer jämställd arbetskår på företaget och gå i framkant för fler jämställda företag!
        
        **BiasBlaster erbjuder vägledning i form av att:**
        - Få din annons analyserad
        - Se de vanligaste manliga orden i jobbannonser
        - Checklista fär din annons
        ''')

with tab2:
    annons_input = st.text_area('Testa hur könsneutral din annons är: ',
                                    height=250,
                                    placeholder='Klistra in här...')
    #if st.checkbox('Analysera annons'):
    annons_results = testa_annons(annons_input)
    annons_cosine_dict = calc_similarity(annons_input, df, 'employer.name', 'description.text')
    col1, col2 = st.columns(2)
    with col2:
        if len(annons_input.split()) >= 70:
            if len(annons_results[0]) < 1:
                st.success('Bra jobbat! Din annons innehåller inga manliga ord.')
                if st.button('Fira med en ballong!'):
                    #st_lottie(lottie_celebrate, height=300, key='celebrate')
                    st.balloons()
            else:
                
                st.write('De maskulint vinklade orden i din annons är: ')
                annons_results.append(set(annons_results[0]))
                for ord in annons_results[2]:
                    count = annons_results[0].count(ord)
                    if count > 1:
                        st.write('-', f"{ord} ({count} gånger)")
                    else:
                        st.write('-', ord)

        else:         
            top_5 = top_5_random(df, 'employer.name', 'Genomsnitt_mask_ord', 'Annons_length')
            st.write('''Här är fem förebilder som skriver annonser utan ett enda maskulint kodat ord, 
                **bra jobbat!**''')
            for i in top_5['employer.name']:
                st.write('-', i)
    with col1:
        if len(annons_input.split()) >= 70:
            if len(annons_results[0]) > 0:
                st.write('Din annons har ', str(len(annons_results[0])), 'manliga ord i sig')
            else:
                st.write('Din annons har inga manliga ord i sig')
            rank = get_rank(df, 'Genomsnitt_mask_ord', len(annons_results[0]))                
            st.write('Vi rankar din annons som nr:', str(rank))
            rank = get_rank(df, 'Genomsnitt_mask_ord', len(annons_results[0]))
            perc_dist = (math.pi - math.acos(annons_cosine_dict['similarity_score']))  * 100 / math.pi
            st.write('Din annons är mest lik en annons från ', annons_cosine_dict['employer'])
            st.write('Era annonsers liknar varandra till ungefär ', str(math.trunc(perc_dist)), '%')
            



        if len(annons_input.split()) <= 0:
            st.write('Klistra in din annons ovaför för att analysera den!')
        elif len(annons_input.split()) < 70:
            st.write('Din annons är lite för kort för att göra en rättvis analys. Försök med minst 70 ord')


    if len(annons_input.split()) >= 70:
        st.write('---')
        if st.checkbox('Klicka för att visa din annonsgranne'):
            st.write('Deras annons ser ut såhär: ')
            st.write(annons_cosine_dict['similar_ad'])

st.write('---')

col1, col2 = st.columns(2)
with col1:
        #Do's and don'ts 
    st.subheader("Checklsita")
    check1 = st.checkbox("Välj rätt ord")
    with st.expander('Läs mer'):
        st.markdown("Ordvalet har betydelse. Välj neutrala ord när du kan! Förekomsten av maskulint kodade ord avskräcker kvinnor, medan feminint kodade ord inte påverkar manliga kandidater")
    check2 = st.checkbox("Håll kravlistan kort")
    with st.expander('Läs mer'):
        st.markdown(''' Forskning visar att färre kvinnor än män svarar på 
        jobbannonser med långa kravlistor. Kraven avskräcker 
        erfarna och kvalificerade kvinnor att söka.''')
    check3 = st.checkbox("Undvik krav på år")
    with st.expander('Läs mer'):
        st.markdown('''Specifierade år av erfarenhet avskräcker kvinnor att söka om dem inte uppnår
         exakta år. Undik längd på arbetserfarenhet och använd andra beskrivande sätt''')
    check4 = st.checkbox("Uppmärksamma insatser för inkludering!")
    with st.expander('Läs mer'):
        st.markdown('''Om inkludering är ett av företagets kärnvärden, 
    ge konkreta exempel på vad det innebär för medarbetarna; 
    flexibel arbetstid, möjligheten att arbeta hemifrån osv.
    ''')
    check5 = st.checkbox("Säkerställ kravprofilen mot bias")
    with st.expander('Läs mer'):
        st.markdown('''Nämner du kön, sexuell läggning, religion, funktionsnedsättning, etnisk
         tillhörighet? Gör om!''')
    if check1 and check2 and check3 and check4 and check5:
        st.write('')
        st.write('')
        st.markdown('''**Bra jobbat! 
        Din annons är neutralt kodad och redo för publicering!**''')

st.write('---') 
with col2:
    #Vanligste orden
    st.write('De vanligaste manskulint kodade orden i annonser')
    barchart_data = pd.DataFrame(top_20_ord(df, 'Mask_ord'), columns=['Ord', 'Antal'])
    #st.bar_chart(barchart_data, x='Antal', y='Ord')

    source = barchart_data

    base = alt.Chart(source).mark_bar().encode(
        x=alt.X('Antal'),
        y=alt.Y('Ord', sort='-x' ),
        ).configure_mark(
            color='red' )

    st.altair_chart(base.mark_bar(), use_container_width=True)

    if check1 and check2 and check3 and check4 and check5:
        st_lottie(lottie_celebrate, height=300, key='celebrate')
