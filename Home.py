import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/me2.jpg", width=400)

with col2:
    st.title("Ahamed Nadeem")
    st.header("3rd Year, EEE")
    content1 = """
    Hi, I am Ahamed Nadeem. I am a Python Developer and a DL Enthusiast. I am currently doing my bachelors from PSG Institute 
    of Technology and Applied Research. I have working in Deep Learning project which classifies Diseases in Heart using
    different Algorithms. I love coding and that's what i do most of the time. My current CGPA is 8.96. My hobbies are 
    solving cube, solving python problems in coding platforms and listening to music.
    """
    st.info(content1)

content2 = """These are some of my works, feel free to contact me"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")





