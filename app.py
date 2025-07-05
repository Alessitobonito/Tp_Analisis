import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.title('Venta de vehículos usados en los Estados Unidos')

st.header("Análisis de vehículos en venta en Estados Unidos")

if st.checkbox('Mostrar histograma de precios'):
    st.write('Histograma interactivo de la columna `price`')
    fig = px.histogram(df, x='price')
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Mostrar gráfico de dispersión odómetro vs precio'):
    st.write('Gráfico de dispersión: Precio vs Kilometraje')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)



