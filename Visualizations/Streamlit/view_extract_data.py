import streamlit as st
import pandas as pd
import folium
from datetime import datetime
import geopandas as gpd
import matplotlib.pyplot as plt #if using matplotlib
import plotly.express as px #if using plotly


def load_page():
    col1, col2 = st.columns(2)
    country = col1.selectbox('Select Country',['Argentina','United Kingdom','Germany','Chile'])
    dataset = col2.selectbox('Select Dataset',['Evapotrative Stress Index','Drought Index'])

    # Read, process and convert the data
    esi_ts = pd.read_csv("time_series.csv")
    esi_ts['geometry'] = gpd.GeoSeries.from_wkt(esi_ts['geometry'])
    esi_ts['date'] = esi_ts['date'].apply(lambda x: datetime.strptime(str(x),'%Y%m%d'))
    argentina_esi_ts = esi_ts.copy(deep=True)
    argentina_esi_ts = argentina_esi_ts[['date','mean_esi']].groupby('date')['mean_esi'].mean()
    argentina_esi_ts = argentina_esi_ts.reset_index()
    argentina_esi_ts = argentina_esi_ts.sort_values(by='date', ascending=True)


    start_date = col1.date_input('From Date',argentina_esi_ts['date'].min())
    end_date = col2.date_input('To Date', argentina_esi_ts['date'].max())

    markdown_html_1=f"""
    <h4 align = 'left'><b>Timeseries at Country level     
    """
    markdown_html_2=f"""
    <h4 align = 'left'><b>Average {dataset} by sub-region over time period     
    """

    col1.markdown(markdown_html_1, unsafe_allow_html=True)
    col2.markdown(markdown_html_2, unsafe_allow_html=True)
    # argentina_esi_plot = argentina_esi_ts[argentina_esi_ts['date'] > start_date]
    # argentina_esi_plot = argentina_esi_plot[argentina_esi_plot['date'] < end_date]

    fig1 = px.bar(argentina_esi_ts, x='date', y="mean_esi")
    col1.plotly_chart(fig1)


    #https://stackoverflow.com/questions/56433138/converting-a-column-of-polygons-from-string-to-geopandas-geometry
    chk_df = gpd.GeoDataFrame(esi_ts, crs="EPSG:4326",geometry='geometry')
    chk_df['geometry'].plot(figsize=(20, 10))

    #Matplotlib plot
    fig, ax = plt.subplots(1, figsize=(3,2))
    chk_df.plot(column='mean_esi', cmap='YlOrRd', linewidth=0.2, ax=ax, edgecolor='0.9', legend = True)
    ax.axis('off')

    col2.pyplot(fig)
    
    download_button = col2.button("Download Regional Data")

