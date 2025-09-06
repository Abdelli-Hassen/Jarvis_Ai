#Jarvis – Offline Personal Assistant

Jarvis is an offline, local personal assistant written in Python. It uses:

Vosk for speech-to-text (STT)

Coqui TTS for text-to-speech

LLaMA for natural language processing via Ollama

RAG-based document search for local knowledge

Jarvis can respond to voice commands or keyboard input, and perform safe actions like opening applications, files, or URLs.

Features

Wakeword detection (Jarvis) for voice commands

Text-to-speech using Coqui TTS

Speech-to-text using Vosk

LLaMA local model integration via Ollama

Retrieval-Augmented Generation (RAG) for local document knowledge

Safe command execution: open apps, files, or URLs

Python Version

Python 3.10

Ensure pip is updated:

python -m pip install --upgrade pip

Quick Start (Windows)
1. Clone the repository
git clone https://github.com/yourusername/jarvis.git
cd jarvis

2. Create virtual environment
python -m venv venv
venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Download Vosk Model

The setup script will do this automatically. Or manually:

Download vosk-model-en-us-0.42-gigaspeech.zip

Extract to models/ folder:

models/vosk-model-en-us-0.42-gigaspeech

5. Install Ollama & LLaMA3 model

Install Ollama

Pull the llama3 model:

ollama pull llama3

6. Run Jarvis
python jarvis_main.py


Voice mode if a microphone is detected (wakeword: Jarvis)

Keyboard mode if no microphone is detected

Project Structure
Jarvis/
│
├─ jarvis_main.py        # Main program
├─ tts_coqui.py          # Text-to-speech wrapper
├─ rag_store.py          # RAG / document search
├─ dispatcher.py         # Safe command execution
├─ llm_client.py         # Ollama LLaMA client
├─ stt_vosk.py           # Vosk STT wrapper
├─ requirements.txt      # Python dependencies
├─ setup.bat             # Windows setup script
├─ .gitignore            # Ignored files/folders
└─ models/               # Models downloaded at runtime (Vosk etc.)

.gitignore

Make sure you have a .gitignore file to ignore:

# Python virtual environment
venv/
Include/
Lib/
Scripts/
Share/

# Python cache
__pycache__/
*.pyc
*.pyo
*.pyd

# Models (large files, downloaded at runtime)
models/

# Temporary audio files
*.wav
*.mp3

# Logs (optional if you add logging later)
logs/

# IDE/project settings (optional)
.vscode/
.idea/

Dependencies

See requirements.txt:

vosk>=0.3.50
TTS>=0.14.0
sounddevice>=0.4.7
soundfile>=0.12.1
ollama>=0.1.5
sentence-transformers>=2.2.2
faiss-cpu>=1.7.4
scikit-learn>=1.2.2
numpy>=1.24.0


System dependencies:

VC++ Build Tools for vosk

ffmpeg in PATH for TTS audio playback

Usage

Wakeword mode:

Jarvis listens for the word “Jarvis”

Responds with TTS

Keyboard mode:

Type commands directly if no microphone is available

Commands can include:

Informational queries (answered using local documents)

Safe actions: open apps, files, or URLs

Setup Script

Windows: setup.bat

This script will:

Create a virtual environment

Install Python dependencies

Download and extract the Vosk model

Remind you to download the Ollama LLaMA3 model if missing

Notes

Models are downloaded at runtime, do not upload them to GitHub.

RAG system allows Jarvis to answer local document queries.

Always activate your virtual environment before running Jarvis.

Temporary audio files are generated in the project root.
