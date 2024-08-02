import streamlit as st
from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv('API_KEY') 

voice_options = {
    "Alloy": "alloy",
    "Nova": "nova",
    "Echo": "echo",
    "Fable": "fable",
    "Onyx": "onyx",
    "Shimmer": "shimmer"
}
st.title("Text to Speech Converter")
voice = st.selectbox("Choose a voice type", list(voice_options.keys()))
text_to_synthesize = st.text_area("Enter the text to convert into audio", height=200)

if st.button("Generate Audio"):
    if not text_to_synthesize:
        st.error("Please enter some text.")
    else:
        selected_voice = voice_options[voice]
        try:
            response = openai.audio.speech.create(
                model="tts-1",
                input=text_to_synthesize,
                voice=selected_voice
            )
            audio_file_path = "output.mp3"
            with open(audio_file_path, "wb") as audio_file:
                audio_file.write(response.content)
            st.success("Audio file created")
            st.audio(audio_file_path)

            with open(audio_file_path, "rb") as audio_file:
                btn = st.download_button(
                    label="Download Audio",
                    data=audio_file,
                    file_name="output.mp3",
                    mime="audio/mpeg"
                )
        except Exception as e:
            st.error(f"Error generating audio: {e}")
