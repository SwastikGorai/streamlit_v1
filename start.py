import streamlit as st
from generate import gen


# image_url = ""

def main():
    st.title("Generate Image")
    st.markdown(
        "This mini-app generates Images using OpenAI's GPT-3 based model for Images."
    )

    topic = st.text_input(label="Describe your image", placeholder="Rick and Morty in Clockwork World")

    st.button(label='Generate',
              on_click=gen(topic))


if __name__ == '__main__':
    main()
