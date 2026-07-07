import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Page Configuration
st.set_page_config(
    page_title="Titanic Data Dashboard",
    layout="wide"
)

# Title
st.title(" Titanic Data Analysis Dashboard")

st.markdown("""
This dashboard performs basic data analysis on the Titanic dataset using **Pandas** and **Streamlit**.

### Features
- Dataset Preview
- Dataset Information
- Missing Values
- Statistical Summary
- Data Visualizations
""")

st.divider()

# Read Dataset
df = pd.read_csv("titanic.csv")

# Preview
st.header("Dataset Preview")
st.dataframe(df.head())

# Dataset Shape
col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.divider()


# Data Types
st.header(" Column Data Types")
st.dataframe(df.dtypes.astype(str))


# Statistical Summary
st.header("Statistical Summary")
st.dataframe(df.describe())


# Missing Values
st.header("Missing Values")

missing = df.isnull().sum()

st.dataframe(missing)

# Visualization Section
st.header("Visualizations")

col1, col2 = st.columns(2)

# Bar Chart
with col1:

    st.subheader("Passenger Class")

    fig, ax = plt.subplots()

    df["Pclass"].value_counts().sort_index().plot(
        kind="bar",
        ax=ax
    )

    ax.set_xlabel("Class")
    ax.set_ylabel("Passengers")

    st.pyplot(fig)

# Histogram
with col2:

    st.subheader("Age Distribution")

    fig, ax = plt.subplots()

    df["Age"].dropna().plot(
        kind="hist",
        bins=20,
        ax=ax
    )

    ax.set_xlabel("Age")

    st.pyplot(fig)

st.divider()

# Interactive Section
st.header("Explore Columns")

selected_column = st.selectbox(
    "Choose a column",
    df.columns
)

st.write(df[selected_column])

st.success("Dashboard Loaded Successfully!")