import streamlit as st
from generate import gen


# image_url = ""

def main():
    st.title("Generate Image")
    st.markdown(
        "This mini-app generates Tweets using OpenAI's GPT-3 based [Davinci model](https://beta.openai.com/docs/models/overview) for texts and [DALL·E](https://beta.openai.com/docs/guides/images) for images. You can find the code on [GitHub](https://github.com/kinosal/tweet) and the author on [Twitter](https://twitter.com/kinosal)."
    )

    topic = st.text_input(label="Describe your image", placeholder="Rick and Morty in Clockwork World")

    st.button(label='Generate',
              on_click=gen(topic))


if __name__ == '__main__':
    main()
