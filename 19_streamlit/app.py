import streamlit as st
import pandas as pd
import numpy as np

## title of the application
st.title("hello streamlit")

#display simple text
st.write("this is a simple text")

df = pd.DataFrame({
    'first':[1,2,3,4],
    'second':[10,20,30,40]
})

st.write(" this is the data frame: ")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)