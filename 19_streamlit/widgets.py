import streamlit as st
import pandas as pd
import numpy as np

st.title(" streamlit text input and widgets")

name = st.text_input("enter your name: ")
if name:
    st.write(f"hello, {name}")

age = st.slider("select you age: ",0,100,20)

options = ["python","java","C++","javascript"]
choice = st.selectbox("choose your favourite language: ", options)
st.write(f"your favourite language is: {choice}")

uploaded_file = st.file_uploader("choose a CSV file", type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df2 = pd.DataFrame(df)
    st.write(df2)

    