import plotly.express as px
import pandas as pd
import streamlit as st

data = pd.read_excel('Panda7.xlsx')

st.set_page_config(layout="wide")
st.title('IRE monde intensité')
st.subheader('Ch. B.')

fig = px.choropleth(data, locations='iso_a3',
            color='IntRem', hover_name='Pays',
            animation_frame = 'Annee',
            animation_group = 'Pays',
            color_continuous_scale= px.colors.sequential.Plasma)

st.plotly_chart(fig, use_container_width=True)