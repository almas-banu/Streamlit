import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="Home", page_icon="https://cdn-icons-png.flaticon.com/512/2/2144.png")

#Loading the dataset
df=pd.read_csv('data/open_pubs.csv')

#Adding releevant column names for dataset
df.columns=['fsa_id','name','address','postcode','easting','northing','latitude','longitude','local_authority']
st.title("Open PUB Application")
st.header("Home Page")
button_click = st.button('Original Dataset')
if button_click == True:
	st.dataframe(df)

#Replacing the null values.
df = df.replace('\\N', np.NaN)
st.write("Are there any null values in dataset?")
button_click = st.button("Check")
if button_click == True:
    st.write(df.isna().sum())
#(Dropping the null value columns)
df=df.dropna()
button_click = st.button('Modified Dataset')
if button_click == True:
	st.dataframe(df)

df[['latitude', 'longitude']]=df[['latitude', 'longitude']].apply(pd.to_numeric, axis = 1)
data_loc=df.local_authority.unique()
data_pos=df.postcode.unique()
pub="Total number of PUBS: "+str(df.shape[0])
auth1="Total number of PUBS in Local Authority: "+str(data_loc.shape[0])
auth2="Total number of PUBS in Post Code: "+str(data_pos.shape[0])

st.sidebar.success("Select Your Page")

st.subheader('Dataset')

option = st.selectbox(
     'What information you want from dataset',
     (' ','Head', 'Tail', 'unique local authority','check null values'))

if option == ' ':
    pass
if option == 'Head':
    st.write(df.head())
if option == 'Tail':
    st.write(df.tail())
if option == 'check null values':
    st.write(df.isnull().sum())
if option == 'unique local authority':
    st.write(df['local_authority'].unique())

button_click = st.button("Describe")

if button_click == True:
    st.dataframe(df.describe())