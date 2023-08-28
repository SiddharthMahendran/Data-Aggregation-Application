#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd

# Set page title and icon
st.set_page_config(page_title="Data Aggregation App", page_icon="📊")

st.markdown("""
<style>
.light {
    background-color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)

# Load data
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx"])

# Main app content
st.title("Data Aggregation App")

if uploaded_file is not None:
    file_extension = uploaded_file.name.split(".")[-1]

    if file_extension == "csv":
        df = pd.read_csv(uploaded_file)
    elif file_extension == "xlsx":
        df = pd.read_excel(uploaded_file, engine="openpyxl")
    else:
        st.error("Unsupported file format")

    # User interface for aggregation
    if file_extension == "csv" or file_extension == "xlsx":
        st.subheader("Select Columns and Aggregation Operation")

        selected_columns = st.multiselect("Select columns for aggregation", df.columns)
        aggregation_option = st.radio("Select aggregation operation", ["SUM", "COUNT", "AVG"])

        if st.button("Perform Aggregation"):
            st.subheader("Aggregated Results:")
            if aggregation_option == "SUM":
                st.write(df[selected_columns].sum())
            elif aggregation_option == "COUNT":
                st.write(df[selected_columns].count())
            elif aggregation_option == "AVG":
                st.write(df[selected_columns].mean())





