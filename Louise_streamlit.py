import streamlit as st
import pandas as pd 

data = pd.read_csv('Final_output.csv')
st.set_page_config(page_title='Mindmakerzzz', page_icon='', layout='wide')

st.header("MindMakerz")
st.subheader("Lär dig att rekrytera kvinnliga utvecklare med vår tjänst!")

# Create a text input box
st.markdown(
    """
    <style>
    .expanded-textarea .stTextInput textarea {
        min-height: 200px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
col1, col2 = st.columns(2)
with col1:
    st.subheader('Se hur könsneutral din annons är!')
    
    annons_input = st.text_input("Testa din annons här: ", "Klistra in här...")
with col2:
    st.subheader("Do's and dont's")
    st.text("***Do's:***")
    manligt = st.checkbox('Kolla igenom de manligt betingade orden')
    check_lista = st.checkbox('Utseslut kravspecifikationer')



# Use the user input
#st.write("You entered:", annons_input)