import os
import numpy as np 
import pandas as pd 
from keplergl import KeplerGl
from streamlit_keplergl import keplergl_static
from map_config import config_point, config_hex
import streamlit as st 

st.set_page_config(layout='wide')

# Data Reading
data = pd.read_csv(os.path.join(os.path.dirname(__file__),"nyc-app.csv"),index_col=0)

# Data Pre-processing
data = data[data['X Coordinate'] != 'Not Found']
data['X Coordinate'] = data['X Coordinate'].astype(float)
data['Y Coordinate'] = data['Y Coordinate'].astype(float)
data['Sale Price'] = data['Sale Price'].round(2)
data['Gross Square Feet'] = data['Gross Square Feet'].round(2)
data['Year Built'] = data['Year Built'].round()

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width:500px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Filters
left_space, rows, right_space = st.sidebar.columns([0.2,1.6,0.2])

with rows:
    st.title('Filters')
    borough = st.multiselect('Regions', data['Borough'].unique(), default=data['Borough'].unique())
    year_built_min, year_built_max = st.select_slider('Year Built', options=data['Year Built'].sort_values(), value=[data['Year Built'].min(),data['Year Built'].max()])
    sale_price_min, sale_price_max = st.select_slider('Sale Price', options=data['Sale Price'].sort_values(), value=[data['Sale Price'].min(), data['Sale Price'].max()])
    map_view = st.radio('Map Visualization',options=['Point View','Hex View'])

data = data[data['Borough'].isin(borough)]
data = data[(data['Year Built'] >= year_built_min) & (data['Year Built'] <= year_built_max)]
data = data[(data['Sale Price'] >= sale_price_min) & (data['Sale Price'] <= sale_price_max)]


# Introduction
column_image, column_title = st.columns([0.2,2.0])
with column_image:
    st.image('Icons/new-york.png',width=100)

with column_title:
    st.title('NYC Properties Sales')

st.write("New York City is a amazing place. Full of buildings, amazing skyscrapers, restaurants, big avenues, parks, all of that with the presence of people from all around the world. When visiting this place, it is almost possible to not ask 'How much does it costs to live here?' ")

st.write('This app is a simple explorer of the NYC Property Sales Dataset, published on Kaggle, focused on main informations of the Buildings being sold, like Price, Area, and most common type of properties, aggregated by Zip Codes. For a interactive view of the data, an Kepler.GL map is used,  associated with interactive widgets from Streamlit, located on the sidebar. Also, two different modes of map are presented, wich can be selected by the "Map Visualization" filter.')

avg_price = np.round(data['Sale Price'].mean(),2)
avg_area = np.round(data['Gross Square Feet'].mean(),2)
avg_year = np.round(data['Year Built'].mean(),2)

space_left, column_image_1, column_1, column_image_2, column_2, column_image_3, column_3, space_right = st.columns([1.0, 0.7, 2.0, 0.7, 2.0, 0.7, 2.0, 0.2])

with column_image_1:
    st.image('Icons/dollar.png',width=70)

with column_1:
    st.metric('Average Sale Price ($)', avg_price)

with column_image_2:
    st.image('Icons/area-chart.png',width=70)

with column_2:
    st.metric('Average Area of Properties (ft²)', avg_area)

with column_image_3:
    st.image('Icons/calendar.png',width=70)

with column_3:
    st.metric('Average Year Built', avg_year)

## Map Visualization
map_data = data[['X Coordinate','Y Coordinate','Sale Price','Address','Building Class Category','Gross Square Feet']]

if map_view == 'Point View':
    ny_map = KeplerGl(height=600,config=config_point)
    ny_map.add_data(data=map_data,name='NY Properties')
    keplergl_static(ny_map,width=1250)
else:
    ny_map = KeplerGl(height=600,config=config_hex)
    ny_map.add_data(data=map_data,name='NY Properties')
    keplergl_static(ny_map,width=1250)


## Credits
space_left,badge_column = st.sidebar.columns([0.2,2.0])
with badge_column:
    st.write('')
    st.write('')
    st.title('Find Me!')
    st.write("&nbsp[![Buy me a coffee](https://img.shields.io/badge/GitHub-000013?style=for-the-badge&logo=github&logoColor=white&link=https://tr.linkedin.com/in/andr%C3%A9lamachado)](https://github.com/andre-ls)&nbsp[![Connect](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&link=https://tr.linkedin.com/in/andr%C3%A9lamachado)](https://tr.linkedin.com/in/andrélamachado)")
    st.title('Credits')
    st.write("Icons made by [Iconixar](https://www.flaticon.com/authors/iconixar), [Flat Icons](https://www.flaticon.com/authors/flat-icons), [surang](https://www.flaticon.com/authors/surang) and [Icon Pond](https://www.flaticon.com/authors/icon-pond), found on [FlatIcon](https://www.flaticon.com/).")



