import streamlit as st
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)
df = data.frame

st.title("My first Streamlit app")
st.header("Hello Felipe!")
st.subheader("This is a subheader")
st.write("This is a simple Streamlit app.")

st.dataframe(df)

