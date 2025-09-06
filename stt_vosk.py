# stt_vosk.py
import queue, json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import os, time

SAMPLE_RATE = 16000
BLOCK_SIZE = 8000

_q = queue.Queue()

def audio_callback(indata, frames, time_, status):
    _q.put(bytes(indata))

class VoskSTT:
    def __init__(self, model_path="models/vosk-model-small-en-us-0.15"):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"VOSK model not found at {model_path}. Download it and set path.")
        self.model = Model(model_path)
        self.rec = KaldiRecognizer(self.model, SAMPLE_RATE)

    def listen_once(self, timeout=5):
        """Listen for a short utterance and return recognized text (blocking)."""
        out = ""
        with sd.RawInputStream(samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE, dtype='int16', channels=1, callback=audio_callback):
            start = time.time()
            while True:
                try:
                    data = _q.get(timeout=timeout)
                except Exception:
                    break
                if self.rec.AcceptWaveform(data):
                    res = json.loads(self.rec.Result())
                    text = res.get("text", "")
                    out += " " + text
                    # break after full result
                    break
                else:
                    # partial, continue (do not accumulate partials as final, but can if needed)
                    pass
                if time.time() - start > timeout:
                    break
        return out.strip()

    def has_wakeword_in(self, text, wakeword="jarvis"):
        return wakeword.lower() in text.lower()
