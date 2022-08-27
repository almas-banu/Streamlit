import streamlit as st
import pandas as pd
import numpy as np
import home
st.title("Pub Locations")
st.header('Select a Local Authority or Postal Code')

option=st.selectbox('Which one ?',('Local Authority','Postal Code'))
'You selected: ',option

#Local Authority
if option == 'Local Authority':
    option=st.selectbox('Select a Location authority',home.data_loc)
    'You selected: ',option
    button_click=st.button('Find now')
    if button_click==True:
        df_loc=home.df[home.df['local_authority']==option]
        count=df_loc.shape[0]
        st.write('Number of Pubs in this area is: ', count)
        df_loc=df_loc[['latitude','longitude']]
        st.map(df_loc)
        
#Postal Code
if  option == 'Postal Code':
    option=st.selectbox('Select a Postal code',home.data_pos)
    'You selected: ',option
    button_click=st.button('Find now')
    if button_click==True:
        df_post=home.df[home.df['postcode']==option]
        count=df_post.shape[0]
        st.write('Number of Pubs in the',option,'area is : ',count)
        df_post=df_post[['latitude','longitude']]
        st.map(df_post)