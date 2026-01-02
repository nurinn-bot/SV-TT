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

# Create a sub-dataframe with only 'Scarcity' and 'Serendipity'
correlation_data = df[['Scarcity', 'Serendipity']]

# Calculate the correlation matrix
correlation_matrix = correlation_data.corr()

# Create interactive heatmap
fig = px.imshow(
    correlation_matrix,
    text_auto=".2f",
    color_continuous_scale="RdBu",
    zmin=-1,
    zmax=1,
    width=600,
    height=500
)

fig.update_layout(
    title="Correlation Heatmap Between Scarcity and Serendipity Scores",
    xaxis_title="Variables",
    yaxis_title="Variables"
)

fig.show()
