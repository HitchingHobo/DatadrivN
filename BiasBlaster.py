import streamlit as st
import pandas as pd
from funktioner import *
import altair as alt
from PIL import Image


logo = Image.open('Logo3.png')


df = pd.read_csv('Final_output_sve.csv')
st.set_page_config(page_title='BiasBlaster | by MindMakers', page_icon='', layout='centered')

st.image(logo)

st.write('')
st.write('')
st.write('')


tab1, tab2 = st.tabs(['Hur funkar det?', 'Testa din annons'])
# lägga in en liten bild här? 

with tab1:
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

with tab2:
    annons_input = st.text_area('Testa hur könsneutral din annons är: ',
                                    height=250,
                                    placeholder='Klistra in här...')
    if st.checkbox('Analysera annons'):
        annons_results = testa_annons(annons_input)
        annons_cosine_dict = calc_similarity(annons_input, df, 'employer.name', 'description.text')
        col1, col2 = st.columns(2)
        with col2:
            if len(annons_input.split()) >= 70:
                if len(annons_results[0]) < 1:
                    st.success('Bra jobbat! Din annons innehåller inga manliga ord.')
                    if st.button('Fira med en ballong!'):
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
                perc_dist = (math.pi - math.acos(annons_cosine_dict['similarity_score']))  * 100 / math.pi
                st.write('Din annons är mest lik en annons från ', annons_cosine_dict['employer'])
                st.write('Era annonsers liknar varandra till ungefär ', str(math.trunc(perc_dist)), '%')
                rank = get_rank(df, 'Genomsnitt_mask_ord', len(annons_results[0]))
                if len(annons_results[0]) > 0:
                    st.write('Din annons har ', len(annons_results[0]), 'manliga ord i sig')
                else:
                    st.write('Din annons har inga manliga ord i sig')
                st.write('Vi rankar din annons som nr:', str(rank))
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
    st.subheader("Do's & Dont's")
    st.checkbox("Ord spelar roll")
    with st.expander('Läs mer'):
        st.markdown("Ordvalet har betydelse. Omedvetet kan vissa ord avskräcka vissa från att söka. Tonalitet, bildval, hur arbetet beskrivs och hur företaget presenteras är också viktigt.")
    st.checkbox("Håll kravlistan kort")
    with st.expander('Läs mer'):
        st.markdown(''' Forskning visar att fler män än kvinnor svarar på 
        jobbannonser med långa kravlistor. För många krav kan avskräcka även 
        erfarna och kvalificerade kvinnor att söka.''')
    st.checkbox("Uppmuntran")
    with st.expander('Läs mer'):
        st.markdown('''Att berätta att företaget strävar mot större mångfald 
    är viktigt. Det är också bra att avsluta annonsen med att 
    uppmuntra läsaren att söka tjänsten.''')
    st.checkbox("Ge exempel")
    with st.expander('Läs mer'):
        st.markdown('''Om inkludering är ett av företagets kärnvärden, 
    ge konkreta exempel på vad det innebär för medarbetarna; 
    flexibel arbetstid, möjligheten att arbeta deltid kan vara exempel.
    ''')
    st.checkbox("Störst effekt för vissa roller")
    with st.expander('Läs mer'):
        st.markdown('''Det är framför allt i roller som domineras av män
    som utformningen av platsannonsen påverkar fler
    kvinnor att söka. När Tieto Evry reviderade platsannonser för 
    projektledare blev det ingen skillnad, men ansökningarna från
    kvinnor ökade kraftigt för programmeringsroller som 
    domineras av män.''')
st.write('---') 
with col2:
    #Vanligste orden
    st.write('Vanligaste manliga orden i jobbannonser')
    barchart_data = pd.DataFrame(top_20_ord(df, 'Mask_ord'), columns=['Ord', 'Antal'])
    #st.bar_chart(barchart_data, x='Antal', y='Ord')

    source = barchart_data

    base = alt.Chart(source).mark_bar().encode(
        x=alt.X('Antal'),
        y=alt.Y('Ord', sort='-x' ),
        ).configure_mark(
            color='red' )


    st.altair_chart(base.mark_bar(), use_container_width=True)