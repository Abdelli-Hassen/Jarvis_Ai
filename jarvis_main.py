# jarvis_main.py
import time, json, re
from llm_client import ask_chat
from stt_vosk import VoskSTT
from tts_coqui import TTSPlayer
from dispatcher import safe_run
from rag_store import RAGStore
import sounddevice as sd
import time

WAKEWORD = "jarvis"
MODEL_NAME = "llama3"

# initialize modules (paths: adjust to your downloads)
stt = VoskSTT(r"models\vosk-model-en-us-0.42-gigaspeech")
tts = TTSPlayer()   # will load model on first use
# RAG: optional — build with your docs once and pass to prompt
# Example small doc set for demo:
docs = [
    "Hassen likes programming and uses Python and Arduino.",
    "Jarvis is offline and runs locally using Ollama and VOSK.",
]
rag = RAGStore()
rag.build(docs)

SYSTEM_PROMPT = """
You are Jarvis, an offline personal assistant running locally. When given a user command, you MUST output ONLY valid JSON (no extra commentary).
JSON structure must be:
{
  "action": "<one of: say, open_app, open_file, open_url, search_docs, none>",
  "text": "<text to say to user, optional>",
  "params": { ... optional parameters ... }
}
If the user asked an informational question that should be answered using local documents, set action to "none" and place the answer in "text".
If you need to run a permitted action, use action fields above. Keep JSON minimal.
"""

def extract_json_from_text(text):
    # try to find first {...} block
    m = re.search(r"(\{[\s\S]*\})", text)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except Exception:
        # try to fix common mistakes: replace single quotes
        s = m.group(1).replace("'", '"')
        try:
            return json.loads(s)
        except Exception:
            return None

def ask_jarvis_and_act(user_text):
    # Ask LLM to produce JSON action
    msg_user = f"User: {user_text}\nPlease reply ONLY with the JSON described."
    resp = ask_chat(
        [{"role": "system", "content": SYSTEM_PROMPT},
         {"role": "user", "content": msg_user}],
        model=MODEL_NAME
    )
#     print("LLM raw:", resp)
    action_json = extract_json_from_text(resp)

    if not action_json:
        # fallback: just speak the LLM plain answer
        fallback_resp = ask_chat(
            [{"role": "system", "content": "You are Jarvis. Answer concisely."},
             {"role": "user", "content": user_text}],
            model=MODEL_NAME
        )
        return True, fallback_resp

    # Case 1: action = search_docs
    if action_json.get("action") == "search_docs":
        q = action_json.get("params", {}).get("query", user_text)
        contexts = rag.retrieve(q, top_k=3)
        context_prompt = (
            "Context documents:\n" + "\n---\n".join(contexts) +
            f"\nAnswer the question: {q}"
        )
        ans = ask_chat(
            [{"role": "system", "content": "You are Jarvis, answer using the provided contexts. If unknown, say you don't know."},
             {"role": "user", "content": context_prompt}],
            model=MODEL_NAME
        )
        return True, ans

    # Case 2: action = none → just return the text
    if action_json.get("action") == "none":
        return True, action_json.get("text", "")

    # Case 3: dispatch to safe_run
    ok, result = safe_run(action_json)
    if ok:
        if isinstance(result, tuple):
            return result  # (ok, message)
        else:
            return True, result if result else action_json.get("text", "Done.")
    else:
        return False, str(result)

        

'''
def ask_jarvis_and_act(user_text):
    # Ask LLM to produce JSON action
    msg_user = f"User: {user_text}\nPlease reply ONLY with the JSON described."
    resp = ask_chat([{"role":"system","content":SYSTEM_PROMPT},
                     {"role":"user","content": msg_user}], model=MODEL_NAME)
    print("LLM raw:", resp)
    action_json = extract_json_from_text(resp)
    if not action_json:
        # fallback: just speak the LLM plain answer
        fallback_resp = ask_chat([{"role":"system","content":"You are Jarvis. Answer concisely."},
                                  {"role":"user","content": user_text}], model=MODEL_NAME)
        return True, fallback_resp
    # If action is search_docs: perform RAG retrieval and ask LLM for answer using contexts
    if action_json.get("action") == "search_docs":
        q = action_json.get("params", {}).get("query", user_text)
        contexts = rag.retrieve(q, top_k=3)
        context_prompt = "Context documents:\n" + "\n---\n".join(contexts) + f"\nAnswer the question: {q}"
        ans = ask_chat([{"role":"system","content":"You are Jarvis, answer using the provided contexts. If unknown, say you don't know."},
                       {"role":"user","content": context_prompt}], model=MODEL_NAME)
        return True, ans
    # otherwise dispatch safe action
    ok, result = safe_run(action_json)
    if ok:
        # If safe_run returned a message result for say/open, gather a reply text
        if isinstance(result, tuple):
            # some functions return (ok, message)
            return result
        else:
            # result is string message
            return True, result if result else action_json.get("text","Done.")
    else:
        return False, str(result)
'''


def has_microphone():
    try:
        devices = sd.query_devices()
        for idx, d in enumerate(devices):
            if d["max_input_channels"] > 0:
                try:
                    # Try actually opening the stream
                    with sd.InputStream(device=idx, channels=1):
                        return True
                except Exception:
                    continue
        return False
    except Exception as e:
        print("Error checking devices:", e)
        return False



def main_loop():
    use_mic = has_microphone()  # detect mic availability at start
    print("Jarvis: Mic mode" if use_mic else "Jarvis: Keyboard mode")
    if use_mic:
        print("Jarvis: Listening for wakeword ('%s') ..." % WAKEWORD)

    while True:
        try:
            if use_mic:
                # Listen briefly for wakeword
                txt = stt.listen_once(timeout=5)
                if not txt:
                    continue
                print("Heard:", txt)

                # Only proceed if wakeword detected
                if not stt.has_wakeword_in(txt, WAKEWORD):
                    continue

                # Wakeword detected: prompt and listen for full command
                tts.speak("Yes?")
                cmd = stt.listen_once(timeout=10)
                print("Command:", cmd)

            else:
                # Keyboard mode: the user's input IS the command (single-step)
                cmd = input("You (keyboard command): ").strip()
                if not cmd:
                    continue

            # If we have a command, ask the LLM and act
            ok, reply = ask_jarvis_and_act(cmd)

            if ok:
                if use_mic:
                    tts.speak(reply)
                else:
                    print("Jarvis:", reply)
            else:
                if use_mic:
                    tts.speak("Sorry, I couldn't do that.")
                else:
                    print("Sorry, I couldn't do that.")

        except KeyboardInterrupt:
            print("Exiting")
            break

        except Exception as e:
            # Improve mic-related error handling: wait and retry, then fallback to keyboard
            err_str = str(e).lower()
            if use_mic and ("portaudioerror" in err_str or "device" in err_str or "no default input" in err_str):
                print("⚠️ Microphone error. Waiting 5 seconds to allow you to plug in a mic...")
                time.sleep(5)
                if has_microphone():
                    print("✅ Mic detected. Resuming mic mode.")
                    use_mic = True
                    print("Jarvis: Listening for wakeword ('%s') ..." % WAKEWORD)
                else:
                    print("❌ Still no mic. Switching to keyboard mode.")
                    use_mic = False
            else:
                print("Error:", e)
                time.sleep(1)




''' def main_loop():
    print("Jarvis: Listening for wakeword ('%s') ..." % WAKEWORD)
    use_mic = True  # start with mic mode

    while True:
        try:
            if use_mic:
                txt = stt.listen_once(timeout=5)
            else:
                txt = input("You (keyboard): ")

            if not txt:
                continue

            print("Heard:", txt)

            if stt.has_wakeword_in(txt, WAKEWORD) or not use_mic:
                if use_mic:
                    # prompt user with TTS
                    tts.speak("Yes?")
                    # listen longer for the real command
                    cmd = stt.listen_once(timeout=10)
                else:
                    cmd = input("Command (keyboard): ")

                print("Command:", cmd)

                if not cmd:
                    tts.speak("I didn't catch that.") if use_mic else print("I didn't catch that.")
                    continue

                ok, reply = ask_jarvis_and_act(cmd)

                if not ok:
                    tts.speak("Sorry, I couldn't do that.") if use_mic else print("Sorry, I couldn't do that.")
                else:
                    tts.speak(reply) if use_mic else print("Jarvis:", reply)

        except KeyboardInterrupt:
            print("Exiting")
            break

        except Exception as e:
            if "PortAudioError" in str(e) or "device" in str(e).lower():
                print("⚠️ No microphone detected. Waiting 5 seconds... Plug in your mic now!")
                time.sleep(5)
                try:
                    # retry once
                    _ = stt.listen_once(timeout=3)
                except:
                    print("❌ Still no mic. Switching to keyboard mode.")
                    use_mic = False
                    continue
            else:
                print("Error:", e)
                time.sleep(1)
 '''

'''
def main_loop():
    print("Jarvis: Listening for wakeword ('%s') ..." % WAKEWORD)
    while True:
        try:
            txt = stt.listen_once(timeout=5)
            if not txt:
                continue
            print("Heard:", txt)
            if stt.has_wakeword_in(txt, WAKEWORD):
                # prompt user (TTS)
                tts.speak("Yes?")
                # listen longer for the real command
                cmd = stt.listen_once(timeout=10)
                print("Command:", cmd)
                if not cmd:
                    tts.speak("I didn't catch that.")
                    continue
                ok, reply = ask_jarvis_and_act(cmd)
                if not ok:
                    tts.speak("Sorry, I couldn't do that.")
                else:
                    tts.speak(reply)
        except KeyboardInterrupt:
            print("Exiting")
            break
        except Exception as e:
            print("Error:", e)
            time.sleep(1)
'''
if __name__ == "__main__":
    main_loop()
