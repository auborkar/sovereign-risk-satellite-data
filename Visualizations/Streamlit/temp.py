import pandas as pd
from datetime import datetime
import geopandas as gpd
import matplotlib.pyplot as plt #if using matplotlib
import plotly.express as px #if using plotly

esi_ts = pd.read_csv("time_series.csv")

argentina_esi_ts = esi_ts[['date','mean_esi']].groupby('date')['mean_esi'].mean()
argentina_esi_ts = argentina_esi_ts.reset_index()
argentina_esi_ts['date'] = argentina_esi_ts['date'].apply(lambda x: datetime.strptime(str(x),'%Y%m%d'))
argentina_esi_ts = argentina_esi_ts.sort_values(by='date', ascending=True)
#argentina_esi_ts.index = argentina_esi_ts['date']
#del argentina_esi_ts['date']
#argentina_esi_ts.plot()


fig = px.bar(argentina_esi_ts, x='date', y="mean_esi")
fig.show()




esi_ts['date'] = esi_ts['date'].apply(lambda x: datetime.strptime(str(x),'%Y%m%d'))
esi_ts = esi_ts[esi_ts['date'] == esi_ts['date'].unique()[0]]
esi_ts.head()

#https://stackoverflow.com/questions/56433138/converting-a-column-of-polygons-from-string-to-geopandas-geometry
esi_ts['geometry'] = gpd.GeoSeries.from_wkt(esi_ts['geometry'])
chk_df = gpd.GeoDataFrame(esi_ts, crs="EPSG:4326",geometry='geometry')
chk_df['geometry'].plot(figsize=(20, 10))


# fig, ax = plt.subplots(1, figsize=(10,6))
# chk_df.plot(column='mean_esi', cmap='Blues', linewidth=1, ax=ax, edgecolor='0.9', legend = True)
# ax.axis('off')


fig = px.choropleth(chk_df, geojson=chk_df.geometry, 
                    locations=chk_df.index, color="mean_esi",
                    height=200,
                   color_continuous_scale="ylorrd")
fig.update_geos(fitbounds="locations", visible=True)
fig.update_layout(
    title_text='Map'
)

fig.update(layout = dict(title=dict(x=0.5)))
fig.update_layout(
    margin={"r":0,"t":30,"l":10,"b":10},
    coloraxis_colorbar={
        'title':'Sum'})
# fig.show()
fig.write_image("/images/fig1.png")


# #https://towardsdatascience.com/plot-choropleth-maps-with-shapefiles-using-geopandas-a6bf6ade0a49
# map_df = gpd.read_file('arg_admbnda_adm1_unhcr2017.shp')
# #map_df.to_crs(pyproj.CRS.from_epsg(4326), inplace=True)

# map_df.plot(figsize=(20, 10))

# map_df.head()


