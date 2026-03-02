import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard de anuncios de coches")

df = pd.read_csv("vehicles_us.csv")

show_top10 = st.checkbox("Mostrar Top 10 vehículos")
show_cheap10= st.checkbox("Mostrar Top 10 vehículos baratos")
build_hist = st.checkbox("Mostrar histograma del odómetro")
build_scatter = st.checkbox("Mostrar gráfico de dispersión precio vs odómetro")
show_types2 = st.checkbox("Mostrar distribución de vehículos por tipo")
show_avg_price = st.checkbox("Mostrar precio promedio por tipo de vehículo")

if show_top10:
    st.write("Los 10 vehículos con mayor precio en el dataset")
    
    # Ordenar por precio descendente
    top10 = df.sort_values(by="price", ascending=False).head(10)
    
    # Seleccionar columnas importantes
    top10 = top10[[
        "price",
        "model_year",
        "model",
        "type",
        "odometer",
        "condition"
    ]]
if show_cheap10:
    st.write("Los 10 vehículos con menor precio en el dataset")
    cheap10 = df.sort_values(by="price", ascending=True).head(10)
    
    # Seleccionar columnas importantes
    cheap10 = cheap10[[
        "price",
        "model_year",
        "model",
        "type",
        "odometer",
        "condition"
    ]]

    st.dataframe(cheap10, use_container_width=True)
if build_hist:
    st.write("Distribución del kilometraje")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write("Relación precio vs kilometraje")
    fig2 = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)

if show_types2:
    st.write("Cantidad de vehículos por tipo")
    
    # Conteo por tipo
    type_counts = df['type'].value_counts().reset_index()
    type_counts.columns = ['type', 'count']
    
    fig = px.bar(
        type_counts,
        x='type',
        y='count',
        title='Distribución de vehículos por tipo',
        labels={'type': 'Tipo de vehículo', 'count': 'Cantidad'}
    )
    
    st.plotly_chart(fig, use_container_width=True)

if show_avg_price:
    st.write("Precio promedio por tipo")
    
    avg_price = df.groupby('type')['price'].mean().reset_index()
    
    fig2 = px.bar(
        avg_price,
        x='type',
        y='price',
        title='Precio promedio por tipo de vehículo',
        labels={'type': 'Tipo de vehículo', 'price': 'Precio promedio'}
    )
    
    st.plotly_chart(fig2, use_container_width=True)