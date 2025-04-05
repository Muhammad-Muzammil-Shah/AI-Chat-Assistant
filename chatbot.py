import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import requests
import tempfile

# Configuration
GROQ_API_KEY = "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"
GROQ_MODEL = "llama3-70b-8192"

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.markdown("""
    <style>
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        background-color: #1e1e1e;
        color: white;
        padding: 1rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
    }
    .user-message, .bot-message {
        margin-bottom: 1rem;
        padding: 0.75rem;
        border-radius: 0.5rem;
    }
    .user-message {
        background-color: #2a2a2a;
        text-align: right;
    }
    .bot-message {
        background-color: #3a3a3a;
        text-align: left;
    }
    .chat-input {
        display: flex;
        gap: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Chat Assistant")

# Initialize chat history if not present
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history with audio included
def display_chat_history():
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for entry in st.session_state.chat_history:
        role_class = "user-message" if entry['role'] == "user" else "bot-message"
        st.markdown(f"<div class='{role_class}'>{entry['content']}</div>", unsafe_allow_html=True)
        
        # Check if there is an audio file and display it
        if 'audio' in entry:
            st.audio(entry['audio'], format='audio/mp3')
    st.markdown("</div>", unsafe_allow_html=True)

display_chat_history()

# Input method
method = st.radio("Input Method", ["Text", "Voice"], horizontal=True)

if method == "Text":
    user_input = st.text_input("", placeholder="Type your message here...", label_visibility="collapsed")
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                *[{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.chat_history]
            ],
            "model": GROQ_MODEL
        }

        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

        if response.status_code == 200:
            reply = response.json()["choices"][0]["message"]["content"]
            st.session_state.chat_history.append({"role": "assistant", "content": reply})

            tts = gTTS(text=reply, lang='en')
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                st.session_state.chat_history[-1]['audio'] = fp.name
            
            # Display updated chat history immediately after new input
            display_chat_history()
        else:
            st.error("API Error")

elif method == "Voice":
    if st.button("🎤 Record Voice"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("Listening...")
            audio = recognizer.listen(source)
            st.success("Processing...")

        try:
            user_input = recognizer.recognize_google(audio)
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    *[{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.chat_history]
                ],
                "model": GROQ_MODEL
            }

            response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)

            if response.status_code == 200:
                reply = response.json()["choices"][0]["message"]["content"]
                st.session_state.chat_history.append({"role": "assistant", "content": reply})

                tts = gTTS(text=reply, lang='en')
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                    tts.save(fp.name)
                    st.session_state.chat_history[-1]['audio'] = fp.name

                # Display updated chat history immediately after new input
                display_chat_history()
            else:
                st.error("API Error")
        except Exception as e:
            st.error(f"Voice error: {e}")
