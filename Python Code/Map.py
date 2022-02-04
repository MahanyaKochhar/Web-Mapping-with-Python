import folium

import pandas
from folium import plugins

data=pandas.read_csv("capital.txt")
data2=pandas.read_csv("wonders.txt")
name=list(data2["Name"])
lat1=list(data2["Latitude"])
lon1=list(data2["Longitude"])
lat=list(data["Latitude"])
lon=list(data["Longitude"])
capital=list(data["Capital"])
map=folium.Map(location=[21.19,79.06],zoom_start=5)
folium.raster_layers.TileLayer('Open Street Map').add_to(map)
folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
folium.raster_layers.TileLayer('CartoDB Positron').add_to(map)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(map)
fg=folium.FeatureGroup("Capitals")
fg1=folium.FeatureGroup("Population Density")
fg2=folium.FeatureGroup("7 wonders of the world")
for i,j,k in zip(lat,lon,capital):
    fg.add_child(folium.CircleMarker(location=[i,j],radius=6,popup=k,fill_color='red',color='grey',opacity=0.7))
fg1.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<=x['properties']['POP2005']<20000000 else 'red'}))
for k,l,m in zip(lat1,lon1,name):
    fg2.add_child(folium.Marker(location=[k,l],popup=m,icon=folium.Icon(color='green')))
map.add_child(fg2)
map.add_child(fg1)
map.add_child(fg)
route_lats_longs = [[22.4707, 70.0577],    # Jamnagar
                    [26.9124, 75.7873]]    # Jaipur
fg3=folium.FeatureGroup("Routes")
data3=pandas.read_csv("routes.txt")
src=list(data3["Source"])
dest=list(data3["Desti"])
lats=list(data3["LatS"])
longs=list(data3["LongS"])
latd=list(data3["LatD"])
longd=list(data3["LongD"])
for i,j,k,l,m,n in zip(src,dest,lats,longs,latd,longd):
    plugins.AntPath([[k,l],[m,n]]).add_to(fg3)
    fg3.add_child(folium.CircleMarker(location=[k,l],radius=6,popup=i,fill_color='red',color='grey',opacity=0.7))
    fg3.add_child(folium.CircleMarker(location=[m,n],radius=6,popup=j,fill_color='red',color='grey',opacity=0.7))
map.add_child(fg3)
map.add_child(folium.LayerControl())
mini_map = plugins.MiniMap(toggle_display=True)
map.add_child(mini_map)
map.save("Capital_Cities.html")
