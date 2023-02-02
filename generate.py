import auth_key
import openai
import streamlit as st

openai.api_key = auth_key.KEY


def gen(topic):
    if not topic:
        st.session_state.text_error = "Please enter a topic"
        return
    with st.spinner("Generating . . ."):
        try:
            response = openai.Image.create(
                prompt=topic,
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            st.image(image_url)
        except openai.error.InvalidRequestError:
            image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2MJanKV-BZsF_47xOBRAbkhLbrH56y5cRoA&usqp=CAU"
            st.image(image_url)
            st.caption('Uh oh. It seems that something is _not_ right. . . 😣😥')







