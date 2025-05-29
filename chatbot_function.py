import os
import datetime
from dotenv import load_dotenv
from fastapi.responses import Response
from openai import OpenAI

# Load environment variables from .env file
#load_dotenv()

# Optionally set proxy if needed
# os.environ["HTTP_PROXY"] = "http://your-proxy:port"
# os.environ["HTTPS_PROXY"] = "http://your-proxy:port"

# Initialize OpenAI client using API key from environment
client = OpenAI(api_key="xxxxx")

def speech_to_text_conversion(file_path):
    """
    Converts an audio file to text using OpenAI's Whisper model.
    """
    try:
        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )
        return transcription.text
    except Exception as e:
        print(f"[ERROR] Speech-to-text failed: {e}")
        return ""

def text_chat(text):
    """
    Generates a response from OpenAI Chat API based on the user's message.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"[ERROR] Chat generation failed: {e}")
        return "I'm sorry, I couldn't process that."

def text_to_speech_conversion(text):
    """
    Converts a given text to spoken audio using OpenAI's TTS model.
    Returns binary audio data suitable for streaming.
    """
    if not text:
        print("[ERROR] Empty input text for TTS.")
        return None

    try:
        speech_file_path = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "_speech.webm"
        response = client.audio.speech.create(
            model="tts-1",
            voice="fable",
            input=text
        )
        response.stream_to_file(speech_file_path)

        with open(speech_file_path, "rb") as audio_file:
            audio_data = audio_file.read()

        os.remove(speech_file_path)
        return audio_data

    except Exception as e:
        print(f"[ERROR] Text-to-speech conversion failed: {e}")
        return None
