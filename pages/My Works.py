import streamlit as st
import pandas

st.set_page_config(layout="wide")

content2 = "Here are some of my works"
st.header(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.subheader(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")