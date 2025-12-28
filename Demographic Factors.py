import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Configuration ---
st.set_page_config(
    page_title="Demographic Factors",
    layout="wide"
)

st.header("Demographic Factors on Impulse Buying in TikTok Shop 🛍️", divider="blue")

# --- 1. DATA LOADING FROM URL ---
url = 'https://raw.githubusercontent.com/nurinn-bot/SV-TT/main/exported_dataframe.csv'

df = pd.read_csv(url)

# --- Distribution of Gender (Pie Chart) ---
gender_counts = df['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']

fig = px.pie(
    gender_counts,
    names='Gender',
    values='Count',
    title='Distribution of Gender',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_traces(textinfo='percent+label')

st.plotly_chart(fig, use_container_width=True)

#--- Relationship Between Age and Average Monthly Income (CountPlot) ---
fig = px.histogram(
    df,
    x='Age',
    color='Average Monthly Income (in RM)',
    barmode='group',
    title='Relationship Between Age and Average Monthly Income',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_layout(
    xaxis_title='Age Group',
    yaxis_title='Count',
    legend_title='Average Monthly Income (in RM)',
    xaxis_tickangle=45
)

st.plotly_chart(fig, use_container_width=True)
