# This is a sample Python script.
import streamlit as st
from streamlit_chat import message
import openai


st.title("ChatGPT私有版")
st.sidebar.title("菜单")
clear_button = st.sidebar.button("清除会话", key="clear")

openai.api_key="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"

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = []


def chat_gpt(prompt):
    completion = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=prompt
    )
    response = completion.choices[0].message.comtent
    return response


response_container = st.container()
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("You:", key="input", height=100)
        st.session_state['past'].append(user_input)
        submit_button = st.form_submit_button(label='Send')

    if submit_button and user_input:
        output = chat_gpt(user_input)
        st.session_state['generated'].append(output)

    if st.session_state['generated']:
        with response_container:
            for i in range(len(st.session_state['generated'])):
                message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
                message(st.session_state['generated'][i], key=str(i))
