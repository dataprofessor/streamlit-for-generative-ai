# 🕹️ Project 4 <br> Build a Code Llama chatbot

## What are we building?

In this project, we're going to build a coding chatbot in Python using Streamlit for the frontend and the open source Code Llama LLM model from Meta in the backend.

<p align="center">
   <img src="../img/project-2-demo-app.png" width="65%">
</p>

## Try the app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://code-llama.streamlit.app/)

## Instructions on using the app

Here are instructions for using the app:
- **Step 1.** Go to the Code Llama chatbot at https://code-llama.streamlit.app/ or your own deployed instance
- **Step 2.** Enter your own Replicate API token in the sidebar.
- **Step 3.** Enter a prompt message in the chat input box on the main panel (found at the bottom portion of the page) and hit on `Enter`.

That's it and in a few moments an LLM generated response should be returned as the displayed output.


## Installing prerequisite libraries

We'll be using 2 prerequisite libraries as follows:
```
streamlit
replicate
```

So if you're building locally you can install these 2 libraries via `pip` as follows:

```
pip install streamlit replicate
```

If deploying to Streamlit Community Cloud, you can go ahead and create a `requirements.txt` file containing the 2 lines mentioned above.

## Getting your own OpenAI API key

Please refer to the _Getting your own Replicate API token_ section of **Lesson 4**.

## Building the chatbot app

The code in its entirety is 86 lines of code, which can be saved into your app file (`streamlit_app.py`):

```Python
import streamlit as st
import replicate
import os

# App title
st.set_page_config(page_title="🦙💬 Code Llama Chatbot")

# Replicate Credentials
with st.sidebar:
    st.title('🦙💬 Code Llama Chatbot')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

    st.subheader('Model parameters')
    temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
    top_k = st.sidebar.slider('top_k', min_value=0, max_value=512, value=250, step=1)
    max_length = st.sidebar.slider('max_length', min_value=32, max_value=128, value=128, step=8)
    
    st.markdown('📖 Learn how to build this app in this [blog](https://blog.streamlit.io/how-to-build-a-llama-2-chatbot/)!')
os.environ['REPLICATE_API_TOKEN'] = replicate_api

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating LLaMA2 response
# Refactored from https://github.com/a16z-infra/llama2-chatbot
def generate_llama2_response(prompt_input):
    
    string_dialogue = """
    You are a coding assistant.

    You must follow the following rules strictly in generating your response:
    1. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'. 
    2. When generating the code answer, please encapsulate the code using ```
    3. If you don't know, say you don't know and don't make up stuff.
    4. Make your response concise, to the point and relevant to the question being asked.
    """
    
    for dict_message in st.session_state.messages:
        if dict_message["role"] == "user":
            string_dialogue += "User: " + dict_message["content"] + "\n\n"
        else:
            string_dialogue += "Assistant: " + dict_message["content"] + "\n\n"
    #output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', 
    output = replicate.run('replicate/codellama-7b-instruct:0103579e86fc75ba0d65912890fa19ef03c84a68554635319accf2e0ba93d3ae',
                           input={"prompt": f"{string_dialogue} {prompt_input} Assistant: ",
                                  "temperature":temperature, "top_p":top_p, "top_k":top_k, "max_length":max_length, "repetition_penalty":1.15})
    return output

# User-provided prompt
if prompt := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llama2_response(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
```
