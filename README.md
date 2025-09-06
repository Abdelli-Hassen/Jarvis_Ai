Jarvis – Offline Personal Assistant

Jarvis is an offline, local personal assistant written in Python. It uses Vosk for speech-to-text, Coqui TTS for text-to-speech, LLaMA for natural language processing, and a RAG-based document search system.

Jarvis can respond to voice commands or keyboard input and can perform safe actions like opening applications, files, or URLs.

Features

Wakeword detection (Jarvis) for voice commands

Text-to-speech using Coqui TTS

Speech-to-text using Vosk

LLaMA local model integration via Ollama

Retrieval-Augmented Generation (RAG) for local document knowledge

Safe command execution: open apps, files, or URLs

Python Version

Python 3.10 (tested)

Make sure pip is updated:

python -m pip install --upgrade pip

Installation & Setup
1. Clone the repository
git clone https://github.com/yourusername/jarvis.git
cd jarvis

2. Create a virtual environment
python -m venv venv


Windows:

venv\Scripts\activate



3. Install dependencies
pip install -r requirements.txt

4. Download Vosk Model

The setup scripts will do this automatically. Or manually:

Download from Vosk Models
 → vosk-model-en-us-0.42-gigaspeech.zip

Extract to models/ folder:

models/vosk-model-en-us-0.42-gigaspeech

5. Ollama LLaMA3 Model

Install Ollama: https://ollama.com/docs

Make sure llama3 model is downloaded:

ollama pull llama3

6. Run Jarvis
python jarvis_main.py


Voice mode (if microphone detected) or keyboard mode if no mic.

Wakeword: Jarvis


Make sure you have a .gitignore that ignores:

venv/, Include/, Lib/, Scripts/, Share/

models/

Temporary audio files *.wav, logs, __pycache__/

Usage

Wakeword mode (microphone detected):

Jarvis listens for "Jarvis"

Responds using TTS

Keyboard mode:

Type commands directly if no microphone is available

Commands can include:

Informational queries (answered using local docs)

Safe actions: open apps, files, or URLs

Dependencies

See requirements.txt for full list:


Optional system dependencies:

Windows: VC++ Build Tools for vosk, add ffmpeg to PATH


Notes

Models are downloaded at runtime, do not upload them to GitHub.

The RAG system is optional but allows Jarvis to answer local document queries.

Always activate your virtual environment before running Jarvis.

Temporary audio files are generated in the project root.

Setup Script

Windows: setup.bat

This will:

Create venv

Install Python dependencies

Download and extract Vosk model

Remind you to download Ollama LLaMA3 model if missing
