import streamlit as st
from utilities import load_css, read_md

st.set_page_config(page_title="Lesson 1 - An introduction to Generative AI", page_icon="📖", layout="wide")

load_css()

md = read_md('Lesson-1.md')
st.markdown(md, unsafe_allow_html=True)
