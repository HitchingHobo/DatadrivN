import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')


#DATE_COLUMN = 'date/time'
#DATA = 'jobtech_dataset2022.csv'
DATA = 'rensad_JBT.csv'





@st.cache_data

def load_data(nrows):
    data = pd.read_csv(DATA, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data


# data_load_state = st.text('Loading data...')
data = load_data(100)
# data_load_state.text("Done! (using st.cache_data)")

st.dataframe(data)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)



st.subheader(f'Map of all pickups at')
st.map(data)
