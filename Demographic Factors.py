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
url = 'https://raw.githubusercontent.com/nurinn-bot/SV-TT/refs/heads/main/cleaned_dataset.csv'

df = pd.read_csv(url)

df['Scarcity'] = df[[
 'promo_deadline_focus',
 'promo_time_worry',
 'limited_quantity_concern',
 'out_of_stock_worry'
]].mean(axis=1)

df['Serendipity'] = df[[
 'product_recall_exposure',
 'surprise_finds',
 'exceeds_expectations',
 'fresh_interesting_info',
 'relevant_surprising_info'
]].mean(axis=1)

df['Trust'] = df[[
 'trust_no_risk',
 'trust_reliable',
 'trust_variety_meets_needs',
 'trust_sells_honestly',
 'trust_quality_matches_description'
]].mean(axis=1)

df['Motivation'] = df[[
 'relax_reduce_stress',
 'motivated_by_discount_promo',
 'motivated_by_gifts'
]].mean(axis=1)

df['BrandDesign'] = df[[
 'similar_to_famous_brand_attraction',
 'new_product_urgency',
 'brand_trust_influence',
 'unique_design_attraction'
]].mean(axis=1)

df['Quality'] = df[[
 'product_description_quality',
 'image_quality_influence',
 'multi_angle_visuals',
 'info_richness_support'
]].mean(axis=1)

df['ImpulseBuying'] = df[[
 'no_purchase_plan',
 'no_purchase_intent',
 'impulse_purchase'
]].mean(axis=1)

# --- Distribution of Gender (Pie Chart) ---
gender_counts = df['gender'].value_counts().reset_index()
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
    x='age',
    color='monthly_income',
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

#--- Impulse Buying Score by age group ---
fig = px.box(
    df,
    x='age',
    y='ImpulseBuying',
    color='age',
    title='Impulse Buying Score by Age Group',
    color_discrete_sequence=px.colors.qualitative.Pastel
)

fig.update_layout(
    xaxis_title='Age Group',
    yaxis_title='Impulse Buying Score',
    showlegend=False
)

fig.update_xaxes(tickangle=45)
fig.update_traces(boxmean='sd')  # shows mean and SD for each box

st.plotly_chart(fig, use_container_width=True)
