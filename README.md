# AI Chat Assistant

An AI-powered chat assistant that supports both text and voice inputs. The assistant generates responses using a conversational AI model and provides voice feedback to the user. This project uses **Streamlit** for the UI, **Speech Recognition** for voice input, and **Google Text-to-Speech (gTTS)** for voice output.

---

## Features
- **Text Input**: Users can interact with the assistant by typing text.
- **Voice Input**: Users can speak to the assistant and get a text response.
- **Voice Output**: The assistant will speak its responses using Text-to-Speech.

---

## Table of Contents
1. [Installation Instructions](#installation-instructions)
2. [Running the Project](#running-the-project)
3. [Project Structure](#project-structure)
4. [Dependencies](#dependencies)
5. [License](#license)

---

## Installation Instructions

### 1. Clone the Repository
First, clone this repository to your local machine.

```bash
git clone https://github.com/your-username/ai-chat-assistant.git
cd ai-chat-assistant

```

### 2. Create a Virtual Environment
It’s a good practice to create a virtual environment for your Python projects to manage dependencies.

For **Windows**:
```bash
python -m venv venv
```

For **macOS/Linux**:
```bash
python3 -m venv venv
```

Activate the virtual environment:

For **Windows**:
```bash
.\venv\Scripts\activate
```

For **macOS/Linux**:
```bash
source venv/bin/activate
```

### 3. Install Dependencies
Once the virtual environment is active, install all the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Project

### 1. Set Up API Key
To interact with the **Groq AI API**, you need to set up your API key. Obtain an API key from **Groq** and add it to the `app.py` file.

In the `app.py` file, locate the following line:
```python
GROQ_API_KEY = "your-groq-api-key"
```
Replace `"your-groq-api-key"` with your actual API key.

### 2. Run the Streamlit App
To start the chat assistant, run the following command in your terminal:

```bash
streamlit run chatbot.py
```

This will open the application in your default web browser at `http://localhost:8501`.

---

## Project Structure

```
ai-chat-assistant/
│
├── chatbot.py             # Main application file
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── assets/                # Folder for any media or additional files (if required)
```

---

## Dependencies

Here is a list of Python libraries used in this project:

- **Streamlit**: For building the interactive chat interface.
- **SpeechRecognition**: For converting speech input into text.
- **PyAudio**: Required for capturing audio from the microphone.
- **gTTS (Google Text-to-Speech)**: For converting the assistant's text response into speech.
- **Requests**: To send HTTP requests to the Groq API.
- **Tempfile**: For saving and handling temporary files, used for storing audio files.

To install all dependencies at once, run:

```bash
pip install -r requirements.txt
```

### `requirements.txt`
```
streamlit==1.8.0
SpeechRecognition==3.8.1
PyAudio==0.2.11
gtts==2.2.3
requests==2.26.0
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Troubleshooting

- **Voice Recognition Not Working**:
  - Make sure the microphone is properly set up and accessible on your machine.
  - Ensure that **PyAudio** is installed correctly. If not, you can reinstall it using `pip install pyaudio`.

- **API Errors**:
  - If you receive API errors, ensure that the **Groq API Key** is valid and correctly set in the `app.py` file.

---

## Contributing

Feel free to fork the repository, create a new branch, and submit a pull request with any improvements or bug fixes!
```

Make sure to replace `"your-username"` with your actual GitHub username and ensure that all links are accurate. This should be a fully functional `README.md` for your GitHub repository.
