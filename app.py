import streamlit as st
from sklearn.datasets import load_iris

data = load_iris(as_frame=True)
df = data.frame

st.title("My first Streamlit app")
st.header("Hello Felipe!")
st.subheader("This is a subheader")
st.write("This is a simple Streamlit app.")

st.dataframe(df)

#put a graph, just the distribution of petal length
st.write("Distribution of petal length")
st.line_chart(df['petal length (cm)'])

#put a graph, just the distribution of petal width
st.write("Distribution of petal width")
st.line_chart(df['petal width (cm)'])
# targethistogram
st.write("target hist")
st.bar_chart(df['target'].value_counts())
