#import requests
#from streamlit_lottie import st_lottie
import streamlit as st
import pandas as pd 

data = pd.read_csv('Final_output.csv')
st.set_page_config(page_title='Mindmakerz', page_icon='', layout='wide')

st.header("MindMakerz")

