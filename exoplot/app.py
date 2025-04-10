import streamlit as st
import pandas as pd

exoplanets = pd.read_csv('exoplanet_archive.csv', comment='#')


st.title('Exoplanet Plotting App')
st.write('This is a simple app to plot exoplanet data.')
st.write('Upload your data file and select the plot type you want to create.')


st.sidebar.header('User Input')

x_axis = st.sidebar.selectbox('Select x axis', ['Mass', 'Radius', 'Temperature'])


y_axis = st.sidebar.selectbox('Select y axis', ['Mass', 'Radius', 'Temperature'])

st.subheader('Scatter Plot')
st.write('Plotting', x_axis, 'vs.', y_axis)
st.scatter_chart(exoplanets[[x_axis, y_axis]])


