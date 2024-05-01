import streamlit as st
from audio_recorder_streamlit import audio_recorder
import tempfile
import requests
import chatbot_function


st.title('🎙️🤖Voice ChatBot🤖🎙️')

audio_bytes = audio_recorder(
    text="Click to record",
    recording_color="#e8b62c",
    neutral_color="#6aa36f",
    icon_name="microphone",
    icon_size="3x",
)

if audio_bytes:
    print(type(audio_bytes))
    
    st.audio(audio_bytes, format="audio/wav")
    
# Save audio to a temporary file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        temp_audio.write(audio_bytes)
        temp_audio_path = temp_audio.name

    if st.button('🎙️Get Rsponse🎙️'):
         #Converting speech to text
        converted_text_openai = chatbot_function.speech_to_text_conversion(temp_audio_path)
        print("Transcribed text",converted_text_openai)
        st.write("Transcription:",converted_text_openai)
        textmodel_response = chatbot_function.text_chat(converted_text_openai) # Generating actor's response
        print("Response:",textmodel_response)
        audio_data = chatbot_function.text_to_speech_conversion(textmodel_response) #Convert final text response to audio format and get the audio file path

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:  # Creating temporary file
            # contents = await file.read()  # Reading file contents asynchronously
            tmpfile.write(audio_data)  # Writing file contents to temporary file
            tmpfile_path = tmpfile.name
            st.write("Response:",textmodel_response)
            st.audio(tmpfile_path)





