# dispatcher.py
import os, subprocess, platform, shlex
import webbrowser
from pathlib import Path

# allowed actions example
ALLOWED_APPS = {
    "chrome": {"win":"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", "linux":"google-chrome", "mac":"/Applications/Google Chrome.app"},
    # add your own
}

def open_file(path):
    p = Path(path)
    if not p.exists():
        return False, f"File not found: {path}"
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", str(path)])
    else:
        subprocess.Popen(["xdg-open", str(path)])
    return True, f"Opened {path}"

def open_app(app_key):
    sys = platform.system().lower()
    info = ALLOWED_APPS.get(app_key)
    if not info:
        return False, f"App {app_key} not allowed"
    path_or_cmd = info.get("win") if sys.startswith("win") else info.get("linux") if sys.startswith("linux") else info.get("mac")
    if not path_or_cmd:
        return False, "No command configured for your OS"
    try:
        if platform.system() == "Windows" and Path(path_or_cmd).exists():
            os.startfile(path_or_cmd)
        else:
            subprocess.Popen(shlex.split(path_or_cmd))
        return True, f"Launched {app_key}"
    except Exception as e:
        return False, f"Error launching {app_key}: {e}"

def play_audio_file(path):
    return open_file(path)

def safe_run(action_json):
    """
    action_json example:
    {"action":"say", "text":"hello"}
    {"action":"open_app", "app":"chrome"}
    {"action":"open_file", "path":"/home/hassen/file.pdf"}
    """
    a = action_json.get("action")
    if a == "say":
        return True, action_json.get("text","")
    if a == "open_app":
        return open_app(action_json.get("app"))
    if a == "open_file":
        return open_file(action_json.get("path"))
    if a == "open_url":
        url = action_json.get("url")
        if url:
            webbrowser.open(url)
            return True, f"Opened {url}"
        return False, "No url provided"
    return False, f"Unknown or disallowed action: {a}"
