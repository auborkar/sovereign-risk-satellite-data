import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def load_page():
    country = st.selectbox('Select Country',['Argentina','United Kingdom','Germany','Chile'])
    dataset = st.selectbox('Select Dataset',['Country ESI','Drought Index'])

    markdown_html_1=f"""
    <h4 align = 'left'><b>{dataset} data for {country}     
    """
    st.markdown(markdown_html_1, unsafe_allow_html=True)


    m=folium.Map([-43.355896, -68.1900307],
    tiles=None,
    overlay=False,
    zoom_start=4,
    max_bounds=True
    )

    folium.TileLayer(tiles='https://api.mapbox.com/styles/v1/amoghb/cj3bmt49y00002rjswkb16mn5/tiles/256/{z}/{x}/{y}@2x?access_token=pk.eyJ1IjoiYW1vZ2hiIiwiYSI6ImNqMDBsaGI1dzAwNmgycXBmY2VqcGN3ZDgifQ.7CJzZE2LOTdZOuSDPyziPg',
    max_bounds=True,
    zoom_start=3,
    min_zoom=3,
    name='Mapbox Tiles',attr='mapbox').add_to(m)

    provinces_esi = pd.read_csv("provinces_esi.csv")

    # Add icons
    for i in range(0,len(provinces_esi),1):
        lat = provinces_esi.iloc[i]['Latitude']
        lon = provinces_esi.iloc[i]['Longitude']
        folium.Marker([lat,lon], tooltip="ESI").add_to(m)

    st_data = st_folium(m,width=500,height=300)

    download_button = st.button("Download Data")

