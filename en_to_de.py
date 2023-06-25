import streamlit as st
from transformers import pipeline

def main():
    st.title("English to German Translator")
    st.write("Enter text in English to translate to German:")

    text=st.text_area("Enter Text:",value='',max_chars=None,key=None)

    if st.button('Translate'):
        with st.spinner("Translating..."):
            translated_text=translate(text)
            st.success(translated_text)

def translate(text):
    translator=pipeline("translation_en_to_de")
    result=translator(text)[0]['translation_text']
    return result

if __name__=="__main__":
    main()