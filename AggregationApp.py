#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd

# Set page title and icon
st.set_page_config(page_title="Data Aggregation App", page_icon="📊")

# Load data
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx"])

# Main app content
st.title("Data Aggregation App")

# Define df variable outside the if statement
df = None
selected_columns = None  # Define selected_columns initially

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]

    if file_extension == "csv":
        df = pd.read_csv(uploaded_file)
    elif file_extension == "xlsx":
        df = pd.read_excel(uploaded_file, engine="openpyxl")
    else:
        st.error("Unsupported file format")
        st.stop()  # Stop execution to prevent further processing

    # Check for non-numeric data in selected columns
    selected_columns = st.multiselect("Select columns for aggregation", df.columns)

    non_numeric_columns = []
    for column in selected_columns:
        if not pd.to_numeric(df[column], errors="coerce").notna().all():
            non_numeric_columns.append(column)

    if non_numeric_columns:
        st.error(f"Unsupported data type in columns: {', '.join(non_numeric_columns)}")
        st.stop()  # Stop execution if non-numeric characters are found
        
# User interface for aggregation
st.subheader("Select Columns and Aggregation Operation")

# Continue using the same selected_columns variable
if selected_columns is not None:
    aggregation_option = st.radio("Select aggregation operation", ["SUM", "COUNT", "AVG"])

    if st.button("Perform Aggregation"):
        st.subheader("Aggregated Results:")
        if aggregation_option == "SUM":
            st.write(df[selected_columns].sum())
        elif aggregation_option == "COUNT":
            st.write(df[selected_columns].count())
        elif aggregation_option == "AVG":
            st.write(df[selected_columns].mean())
