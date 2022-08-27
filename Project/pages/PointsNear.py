import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np
import home

st.header("Nearest Pub") 
# Calculate the Euclidean distance between two points
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** ( 1 / 2)
 
# Function to calculate K closest points
def KNear(points, target, K):
    temp = []
    n = len(points)
    d = []
 
    for i in range(n):
        d.append({
            "first": distance(points[i][0], points[i][1], target[0], target[1]),
            "second": i
        })
    
    d = sorted(d, key=lambda l:l["first"])
    
    for i in range(K):
        pt = []
        pt.append(points[d[i]["second"]][0])
        pt.append(points[d[i]["second"]][1])
        temp.append(pt)
   
# Calling DataFrame constructor on list
    df_nearest_loc = pd.DataFrame(temp,columns=['latitude','longitude'])
    st.subheader('Nearest 5 Pubs for the Entered Latitude and Longitude')
    st.map(df_nearest_loc)
    

df_lat_log=home.df[['latitude','longitude']]
points = df_lat_log.values.tolist()
lat = st.number_input('Enter Latitude',format="%.5f")
long = st.number_input('Enter Longitude',format="%.6f",key=int)
target = [lat,long]
K = 5

if(lat and long):
    KNear(points, target, K)
