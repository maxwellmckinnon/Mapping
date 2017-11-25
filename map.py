# coding=utf-8
"""
Mapping application with markers in folium
"""

import folium

map = folium.Map(location=[37.972885, -122.340542])
fg = folium.FeatureGroup(name="Locations of Notable Zelda Players")
fg.add_child(folium.Marker(location=[37.972885, -122.340542], popup="Hello BigChris35"))
fg.add_child(folium.Marker(location=[37.363498, -121.914129], popup="Viktor Big Diktor"))
fg.add_child(folium.Marker(location=[37.310257, -122.029813], popup="Gold Darius Penta"))

fe = folium.FeatureGroup(name="Flat Earthers United")
for i in range(30):
    for j in range(30):
        fe.add_child(folium.Marker(location=[50 + 2*i, -100 + 2*j], popup="Grid"))

map.add_child(fg)
map.add_child(fe)
map.save("map1.html")

