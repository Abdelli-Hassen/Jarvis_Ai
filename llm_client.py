# llm_client.py
from ollama import chat, generate
import json

DEFAULT_MODEL = "llama3"  # change if you pulled a different model

def ask_chat(messages, model=DEFAULT_MODEL, stream=False):
    resp = chat(model=model, messages=messages, stream=stream)

    # streaming (optional)
    if stream:
        out = ""
        for chunk in resp:
            try:
                out += chunk["message"].content
            except:
                out += str(chunk)
        return out

    # non-stream
    try:
        # حاول مباشرة استخراج .content من resp["message"]
        msg = resp.get("message", None)
        if msg:
            # إذا كان Message object
            try:
                return msg.content
            except:
                # إذا كان dict
                return str(msg.get("content", msg))
        # fallback: حاول resp.content مباشرة
        try:
            return resp.content
        except:
            return str(resp)
    except:
        return str(resp)




def ask_simple(prompt, system=None, model=DEFAULT_MODEL):
    messages = []
    if system:
        messages.append({"role":"system","content": system})
    messages.append({"role":"user","content": prompt})
    return ask_chat(messages, model=model)
