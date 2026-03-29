
import streamlit as st
import pandas as pd

st.title("Healthcare AI Platform")

try:
    df=pd.read_csv("data/sample.csv")
    st.write(df.head())
    st.bar_chart(df.select_dtypes(include='number'))
except:
    st.write("Dataset not loaded.")
