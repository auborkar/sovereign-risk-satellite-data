import numpy as np
import pandas as pd
import streamlit as st
import view_extract_data
import upload_raw_data

seed =10
st.set_page_config(layout='wide')
st.title("Satellite Data Extractor")


with st.sidebar:
    choice = st.sidebar.radio('Select Module',['Upload raw satellite data','View/ Extract Available Data'])

if choice=='Upload raw satellite data':
    upload_raw_data.load_page()
elif choice=='View/ Extract Available Data':
    view_extract_data.load_page()