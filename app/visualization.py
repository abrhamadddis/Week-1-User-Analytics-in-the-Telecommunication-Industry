import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from other_module import fetch_data, create_conn
"""
    function that plot top 10 handsets type and it's count
"""
def create_top_10_handsets_chart(data):
    top_10_handsets = data['Handset Type'].value_counts().head(10)
    fig = px.bar(top_10_handsets, x=top_10_handsets.index, y=top_10_handsets.values, labels={'x': 'Handset Type', 'y': 'Count'})
    fig.update_layout(title='Top 10 Handsets')
    st.plotly_chart(fig)
"""
    function that plot top 3 manufacturers with it's count 
"""
def create_top_3_manufacturers_chart(data):
    top_3_manufactures = data['Handset Manufacturer'].value_counts().head(3)
    fig = px.bar(top_3_manufactures, x=top_3_manufactures.index, y=top_3_manufactures.values, labels={'x': 'Manufacturer', 'y': 'Count'})
    fig.update_layout(title='Top 3 Handset Manufacturers')
    st.plotly_chart(fig)
"""
    function that plot top 5 handsets per manufacturer with it's type
"""
def create_top_5_handsets_per_manufacturer_chart(data):
    top_3_manufacturers = data['Handset Manufacturer'].value_counts().head(3).index
    filtered_data = data[data['Handset Manufacturer'].isin(top_3_manufacturers)]

    top_5_handsets_per_manufacturer = filtered_data.groupby(['Handset Manufacturer', 'Handset Type']).size().reset_index(name='Count')

    fig = go.Figure(data=go.Heatmap(
        z=top_5_handsets_per_manufacturer['Count'],
        x=top_5_handsets_per_manufacturer['Handset Manufacturer'],
        y=top_5_handsets_per_manufacturer['Handset Type'],
        colorscale='Viridis',
        colorbar=dict(title='Count'),
    ))

    fig.update_layout(title='Top 5 Handsets per Manufacturer',
                      xaxis=dict(title='Manufacturer'),
                      yaxis=dict(title='Handset Type'))

    st.plotly_chart(fig)




