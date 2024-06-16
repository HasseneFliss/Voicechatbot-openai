# Voice based ChatBot with Openai models
![image](https://github.com/GayaaniD/Voicechatbot-openai/assets/125920863/dd0fc455-bbc4-4341-8b0f-c01d7d129928)

In the era of AI and Machine Learning, chatbots have become a crucial part of our digital experience. They are everywhere, from customer service to virtual assistants. Today, I’m excited to share my latest project — a Voice-based Chatbot that takes this experience to the next level.

This Bot seamlessly integrates three key components: Speech-to-Text transcription, Text-Based conversation generation, and Text-to-Speech synthesis. It understands spoken language, responds intelligently in text, and then converts these text responses back into spoken words, creating a seamless voice chat experience.

## Key components 
### 1. [Whisper](https://platform.openai.com/docs/guides/speech-to-text) :
  - The Audio API provides two speech to text endpoints, transcriptions and translations, based on state-of-the-art open source large-v2 Whisper model. They can be used to:
    - Transcribe audio into whatever language the audio is in.
    - Translate and transcribe the audio into English.
  - File uploads are currently limited to 25 MB and the following input file types are supported: mp3, mp4, mpeg, mpga, m4a, wav, and webm.
  - In this project, the whisper model is employed for accurate speech-to-text conversion, Whisper excels in transcribing audio inputs into text with remarkable precision.

### 2. [GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5-turbo) : 
  - As the backbone of the text-based conversation generation, GPT-3.5 Turbo harnesses the power of advanced natural language processing to generate contextually relevant responses.

### 3. [TTS-1](https://platform.openai.com/docs/guides/text-to-speech) :
  - The Audio API provides a speech endpoint based on our TTS (text-to-speech) model. It comes with 6 built-in voices and can be used to:
    - Narrate a written blog post
    - Produce spoken audio in multiple language
    - Give real time audio output using streaming
  - Utilised for converting text responses into lifelike speech, TTS-1 delivers synthesised audio outputs that closely resemble human speech patterns.
  - *Voice options : alloy, echo, fable, onyx, nova, and shimmer*
  - *Models : tts-1, tts-1-hd. For real-time applications, the standard tts-1 model provides the lowest latency but at a lower quality than the tts-1-hd model. Due to the way the audio is generated, tts-1 is likely to generate content that has more static in certain situations than tts-1-hd.*

### UI Framework :
  - The user interface is built using [Streamlit](https://docs.streamlit.io/get-started/tutorials/create-an-app), a versatile framework known for its simplicity and ease of use. Streamlit provides an intuitive platform for users to interact with the Voice ChatBot effortlessly. [Streamlit audio recorder](https://pypi.org/project/audio-recorder-streamlit/) is used for recording the audio from user.

## Project Flow
  - Speech-to-Text Transcription:
  Create a function to convert speech to text using OpenAI's Whisper model. Open the audio file in binary read mode and use the client to transcribe the audio into text.
  
  - Text-Based Conversation Generation:
  Implement a function to generate conversational responses using the OpenAI GPT-3.5-turbo model. This function takes the transcribed text and generates a contextually relevant response based on predefined prompts.
  
  - Text-to-Speech Synthesis:
  Develop a function to convert text back into speech using OpenAI's text-to-speech model. The generated speech is streamed into a file, which is then read as binary data and returned for playback.
  
  - Streamlit UI:
  Set up a user interface using Streamlit. The UI includes an audio recorder for capturing voice input, which is then saved as a temporary file. When the 'Get Response' button is clicked, the application transcribes the audio to text, generates a response, and converts this response back to audio. The UI displays the original transcription, the generated text response, and plays the audio response.

## How to Run the Project
1. Clone the GitHub repository.
2. Rename the `.env.example` file to `.env` and add your API keys.
3. Install the project dependencies by running the `requirements.txt` file. You can do this by opening your terminal and typing:
    ```
    pip install -r requirements.txt
    ```
4. After the dependencies are installed, you can run the project using;
   ```
   streamlit run app.py
   ```
   
## Demo
[Watch Demo Video Here!!](https://www.linkedin.com/posts/gayaani_ai-voicetech-innovation-activity-7191309969688793089-oyuj?utm_source=share&utm_medium=member_desktop "Voice ChatBot Demo Video")
