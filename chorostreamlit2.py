import streamlit as st
import folium
import plotly.express as px
from openpyxl import *
import pandas as pd
from streamlit_folium import folium_static
import altair as alt
from vega_datasets import data

st.set_page_config(layout="wide")
geojson_url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json'

m = folium.Map(location=[20,10], zoom_start =2)

st.title('IntRem mondiale')
st.subheader('Ch. Bill')

data = pd.read_excel('Panda7.xlsx')

fig = px.scatter(data, x='iso_a3',
            color='IntRem', hover_name='Pays',
            animation_frame = 'Annee',
            animation_group = 'Pays',
            color_continuous_scale= px.colors.sequential.Plasma,
            projection='natural earth')

st.plotly_chart(fig)