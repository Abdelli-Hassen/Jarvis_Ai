# tts_coqui.py
from TTS.api import TTS
import soundfile as sf
import sounddevice as sd
import os

# choose a released model from Coqui list; change to your preferred model
DEFAULT_TTS_MODEL = "tts_models/en/ljspeech/tacotron2-DDC"

class TTSPlayer:
    def __init__(self, model_name=DEFAULT_TTS_MODEL, device=None):
        # model loads to CPU or GPU if available
        self.tts = TTS(model_name)
        self.device = device

    def speak_to_file(self, text, out_path="out.wav"):
        self.tts.tts_to_file(text=text, file_path=out_path)
        return out_path

    def speak(self, text):
        path = self.speak_to_file(text)
        data, sr = sf.read(path, dtype='float32')
        sd.play(data, sr)
        sd.wait()
