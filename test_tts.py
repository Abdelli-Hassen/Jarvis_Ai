from tts_coqui import TTSPlayer

tts = TTSPlayer()

while True:
    text = input("Enter text for Jarvis to say (or 'exit'): ")
    if text.lower() == "exit":
        break
    print("Speaking...")
    tts.speak(text)
    print("Done!\n")
