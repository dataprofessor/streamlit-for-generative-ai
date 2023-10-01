import streamlit as st
from PIL import Image
from utilities import load_css
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Welcome to the Streamlit for LLM course",
    page_icon="🏠",
)

load_css()

img = Image.open('img/course-logo.png')
st.image(img, width=400)

# About
st.header('About')
st.info('The Streamlit for Generative AI course will show you how to use Streamlit to build large language model (LLM) powered apps. Finally you can deploy the Streamlit app to the cloud and share with the community.')

# Table of Contents
st.header('Table of Contents')

if st.button('**Lesson 0** - Getting up to speed with Streamlit'):
    switch_page('Lesson_0_Intro_to_Streamlit')
if st.button('**Lesson 1** - An introduction to Generative AI'):
    switch_page('Lesson_1_Intro_to_Gen_AI')
if st.button('**Lesson 2** - Using LLM models from OpenAI'):
    switch_page('Lesson_2_Using_LLM_models')
if st.button('**Lesson 3** - Build a HugChat chatbot'):
    switch_page('Lesson_3_Using_open_source_LLM')
if st.button('**Lesson 4** - Using hosted open source LLM models from Replicate'):
    switch_page('Lesson_4_Using_hosted_LLM')
if st.button('**Lesson 5** - Orchestrating an LLM workflow with LangChain'):
    switch_page('Lesson_5_Orchestrating_LLM_workflow')
if st.button('**Project 1** - Build a ChatGPT clone'):
    switch_page('Project_1_ChatGPT_clone')
if st.button('**Project 2** - Build a Llama 2 chatbot'):
    switch_page('Project_2_Llama_2_chatbot')
if st.button('**Project 3** - Build a HugChat chatbot'):
    switch_page('Project_3_HugChat_chatbot')
if st.button('**Project 4** - Build a Code Llama chatbot'):
    switch_page('Project_4_Code_Llama_chatbot')
