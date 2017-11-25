# coding=utf-8
"""
Mapping application with markers in folium
"""

import folium
import pandas as pd

VOLC_TXT = 'Volcanoes_USA.txt'
WORLD_JSON = 'world.json'
data = pd.read_csv(VOLC_TXT)
# print(data)
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'



map = folium.Map(location=[37.972885, -122.340542])
fg = folium.FeatureGroup(name='Locations of Notable Zelda Players')
fg.add_child(folium.Marker(location=[37.972885, -122.340542], popup='Hello BigChris35'))
fg.add_child(folium.Marker(location=[37.363498, -121.914129], popup='Viktor Big Diktor'))
fg.add_child(folium.Marker(location=[37.310257, -122.029813], popup='Gold Darius Penta'))
fg.add_child(folium.Marker(location=[37.404852, -121.892283], popup='Singed Main'))

fe = folium.FeatureGroup(name='Flat Earthers United')
for i in range(30):
    for j in range(30):
        fe.add_child(folium.Marker(location=[50 + 2*i, -100 + 2*j], popup='Grid'))

fgv = folium.FeatureGroup(name='Volcanoes')
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            radius=6,
            popup=str(el) + ' m',
            fill_color=color(el),
            fill=True,
            color='grey',
            fill_opacity=0.7))

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(
    folium.GeoJson(
        data=open(
            WORLD_JSON,
            'r',
            encoding='utf-8-sig').read(),
        style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(fg)
map.add_child(fe)
map.add_child(folium.LayerControl())
map.save('map1.html')

