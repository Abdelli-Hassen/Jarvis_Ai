# llm_client.py
from ollama import chat, generate
import json

DEFAULT_MODEL = "llama3"  # change if you pulled a different model

def ask_chat(messages, model=DEFAULT_MODEL, stream=False):
    """
    messages: list of {'role': 'system'|'user'|'assistant', 'content': '...'}
    returns the assistant's text response (string)
    """
    resp = chat(model=model, messages=messages, stream=stream)
    # resp is either final dict or a stream generator when stream=True
    if stream:
        # assemble streaming chunks
        out = ""
        for chunk in resp:
            # chunk has structure {'message': {'role': 'assistant', 'content': '...'}}
            out += chunk.get("message", {}).get("content", "")
        return out
    else:
        # non-stream: response is dict-like
        if isinstance(resp, dict):
            # new sdk returns response['message']['content']
            return resp.get("message", {}).get("content") or resp.get("response")
        # fallback
        return str(resp)

def ask_simple(prompt, system=None, model=DEFAULT_MODEL):
    messages = []
    if system:
        messages.append({"role":"system","content": system})
    messages.append({"role":"user","content": prompt})
    return ask_chat(messages, model=model)
