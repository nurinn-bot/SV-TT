import streamlit as st
import pandas as pd
import plotly.express as px

# --- Streamlit Configuration ---
st.set_page_config(
    page_title="Demographic Factors",
    layout="wide"
)

st.header("Demographic Factors on Impulse Buying in TikTok Shop🛍️", divider="blue")

# ######################################################################
# --- 1. DATA LOADING FROM URL (Replaced Dummy Data) ---
url = 'https://raw.githubusercontent.com/nurinn-bot/SV-TT/refs/heads/main/exported_dataframe.csv'

# Load data from the remote CSV file
# Consider using @st.cache_data for improved performance in a real Streamlit app
df = pd.read_csv(url)
)
