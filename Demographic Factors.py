import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# --- Streamlit Configuration ---
st.set_page_config(
    page_title="Demographic Factors",
    layout="wide"
)

st.header("Demographic Factors on Impulse Buying in TikTok Shop 🛍️", divider="blue")

# --- 1. DATA LOADING FROM URL ---
url = 'https://raw.githubusercontent.com/nurinn-bot/SV-TT/refs/heads/main/TikTok_DataFrame.csv'

df = pd.read_csv(url)

# Calculate the counts and reset the index to create a Plotly-friendly DataFrame
# Assumes the loaded CSV has a column named 'Gender'
gender_counts_df = arts_df['Gender'].value_counts().reset_index()
gender_counts_df.columns = ['Gender', 'Count']

st.write("Data summary (Counts):")
st.dataframe(gender_counts_df, hide_index=True)

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

st.plotly_chart(fig, use_container_width=True)

# Calculate the average Scarcity and Serendipity scores by monthly_income
average_scores_by_income = (
    df.groupby('monthly_income')[['Scarcity', 'Serendipity']]
    .mean()
    .reset_index()
)

# Define the order for income groups
income_order = ['Under RM100', 'RM100 - RM300', 'Over RM300']
average_scores_by_income['monthly_income'] = pd.Categorical(
    average_scores_by_income['monthly_income'],
    categories=income_order,
    ordered=True
)
average_scores_by_income = average_scores_by_income.sort_values('monthly_income')

# Melt the DataFrame for Plotly
melted_scores_income = average_scores_by_income.melt(
    id_vars='monthly_income',
    value_vars=['Scarcity', 'Serendipity'],
    var_name='Score_Type',
    value_name='Average_Score'
)

# Create interactive bar chart
fig = px.bar(
    melted_scores_income,
    x='monthly_income',
    y='Average_Score',
    color='Score_Type',
    barmode='group',
    text_auto='.2f',
    category_orders={'monthly_income': income_order},
    title='Average Scarcity and Serendipity Scores by Monthly Income',
    labels={
        'monthly_income': 'Monthly Income (in RM)',
        'Average_Score': 'Average Score',
        'Score_Type': 'Score Type'
    },
    width=900,
    height=500
)

fig.update_layout(
    xaxis_tickangle=-45,
    legend_title_text='Score Type'
)

st.plotly_chart(fig, use_container_width=True)

# Calculate the average Scarcity and Serendipity scores by gender
average_scores_by_gender = (
    df.groupby('gender')[['Scarcity', 'Serendipity']]
    .mean()
    .reset_index()
)

# Melt the DataFrame for Plotly
melted_scores = average_scores_by_gender.melt(
    id_vars='gender',
    value_vars=['Scarcity', 'Serendipity'],
    var_name='Score_Type',
    value_name='Average_Score'
)

# Create interactive bar chart
fig = px.bar(
    melted_scores,
    x='gender',
    y='Average_Score',
    color='Score_Type',
    barmode='group',
    text_auto='.2f',
    title='Average Scarcity and Serendipity Scores by Gender',
    labels={
        'gender': 'Gender',
        'Average_Score': 'Average Score',
        'Score_Type': 'Score Type'
    },
    width=800,
    height=450
)

fig.update_layout(
    legend_title_text='Score Type'
)

st.plotly_chart(fig, use_container_width=True)

# Create subplots: 1 row, 2 columns
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=[
        "Distribution of Scarcity Score",
        "Distribution of Serendipity Score"
    ]
)

# Box plot for Scarcity
fig.add_trace(
    go.Box(
        y=df['Scarcity'],
        name='Scarcity',
        boxmean=True
    ),
    row=1, col=1
)

# Box plot for Serendipity
fig.add_trace(
    go.Box(
        y=df['Serendipity'],
        name='Serendipity',
        boxmean=True
    ),
    row=1, col=2
)

# Layout adjustments
fig.update_layout(
    height=500,
    width=900,
    showlegend=False
)

fig.update_yaxes(title_text="Scarcity Score", row=1, col=1)
fig.update_yaxes(title_text="Serendipity Score", row=1, col=2)

st.plotly_chart(fig, use_container_width=True)

# Create subplots
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=[
        "Distribution of Scarcity Score",
        "Distribution of Serendipity Score"
    ]
)

# Histogram for Scarcity
fig.add_trace(
    go.Histogram(
        x=df['Scarcity'],
        nbinsx=5,
        name='Scarcity',
        opacity=0.75
    ),
    row=1, col=1
)

# Histogram for Serendipity
fig.add_trace(
    go.Histogram(
        x=df['Serendipity'],
        nbinsx=5,
        name='Serendipity',
        opacity=0.75
    ),
    row=1, col=2
)

# Layout adjustments
fig.update_layout(
    height=500,
    width=950,
    showlegend=False
)

fig.update_xaxes(title_text="Scarcity Score", row=1, col=1)
fig.update_xaxes(title_text="Serendipity Score", row=1, col=2)
fig.update_yaxes(title_text="Frequency")

st.plotly_chart(fig, use_container_width=True)
