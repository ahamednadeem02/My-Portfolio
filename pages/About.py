import streamlit as st

st.set_page_config(layout="wide")
st.header("ABOUT ME")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me2.jpg", width=400)

with col2:
    st.subheader("<---Ahamed Nadeem")
    content1 = """
    Hi, I am Ahamed Nadeem. I am a Python Developer and a DL Enthusiast. I am currently doing my bachelors from PSG Institute 
    of Technology and Applied Research. I have working in Deep Learning project which classifies Diseases in Heart using
    different Algorithms. I love coding and that's what i do most of the time. My current CGPA is 8.96. My hobbies are 
    solving cube, solving python problems in coding platforms and listening to music.
    """
    st.info(content1)