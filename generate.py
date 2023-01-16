import auth_key
import openai
import streamlit as st

openai.api_key = auth_key.KEY


def gen(topic):
    if not topic:
        st.session_state.text_error = "Please enter a topic"
        return
    response = openai.Image.create(
        prompt=topic,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']

    st.image(image_url)
