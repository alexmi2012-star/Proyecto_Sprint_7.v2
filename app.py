import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard de anuncios de coches")

df = pd.read_csv("vehicles_us.csv")

build_hist = st.checkbox("Mostrar histograma del odómetro")
build_scatter = st.checkbox("Mostrar gráfico de dispersión precio vs odómetro")

if build_hist:
    st.write("Distribución del kilometraje")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write("Relación precio vs kilometraje")
    fig2 = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)