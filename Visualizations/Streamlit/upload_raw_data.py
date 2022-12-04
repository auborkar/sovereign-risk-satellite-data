import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

def load_page():
    markdown_html_1=f"""
    <h4 align = 'left'><b>Upload a .tif file granular satellite images & a corresponding shapefile to aggregate over.     
    """
    st.markdown(markdown_html_1, unsafe_allow_html=True)

    tif_file = st.file_uploader("Upload a .tif file", type='tif')
    shape_file = st.file_uploader("Upload a .shp file", type='shp')
    