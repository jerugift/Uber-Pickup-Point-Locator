# -*- coding: utf-8 -*-
"""Uber trips in New York in April 2014"""

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import folium as fol
from sklearn.cluster import KMeans

uber_ride=pd.read_csv(r"uber-raw-data-apr14.csv")
#uber_ride

print(f'Number of trips : {uber_ride.shape[0]}')

plt.scatter(uber_ride.iloc[:,1],uber_ride.iloc[:,2])
plt.show()

wcss=[]
for i in range(1,11):
  kmeans=KMeans(n_clusters=i,random_state=1)
  kmeans.fit(uber_ride[['Lat','Lon']])
  wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
plt.plot(range(1,11),wcss, marker='o')
plt.xticks(ticks=list(range(1,11)))
plt.title("Elbow Method", fontsize=17)
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

kmeans=KMeans(n_clusters=7,random_state=1)
kmeans.fit_predict(uber_ride[['Lat','Lon']])

plt.scatter(uber_ride.iloc[:,2],uber_ride.iloc[:,1],c='blue')
plt.scatter(kmeans.cluster_centers_[:,1],kmeans.cluster_centers_[:,0],s=100,c='orange')
plt.show()

centroids=pd.DataFrame(kmeans.cluster_centers_)
#centroids

centroids.columns=[['Lat','Lon']]
#centroids

plt.scatter(centroids['Lon'],centroids['Lat'], marker="*", c="red")
plt.show()



cen_val=centroids.values.tolist()
cen_names=["Pickup Point 1","Pickup Point 2","Pickup Point 3","Pickup Point 4","Pickup Point 5","Pickup Point 6","Pickup Point 7"]
#cen_val,cen_names

cen_dict={ "Pickup Point 1": [40.68858765865063, -73.9656936740147],
 "Pickup Point 2":[40.7654230768519, -73.97316457280853],
 "Pickup Point 3":[40.78800052141339, -73.87985791232155],
 "Pickup Point 4":[40.656997454878734, -73.78003546954315],
 "Pickup Point 5":[40.731074052287056, -73.99864377251673],
 "Pickup Point 6":[40.70054140415895, -74.20167302861849],
 "Pickup Point 7":[40.97122854230377, -73.6112875637105]}
#cen_dict

for value in cen_dict.values():
  print(value)


nyc_map=fol.Map(location=[40.78800052141339, -73.87985791232155])
#nyc_map

for point in range(len(cen_val)):
  fol.Marker(cen_val[point],popup=cen_val[point],icon=fol.Icon(color='green',icon='arrow-right')).add_to(nyc_map)
#nyc_map

# The marked points are the pickup points
# Based on the location of the customer, Uber will send a driver from the nearest centroid aka pickup points

st.title("Uber Pick-up Point Locator")

# Finding the closest cluster for Lincoln Center for the Performing Arts in the borough of Manhattan:

LincolnCenter=[[40.7725,-73.9835]]
pred=kmeans.predict(LincolnCenter)

nyc_map=fol.Map(location=[40.78800052141339, -73.87985791232155])
for point in range(len(cen_val)):
  fol.Marker(cen_val[point],popup=cen_val[point],icon=fol.Icon(color='green',icon='arrow-right')).add_to(nyc_map)

fol.Marker(LincolnCenter[0],popup="Lincoln Center",icon=fol.Icon(color='red',icon="star")).add_to(nyc_map)
fol.Marker(cen_val[pred[0]],popup=cen_names[pred[0]],icon=fol.Icon(color='black',icon="arrow-right")).add_to(nyc_map)
nyc_map


HowardBeach=[[40.6571, -73.8430]]
pred=kmeans.predict(HowardBeach)

nyc_map=fol.Map(location=[40.78800052141339, -73.87985791232155])
for point in range(len(cen_val)):
  fol.Marker(cen_val[point],popup=cen_val[point] ,icon=fol.Icon(color='green',icon='arrow-right')).add_to(nyc_map)

fol.Marker(HowardBeach[0],popup="Howard Beach",icon=fol.Icon(color='red',icon='star')).add_to(nyc_map)
fol.Marker(cen_val[pred[0]],popup=cen_names[pred[0]],icon=fol.Icon(color='black',icon="arrow-right")).add_to(nyc_map)
nyc_map

#colors that work in fol.Icon:
# colors = [
#     'red',
#     'blue',
#     'gray',
#     'darkred',
#     'lightred',
#     'orange',
#     'beige',
#     'green',
#     'darkgreen',
#     'lightgreen',
#     'darkblue',
#     'lightblue',
#     'purple',
#     'darkpurple',
#     'pink',
#     'cadetblue',
#     'lightgray',
#     'black'
# ]


