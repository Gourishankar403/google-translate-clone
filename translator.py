import streamlit as st

from deep_translator import GoogleTranslator

language_codes={
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar',
    'armenian': 'hy', 'assamese': 'as', 'azerbaijani': 'az', 'bengali': 'bn',
    'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW',
    'dutch': 'nl', 'english': 'en', 'french': 'fr', 'german': 'de',
    'greek': 'el', 'gujarati': 'gu', 'hindi': 'hi', 'italian': 'it',
    'japanese': 'ja', 'kannada': 'kn', 'korean': 'ko', 'malayalam': 'ml',
    'marathi': 'mr', 'portuguese': 'pt', 'punjabi': 'pa', 'russian': 'ru',
    'spanish': 'es', 'tamil': 'ta', 'telugu': 'te', 'urdu': 'ur'
}

st.set_page_config(page_title="Multi-Language Translator",page_icon="🌐")


st.title("Multi Language Text Translator")

st.write("Enter your text below and choose the language")


text_input=st.text_area("Text to Translate",height=150)
lang_options=list(language_codes.keys())
selected_lang=st.selectbox("Choose the Language",lang_options)


if st.button("Translate"):
    if text_input.strip()=="":
        st.warning("Please enter text to translate")
    else:
        lang_code=language_codes.get(selected_lang.lower())
        try:
            translator = GoogleTranslator(source='auto',target=lang_code)
            translated_text = translator.translate(text_input)
            st.success("Translation Successful!")
            st.text_area("Translated Text", translated_text, height=150)
        except Exception as e:
            st.error(f"Error during translation:{e}")



st.markdown("-----")
st.caption("Built with Python & Streamlit | Powered by Google Translator")
