@echo off
echo === Jarvis Setup ===

:: 1. Create virtual environment
python -m venv venv
call venv\Scripts\activate

:: 2. Upgrade pip
python -m pip install --upgrade pip

:: 3. Install requirements
pip install -r requirements.txt

:: 4. Create models folder
if not exist models mkdir models
cd models

:: 5. Download Vosk model
if not exist "vosk-model-en-us-0.42-gigaspeech" (
    echo Downloading Vosk model...
    powershell -Command "Invoke-WebRequest -Uri https://alphacephei.com/vosk/models/vosk-model-en-us-0.42-gigaspeech.zip -OutFile vosk-model-en-us-0.42-gigaspeech.zip"
    powershell -Command "Expand-Archive -Path vosk-model-en-us-0.42-gigaspeech.zip -DestinationPath ."
    del vosk-model-en-us-0.42-gigaspeech.zip
)
cd ..

:: 6. Check Ollama model
ollama list | findstr /i "llama3" >nul
if errorlevel 1 (
    echo ⚠️ Ollama llama3 model not found. Please install via Ollama app or CLI:
    echo     ollama pull llama3
)

echo ✅ Setup complete. Activate venv with: venv\Scripts\activate
echo Run Jarvis with: python jarvis_main.py
pause
