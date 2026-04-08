# Seno — Your Fully Offline Personal AI Agent

> **Everything runs locally. No cloud. No subscriptions. No data leaving your machine.**
>
> Seno is a fully autonomous offline AI assistant built from scratch over 6 development sessions. It combines a local LLM (Qwen 2.5 7B via llama.cpp), real-time voice input (Faster-Whisper), neural text-to-speech (Silero), a multi-file document memory system (FAISS RAG), and a fully modular plugin architecture — all running on your own GPU.

---

## Table of Contents

1. [What Is Seno?](#1-what-is-seno)
2. [System Requirements](#2-system-requirements)
3. [Installation & Setup](#3-installation--setup)
4. [How to Launch Seno](#4-how-to-launch-seno)
5. [How to Talk to Seno](#5-how-to-talk-to-seno)
6. [Complete Feature Reference](#6-complete-feature-reference)
   - [6.1 Voice Input (STT)](#61-voice-input-stt)
   - [6.2 Voice Output (TTS)](#62-voice-output-tts)
   - [6.3 Offline LLM Brain](#63-offline-llm-brain)
   - [6.4 Hybrid Brain — Smart Routing](#64-hybrid-brain--smart-routing)
   - [6.5 App Control](#65-app-control)
   - [6.6 Volume & Audio Control](#66-volume--audio-control)
   - [6.7 Web & Information](#67-web--information)
   - [6.8 File & Document System](#68-file--document-system)
   - [6.9 Reminders & Timers](#69-reminders--timers)
   - [6.10 Focus Mode](#610-focus-mode)
   - [6.11 Python Sandbox](#611-python-sandbox)
   - [6.12 Autonomous Agent Engine](#612-autonomous-agent-engine)
   - [6.13 System Awareness & Telemetry](#613-system-awareness--telemetry)
   - [6.14 Screen Vision (OCR)](#614-screen-vision-ocr)
   - [6.15 Clipboard & Active File Injection](#615-clipboard--active-file-injection)
   - [6.16 Conversation Modes](#616-conversation-modes)
   - [6.17 RAG Document Memory](#617-rag-document-memory)
   - [6.18 Chat History & Persistent Memory](#618-chat-history--persistent-memory)
   - [6.19 Task Memory (Overarching Missions)](#619-task-memory-overarching-missions)
   - [6.20 Workspace Snapshots (Setups)](#620-workspace-snapshots-setups)
   - [6.21 Parallel Thinking Engine](#621-parallel-thinking-engine)
   - [6.22 Execution Memory (Muscle Memory)](#622-execution-memory-muscle-memory)
   - [6.23 Error Intelligence Database](#623-error-intelligence-database)
   - [6.24 System-Level Workflow Engine](#624-system-level-workflow-engine)
   - [6.25 Learning Engine (Self-Improving)](#625-learning-engine-self-improving)
   - [6.26 Security Daemon (Background Monitor)](#626-security-daemon-background-monitor)
   - [6.27 Plugin System](#627-plugin-system)
   - [6.28 Time Awareness & Schedule Context](#628-time-awareness--schedule-context)
   - [6.29 Urgency Detection](#629-urgency-detection)
   - [6.30 Computer Lock](#630-computer-lock)
7. [Configuration Reference (seno_config.json)](#7-configuration-reference-seno_configjson)
8. [File Structure Reference](#8-file-structure-reference)
9. [Data Files Created at Runtime](#9-data-files-created-at-runtime)
10. [Adding Custom Plugins](#10-adding-custom-plugins)
11. [Known Limitations & Notes](#11-known-limitations--notes)

---

## 1. What Is Seno?

Seno is a personal AI agent you run entirely on your own computer. There is no internet dependency for the AI brain — the language model runs locally on your GPU using `llama.cpp`. Every component (speech recognition, speech synthesis, document memory, screen reading) is local.

Seno is **not a simple chatbot**. It can:

- Launch and close applications on your computer
- Browse the web silently in the background without opening a browser window
- Set alarms and reminders that persist even after you shut down your PC
- Take full autonomous control to build software, write code, run tests, and fix its own errors
- Read whatever text is on your screen at this moment
- Store named automation workflows and replay them on command
- Learn from its own errors and recall fixes instantly next time
- Route every request to the right inference profile automatically for maximum speed

---

## 2. System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10/11 | Windows 11 |
| CPU | Intel i5 / Ryzen 5 | Intel i7 / Ryzen 7 |
| RAM | 12 GB | 16+ GB |
| GPU | NVIDIA 6 GB VRAM (CUDA) | NVIDIA 8 GB VRAM (RTX series) |
| Python | 3.10+ | 3.12 |
| Storage | 15 GB free | 20+ GB free |
| Microphone | Any USB or built-in mic | Any quality USB mic |

> **CUDA is required for full performance.** Seno will fall back to CPU if no GPU is found, but response time will increase to 20–30 seconds per message. With GPU offload enabled, responses arrive in 2–4 seconds.

**Key software dependencies (installed automatically):**
- `llama-cpp-python` (CUDA build) — the LLM runtime
- `faster-whisper` — offline speech-to-text
- `silero` (via torch) — neural text-to-speech
- `sentence-transformers` + `faiss-cpu` — document memory (RAG)
- `easyocr` + `mss` — screen reading / OCR
- `psutil` — process and system monitoring
- `sounddevice`, `soundfile` — audio I/O

---

## 3. Installation & Setup

### Step 1 — Clone or Download the Project

Place the `Jarvis_Ai` folder anywhere on your machine (e.g. `C:\Users\you\Desktop\Jarvis_Ai`).

### Step 2 — Run the Setup Script

Double-click `setup.bat` or run in a terminal:

```
setup.bat
```

This will:
1. Create a Python virtual environment at `venv\`
2. Install all Python dependencies from `requirements.txt`
3. Create the `models\` directory

### Step 3 — Download the LLM Model

Seno uses **Qwen 2.5 7B Instruct** in Q5_K_M quantization (split across 2 files). Download both files and place them in the `models\` folder:

```
models\qwen2.5-7b-instruct-q5_k_m-00001-of-00002.gguf
models\qwen2.5-7b-instruct-q5_k_m-00002-of-00002.gguf
```

> You only pass the first file path to llama.cpp — it discovers the second automatically.

### Step 4 — Install the CUDA-Enabled llama-cpp-python

The standard `pip install llama-cpp-python` installs **without CUDA** and runs on CPU only. You must install the CUDA pre-built wheel:

```
pip install https://github.com/abetlen/llama-cpp-python/releases/download/v0.3.4-cu124/llama_cpp_python-0.3.4-cp312-cp312-win_amd64.whl
```

Replace `cp312` with your Python version if needed (e.g. `cp310` for Python 3.10).

### Step 5 — (Optional) Install Vision Dependencies

To enable the screen-reading feature:

```
pip install easyocr opencv-python-headless Pillow mss numpy
```

### Step 6 — Verify

Start Seno (see next section). On first boot, you should see in the console:

```
ggml_cuda_init: found 1 CUDA devices:
  Device 0: NVIDIA GeForce RTX 4060 Laptop GPU, compute capability 8.9
[LLM] Full GPU offload enabled (7.9 GB VRAM on NVIDIA GeForce RTX 4060 Laptop GPU)
[Seno] Reminder engine ready.
[Seno] Background security agents initialized.
```

---

## 4. How to Launch Seno

There are **two ways** to run Seno:

### Option A — Graphical HUD (Recommended)

Double-click **`Seno.bat`**

This launches `seno_ui.py` — the full graphical interface with an animated Iron Man-inspired HUD, the audio visualizer, system telemetry display, and all controls.

### Option B — Terminal / Command Line

Double-click **`SenoCmd.bat`**

This launches `seno_main.py` directly in a terminal. On startup you will be asked:

```
Would you like to (s)peak or (w)rite? [s/w]:
```

- Press `s` for microphone (voice) mode
- Press `w` for keyboard (text) mode

Press `Ctrl+C` to exit. Before exiting, Seno automatically saves a summary of the session to its long-term document memory.

---

## 5. How to Talk to Seno

### Wake Word

In microphone mode, Seno is always listening but only responds when it hears its wake word. The default wake word is:

> **"Seno"**

Seno also recognizes several phonetic aliases in case the microphone mishears you:

`seno`, `nervous`, `travis`, `service`, `darvis`, `drivers`, `garbage`, `charvis`, `ceno`, `cinno`, `come on man`, `wake up`

### How a Conversation Turn Works

1. You say **"Seno"** (or any alias)
2. Seno says **"Yes?"** and starts listening for your command
3. You speak your command
4. Seno transcribes it with Faster-Whisper (offline, GPU-accelerated)
5. The transcript is sent through an LLM correction step to fix phonetic errors
6. The corrected command is routed to the Hybrid Brain classifier
7. The LLM generates a JSON action response
8. The action is dispatched (open app, search web, set reminder, etc.)
9. Seno speaks the result through Silero TTS

### Keyboard Mode

In keyboard mode, simply type your command at the `You (keyboard command):` prompt. No wake word is needed.

### Multi-Command Requests

You can combine multiple commands in a single request:

> "Seno, close Spotify and mute the volume"

> "Seno, open Chrome and search for the latest Python news"

---

## 6. Complete Feature Reference

---

### 6.1 Voice Input (STT)

**Technology:** Faster-Whisper (`base.en` model), GPU-accelerated on CUDA.

**How it works:**
- Seno listens continuously using your microphone via `sounddevice`
- When the wake word is detected, a second `listen_once()` call captures your command
- The audio is passed to Faster-Whisper for offline transcription
- The raw transcript is then sent to the LLM for phonetic correction (e.g. "reminds me" → "remind me", "muts the volume" → "mute the volume")

**Files:** `stt_whisper.py`

**Notes:**
- Entirely offline — no audio is ever sent to the internet
- If the microphone disconnects mid-session, Seno waits 5 seconds and switches to keyboard mode automatically
- You can start in keyboard mode from the beginning by choosing `w` at startup

---

### 6.2 Voice Output (TTS)

**Technology:** Silero neural TTS (TorchScript model), always runs on CPU on Windows for stability.

**How it works:**
- Seno maintains a background TTS worker thread and a Python `queue.Queue`
- When Seno has something to say, the text is pushed onto the queue immediately
- The worker thread pulls from the queue and calls `tts.speak()` sequentially
- This means Seno starts speaking the first sentence while the LLM is still generating the rest — zero waiting

**Files:** `tts_silero.py`

**Voice setting:** Configured in `seno_config.json` under `voice_settings.speaker` (default: `en_1`).

**Silent Mode:** You can tell Seno to completely disable TTS output — see [Conversation Modes](#616-conversation-modes).

---

### 6.3 Offline LLM Brain

**Model:** Qwen 2.5 7B Instruct (Q5_K_M quantization, ~5.2 GB on disk)

**Runtime:** llama-cpp-python with CUDA 12.4 acceleration

**GPU allocation strategy (auto-detected at startup):**

| VRAM Available | Strategy |
|---|---|
| ≥ 7.5 GB | Full offload — all 32 transformer layers on GPU. Response: 2–4s |
| ≥ 6.0 GB | Partial offload — 24 layers on GPU. Response: ~8s |
| < 6.0 GB | Conservative — 18 layers on GPU. Response: ~15s |
| No CUDA | CPU only. Response: 20–30s |

**Speed tweaks applied:**
- `flash_attn=True` — fuses QKV matrix operations into a single CUDA kernel (~15–30% faster)
- `use_mmap=True` — memory-mapped model load (faster startup, lower RAM footprint)
- `n_ctx=3072` — context window sized to fit system prompt (~2200 tokens) with safe headroom
- `repeat_penalty=1.1`, `top_p=0.95`, `top_k=40` — quality sampling parameters

**Thread safety:** All GPU inference calls are serialized through a single `threading.Lock()` (`_llm_lock`). This prevents CUDA memory pool corruption when multiple background features (think_deep, background agents) attempt simultaneous inference.

**Files:** `llm_client.py`

---

### 6.4 Hybrid Brain — Smart Routing

Every single user request is automatically classified by a lightweight heuristic engine before hitting the LLM. There is **no extra GPU call** — this is pure Python regex and string analysis.

**Three inference profiles:**

| Profile | Temp | Max Tokens | Used For |
|---|---|---|---|
| **FAST** | 0.15 | 180 | Device commands, greetings, math, reminders, volume |
| **NORMAL** | 0.65 | 512 | General conversation, coding help, web search |
| **DEEP** | 0.75 | 1024 | Architecture, writing, analysis, long explanations |

**Examples of automatic routing:**
- `"Open chrome"` → **FAST** (device command keyword)
- `"Mute the volume"` → **FAST**
- `"What time is it?"` → **FAST**
- `"Hey Seno!"` → **FAST** (greeting pattern)
- `"Help me debug my Flask app"` → **NORMAL**
- `"Design a scalable database schema for a multi-tenant SaaS platform"` → **DEEP**
- `"Write a detailed comparative analysis of REST vs GraphQL"` → **DEEP**

**Urgency override:** If the user says anything urgent (see [Urgency Detection](#629-urgency-detection)), the router is overridden and FAST profile is forced regardless.

**Console output:** Every request prints `[HybridBrain/LABEL] temp=X, max_tokens=Y` so you can verify routing.

**Files:** `task_router.py`

---

### 6.5 App Control

**Open an application:**
> "Seno, open Chrome"
> "Seno, launch VSCode"
> "Seno, open the calculator"

**Close an application:**
> "Seno, close Spotify"
> "Seno, kill Discord"
> "Seno, close Chrome"

Seno uses `psutil` to scan all running processes dynamically. It matches by raw process name (`msedge.exe`), friendly name (`Microsoft Edge`), or partial match. No hardcoded process list needed.

**Pre-configured applications (ready to use out of the box):**

| Name | Windows | Linux | Mac |
|---|---|---|---|
| chrome | chrome.exe | google-chrome | open -a Google Chrome |
| edge | msedge.exe | microsoft-edge | open -a Microsoft Edge |
| notepad | notepad.exe | gedit | open -a TextEdit |
| calculator | calc.exe | gnome-calculator | open -a Calculator |
| explorer | explorer.exe | xdg-open . | open . |
| cmd | cmd.exe | gnome-terminal | open -a Terminal |
| powershell | powershell.exe | pwsh | pwsh |
| paint | mspaint.exe | pinta | open -a Preview |
| wordpad | write.exe | libreoffice --writer | open -a TextEdit |
| snipping_tool | SnippingTool.exe | gnome-screenshot | screencapture -i |
| control_panel | control.exe | gnome-control-center | open -a System Settings |
| task_manager | taskmgr.exe | gnome-system-monitor | open -a Activity Monitor |
| windows_store | ms-windows-store://home | gnome-software | open -a App Store |
| camera | microsoft.windows.camera: | cheese | open -a Photo Booth |

**Learn a new application permanently:**
> "Seno, learn app 'rider' at 'C:\Program Files\JetBrains\Rider\bin\rider64.exe'"

This saves the new app to `seno_config.json` permanently. From that point on, `"open rider"` works forever.

**Fallback auto-discovery:** If an app is not configured, Seno automatically scans the Windows Start Menu Programs folder and common install directories (Program Files, Program Files (x86), AppData\Local) before giving up.

**Files:** `dispatcher.py` — `open_app()`, `close_app()`, `learn_app()`, `find_app_in_system()`

---

### 6.6 Volume & Audio Control

**Mute:**
> "Seno, mute the volume"
> "Seno, silence everything"

**Unmute:**
> "Seno, unmute"
> "Seno, turn the sound back on"

**Set specific level:**
> "Seno, set the volume to 40 percent"
> "Seno, set volume to 80"

On Windows, volume is controlled using the Windows Core Audio COM API via PowerShell (zero additional dependencies). On Linux via `amixer/pulse`. On macOS via `osascript`.

**Files:** `dispatcher.py` — `set_system_volume()`

---

### 6.7 Web & Information

Seno has two distinct modes for web interaction:

#### Silent Web Scraping (Ghost Browsing) — Default

> "Seno, what's the latest news about AI?"
> "Seno, what is the weather like in London today?"
> "Seno, tell me about the recent drama at OpenAI"

Seno uses **Google News RSS** and **DuckDuckGo** APIs in the background — no browser window opens. The raw HTML/RSS data is passed to the LLM which synthesizes a spoken briefing. This is the default for all factual/news questions.

Three sub-modes:
- **News mode:** Fetches Google News RSS (no API key). Falls back to DuckDuckGo + "news" keyword if RSS returns empty.
- **Search mode:** DuckDuckGo Instant Answer API, then DuckDuckGo Lite HTML fallback.
- **Page mode:** Fetch any arbitrary URL and extract readable text.

#### Visual Web Search (Opens Browser)

> "Seno, open YouTube and search for lo-fi music"
> "Seno, show me the GitHub page for FastAPI"
> "Seno, go to reddit.com"

Only triggered by explicit navigation keywords: **"open", "show me", "display", "go to", "navigate to"**. Launches your default browser.

Supports: Google, YouTube, GitHub, or any direct URL.

**Files:** `web_scraper.py`, `dispatcher.py` — `search_web()`, `seno_plugins/web/scrape_web.py`

---

### 6.8 File & Document System

**Open a file:**
> "Seno, open my resume"
> "Seno, open the file project_plan.pdf"

Seno searches for the file on your Desktop, Downloads, and Documents with up to 4 levels of directory depth. Fuzzy matching normalizes spaces, dashes, and underscores. Opens with the system default application.

**Find a document:**
> "Seno, find the document about the API design"
> "Seno, find my notes from last week"

Uses ripgrep (`rg`) or `fd` for ultra-fast recursive searching. Once found, the document contents are injected into the LLM prompt for a spoken verbal summary.

**Open a URL:**
> "Seno, open https://github.com"

**Files:** `dispatcher.py` — `open_file()`, `find_document()`, `open_url()`, `seno_plugins/system/find_document.py`

---

### 6.9 Reminders & Timers

**Set a reminder:**
> "Seno, remind me in 20 minutes to call mom"
> "Seno, set an alarm for 1 hour and 30 minutes — pasta is done"
> "Seno, remind me in 45 minutes to take my medication"

Seno understands hours, minutes, and seconds in any combination.

**List active reminders:**
> "Seno, what reminders do I have?"
> "Seno, show me my alarms"

**Cancel a reminder:**
> "Seno, cancel reminder 3"
> "Seno, cancel all reminders"

**Persistence — Missed Reminders:**
All reminders are saved to `seno_reminders.json` on disk. If you set a reminder, turn off your PC, and turn it back on — the alarm fires **instantly on the next boot**. Nothing is ever missed.

**How it works:** A dedicated daemon thread (`reminder_engine.py`) ticks at 1 second intervals, checking the pending alarm queue. When an alarm fires, it calls `speak_async()` to interrupt whatever Seno is doing and say your reminder out loud.

**Files:** `reminder_engine.py`, `dispatcher.py`, `seno_plugins/custom/reminders_set.py`, `reminders_list.py`, `reminders_cancel.py`

---

### 6.10 Focus Mode

**Activate focus mode:**
> "Seno, start focus mode"
> "Seno, focus mode for 90 minutes"
> "Seno, enable focus mode and close Discord and Spotify"

When focus mode activates:
1. System volume is immediately muted
2. A configurable list of distracting apps is closed (default: Discord, Spotify, Steam, Chrome, Edge, Firefox)
3. If a duration was given, a timer is set for auto-exit

**End focus mode:**
> "Seno, end focus mode"
> "Seno, focus mode off"

When focus mode ends:
1. Volume is unmuted
2. Seno asks: *"I previously closed Discord, Spotify, Steam. Would you like me to re-open them?"*
3. Say **"yes"** and they all relaunch automatically

**Timed auto-end:** If you said "focus mode for 90 minutes", after 90 minutes the reminder engine fires `__FOCUS_END__` automatically — Seno announces the end and restores your audio without any manual intervention.

**Configuring distraction apps:** Edit `"focus_mode_close"` in `seno_config.json`:
```json
"focus_mode_close": ["discord", "spotify", "steam", "chrome", "edge", "firefox"]
```

**Files:** `dispatcher.py` — `focus_mode()`, `focus_end()`

---

### 6.11 Python Sandbox

> "Seno, what is 1,234 times 5,678?"
> "Seno, calculate the compound interest on $10,000 at 7% for 5 years"
> "Seno, how many days until Christmas?"
> "Seno, write a Python script to generate a list of prime numbers under 100"

Seno writes and executes raw Python code in a sandboxed subprocess. The `stdout` output is captured and fed back to the LLM to synthesize a verbal answer. This allows Seno to compute complex math, parse data, or figure out anything that Python can calculate.

**Files:** `seno_plugins/coding/run_python.py`

---

### 6.12 Autonomous Agent Engine

The most powerful feature. Seno can switch into a fully autonomous **ReAct Loop** to handle multi-step goals without you needing to guide it.

**Trigger:**
> "Seno, build me a simple Flask REST API"
> "Seno, research how RAG works and write me a summary document"
> "Seno, create a Python script that reads a CSV and generates a bar chart"

**What happens:**
1. Seno enters `AutonomousAgent.run_task()` — a dedicated loop separate from the main conversation
2. The LLM generates a thought + tool call in JSON format every turn
3. The agent executes the tool and feeds the result back
4. This continues until the LLM calls `finish_task`

**Agent tools available inside the loop:**

| Tool | What it does |
|---|---|
| `write_file` | Create or overwrite any file in the workspace |
| `read_file` | Read any file's contents |
| `run_command` | Execute a terminal command in the workspace directory |
| `finish_task` | End the loop and speak a summary to the user |

**Working directory:** `seno_workspace\` inside the project folder. All files created by the agent land here by default.

**Self-correction:** If the LLM produces invalid JSON 10 consecutive times, Seno pauses and asks you out loud: *"I've run into errors 10 times in a row. Should I abort or keep trying?"*

**Execution Memory integration:** Every successful `run_command` call is recorded. When the task completes, the full command chain is saved to `seno_execution_memory.json` mapped to the goal description.

**Error Intelligence integration:** Before running any command, the agent checks the Error Intelligence Database for known fixes matching the command. If a past error is recognized, the fix is injected as context so the LLM can correct itself proactively.

**Files:** `seno_agent.py`

---

### 6.13 System Awareness & Telemetry

> "Seno, what's my system status?"
> "Seno, how much RAM do I have left?"
> "Seno, what's my CPU temperature?"
> "Seno, what apps are open right now?"

Seno reads and speaks:
- CPU temperature and usage percentage
- Available RAM
- Battery percentage (on laptops)
- A complete list of every open application window on the desktop

**Window scanning is cached** with an 8-second TTL. Back-to-back calls cost ~0ms instead of ~200ms for the raw psutil scan.

**Active window injection:** On every conversation turn, Seno automatically injects your currently active window name and title into the system prompt, so it always knows what you're looking at.

**Files:** `system_senses.py`

---

### 6.14 Screen Vision (OCR)

> "Seno, what's on my screen?"
> "Seno, read what you can see"
> "Seno, look at this code"
> "Seno, analyze my screen"

Seno takes a **screenshot of your primary monitor** using `mss` (pure Python, zero external dependencies). The image is processed by `easyocr` running entirely locally (GPU=False by default). The extracted text (up to 2000 characters) is injected into the LLM context for analysis.

**IMPORTANT:** Seno will **never** say "I'm a text-only AI" or "I can't see your screen". The system prompt explicitly forbids this. If you ask Seno to look at your screen, it will always attempt to use `read_screen`.

**Files:** `seno_plugins/system/read_screen.py`

**Dependencies:** `pip install easyocr opencv-python-headless Pillow mss numpy`

---

### 6.15 Clipboard & Active File Injection

These are automatic context injections — no command needed.

**Clipboard:** If your message contains the words `"this"`, `"clipboard"`, `"copy"`, or `"read"`, Seno automatically reads your system clipboard and injects it into the prompt.

Example:
> (Copy some code to clipboard) → "Seno, explain this"
> Seno reads your clipboard and explains the code.

**Active File:** If your message contains `"this"`, `"file"`, `"code"`, `"document"`, or `"look"`, Seno detects your active foreground window, deduces the file path (common for VSCode, Notepad, etc.), and injects the file's raw content into the prompt.

Example:
> (Open a Python file in VSCode) → "Seno, review this code"
> Seno reads the open file and gives you a code review.

**Files:** `system_senses.py` — `get_clipboard_text()`, `get_active_file_content()`

---

### 6.16 Conversation Modes

Seno supports three distinct personality modes that change how verbose and formal it is:

**Switch modes:**
> "Seno, switch to developer mode"
> "Seno, activate silent mode"
> "Seno, go back to assistant mode"

| Mode | Behavior |
|---|---|
| **assistant** (default) | Natural, conversational, explains things, chatty, uses casual language. Full TTS output. |
| **developer** | Hyper-concise. Strips all filler. Returns raw data and code snippets immediately. Still speaks, but briefly. |
| **silent** | Disables the TTS engine entirely. Seno processes commands and outputs results to the console only — no voice output whatsoever. |

The mode is saved to `seno_config.json` so it persists across restarts.

**Files:** `seno_plugins/custom/change_mode.py`

---

### 6.17 RAG Document Memory

Seno can answer questions about any `.txt` or `.md` files you place in a designated folder.

**Document folder:** `seno_documents\` (configurable in `seno_config.json` via `"rag_folder"`)

**How to use it:**
1. Drop any `.txt` or `.md` files into `seno_documents\`
2. Restart Seno (or it will detect the change and rebuild automatically)
3. Ask about your documents:
   > "Seno, what does my API design document say about authentication?"
   > "Seno, search my notes for anything about the database schema"

**How it works:**
- Documents are chunked into 800-character segments with 100-character overlap
- Each chunk is converted to a vector embedding using `sentence-transformers` (MiniLM-L6-v2)
- Stored in a FAISS matrix for millisecond nearest-neighbor retrieval
- On query, the top 3 most relevant chunks are injected into the LLM context

**Instant-start caching:** Seno hashes the folder metadata and caches the FAISS matrix to disk. If nothing has changed since last boot, the RAG system loads in **< 0.1 seconds** instead of the usual 5+ second embedding computation.

**Live document ingestion:** When `find_document` locates a file, it is injected into the running RAG store in real-time without a restart.

**Session memory:** When you exit Seno (`Ctrl+C`), it automatically writes a summary of the session to `seno_documents/seno_conversations.txt`. This makes past conversations searchable via RAG on future sessions.

**Files:** `rag_store.py`, `seno_documents/`

**Config keys:**
```json
"rag_folder": "seno_documents",
"rag_chunk_chars": 800,
"rag_chunk_overlap": 100
```

---

### 6.18 Chat History & Persistent Memory

Seno remembers the last **10 conversation turns** within a session and across restarts.

- Every turn (user message + Seno response) is saved to `seno_chat_history.json` after each exchange
- On next startup, those 10 turns are rehydrated into the conversation context
- This means Seno remembers what you said 5 minutes ago, or yesterday

The rolling window keeps the last 10 × 2 messages (20 total: 10 user + 10 assistant). Older history falls off automatically.

**Files:** `seno_main.py` — `load_chat_history()`, `save_chat_history()`

---

### 6.19 Task Memory (Overarching Missions)

You can give Seno a persistent background mission that stays in its mind across every conversation turn until you clear it.

**Set a task memory:**
> "Seno, set task memory to 'We are building a FastAPI backend for my e-commerce project'"
> "Seno, remember that our current goal is to migrate the database to PostgreSQL"

**Clear task memory:**
> "Seno, clear task memory"
> "Seno, forget the mission"

The mission text is saved to `seno_task_memory.txt` and injected into every system prompt. Seno stays focused on your overarching goal no matter what other random things you ask it.

**Files:** `dispatcher.py` — `set_task_memory()`, `clear_task_memory()`

---

### 6.20 Workspace Snapshots (Setups)

**Save your current workspace:**
> "Seno, save this setup as development"
> "Seno, save this as my design layout"

Seno scans all currently open windows and saves the list to `seno_setups.json`.

**Restore a workspace:**
> "Seno, load my development setup"
> "Seno, restore the design layout"

Seno re-launches all the apps that were open when you saved that setup.

**Files:** `dispatcher.py` — `save_setup()`, `load_setup()`

---

### 6.21 Parallel Thinking Engine

For extraordinarily difficult problems, Seno spawns 3 independent reasoning agents simultaneously and synthesizes their conclusions into one answer.

**Trigger:**
> "Seno, think deep — what's the best way to architect a distributed event-driven system?"
> "Seno, think hard about this: is it better to use Redis or PostgreSQL for session storage?"
> "Seno, take your time and reason through the trolley problem for me"

**What happens:**
1. Three separate LLM inference calls are dispatched via Python threads
2. Each agent runs at a different temperature signature:
   - **Node 1 (Strict Logic):** temp=0.2 — deterministic, fact-focused
   - **Node 2 (Balanced):** temp=0.7 — logical but natural
   - **Node 3 (Creative):** temp=0.9 — tests edge cases, challenges assumptions
3. Once all three complete, a **4th synthesis LLM call** reads all three outputs, cross-verifies the logic, and produces one final definitive answer
4. The GPU memory pool is protected by `_llm_lock` — all 4 calls serialize safely despite the threads running concurrently

**Files:** `seno_plugins/system/think_deep.py`

---

### 6.22 Execution Memory (Muscle Memory)

During any autonomous agent task, every successful terminal command is recorded. When the task completes, the entire command chain is saved to `seno_execution_memory.json` mapped to the human-readable goal.

**Search muscle memory:**
> "Seno, how did I build the Flask API last time?"
> "Seno, search memory for how I set up Docker"
> "Seno, recall how I deployed the project"

The `recall_execution` plugin searches past execution memory by goal keywords and returns the exact sequence of commands that worked.

**Why this matters:** Instead of the LLM potentially hallucinating a deployment sequence, Seno recalls the actual commands that *you* previously verified worked on *your* machine.

**Files:** `seno_agent.py` — `_save_execution_memory()`, `seno_plugins/system/recall_execution.py`

**Data file:** `seno_execution_memory.json`

---

### 6.23 Error Intelligence Database

Every time the autonomous agent hits an error during a task, and then later finds a command that fixes it — the error+fix pair is automatically recorded.

**How it works:**
- Before executing any terminal command, the agent looks up the command in the error DB using **fuzzy string matching** (65% similarity threshold)
- If a past error signature matches, the known fix is injected into the LLM context as a hint *before* execution
- When a command succeeds after previous errors in the same task, the `(error → fix)` pair is recorded automatically with `record_error()`

**Manual actions:**
> "Seno, what errors have I had before?"
> "Seno, look up this error: ModuleNotFoundError: No module named 'flask'"
> "Seno, record that the fix for CUDA out of memory is to reduce n_ctx to 2048"
> "Seno, clear the error database"

**Fuzzy matching:** Uses `difflib.SequenceMatcher`. Strips memory addresses, line numbers, and timestamps before comparing so the same logical error matches even if the exact file path or line number differs.

**Data file:** `seno_error_db.json`

**Files:** `error_intel.py`, `seno_plugins/system/error_intel_plugin.py`

---

### 6.24 System-Level Workflow Engine

You can define named multi-step automation workflows that chain any combination of Seno's capabilities.

**Save a workflow:**
> "Seno, save a workflow called start_dev with steps: open VSCode, open Chrome and go to localhost 3000, then say I'm ready"

Internally a workflow is a JSON array of action steps:
```json
{
  "start_dev": {
    "description": "Open my dev environment",
    "steps": [
      {"action": "open_app", "params": {"app": "vscode"}},
      {"action": "open_url",  "params": {"url": "http://localhost:3000"}},
      {"action": "say",       "params": {"text": "Dev environment is ready!"}}
    ]
  }
}
```

**Run a workflow:**
> "Seno, run my start_dev workflow"
> "Seno, execute the morning_routine workflow"

**List workflows:**
> "Seno, what workflows do I have?"
> "Seno, list my saved workflows"

**Delete a workflow:**
> "Seno, delete the start_dev workflow"

Workflow steps can use **any dispatcher action** — `open_app`, `close_app`, `mute_volume`, `set_reminder`, `scrape_web`, `run_command`, `say`, etc. Any combination, any length.

**Data file:** `seno_workflows.json`

**Files:** `workflow_engine.py`, `seno_plugins/system/workflow_plugin.py`

---

### 6.25 Learning Engine (Self-Improving)

Seno analyzes your past action history to detect recurring patterns and proactively suggests automating them.

**How it works:**
- Your complete JSON action history is stored in `seno_chat_history.json`
- During idle periods, the background reminder engine triggers a learning scan every ~60 seconds
- The learning engine parses the JSON history, identifies repeated action sequences (e.g. you always open Chrome then VSCode together)
- When a pattern is detected, Seno interrupts with a spoken suggestion: *"I've noticed you often open Chrome and VSCode together. Would you like me to create a workflow for that?"*

**Files:** `learning_engine.py`

---

### 6.26 Security Daemon (Background Monitor)

A dedicated Python thread runs continuously in the background monitoring CPU and RAM usage.

**Trigger threshold:** 92% CPU or RAM usage

When a spike is detected:
1. Seno identifies the top offending process using `psutil`
2. Immediately speaks out loud: *"Warning: {process} is using {X}% of your {CPU/RAM}. Want me to kill it?"*
3. You can respond verbally to confirm or deny

This runs independently of any user interaction — Seno will interrupt itself to tell you if your computer is being throttled.

**Files:** `background_agents.py`

---

### 6.27 Plugin System

Seno's capabilities are extended through a fully dynamic plugin system. Plugins in `seno_plugins/` are discovered, loaded, and fully integrated at startup — no hardcoding in the core.

**Plugin directory structure:**
```
seno_plugins/
├── system/
│   ├── read_screen.py       — OCR screen reading
│   ├── think_deep.py        — Parallel reasoning engine
│   ├── find_document.py     — File system search
│   ├── organize_files.py    — File organization
│   ├── recall_execution.py  — Execution memory search
│   ├── workflow_plugin.py   — Workflow engine
│   └── error_intel_plugin.py — Error intelligence DB
├── coding/
│   └── run_python.py        — Python sandbox executor
├── web/
│   └── scrape_web.py        — Silent web scraper
└── custom/
    ├── change_mode.py       — Conversation mode switcher
    ├── reminders_set.py     — Set reminder
    ├── reminders_list.py    — List reminders
    └── reminders_cancel.py  — Cancel reminder
```

**How plugins are integrated:**
- Each plugin exposes `SCHEMA` (action name), `CAPABILITIES` (natural language description), and `execute(action, params, context)` function
- At startup, `plugin_manager.py` scans all subdirectories, imports every plugin, and injects their capabilities and schema strings directly into the LLM system prompt
- When the LLM outputs a plugin action name, the dispatcher's `safe_run()` calls the plugin's `execute()` function

**To create a custom plugin:** Add a new `.py` file in any subfolder of `seno_plugins/`. It will be discovered and integrated automatically at the next startup — no config changes needed.

**Files:** `plugin_manager.py`

---

### 6.28 Time Awareness & Schedule Context

On every single conversation turn, the system prompt is dynamically rebuilt to include:

- **Current time** (HH:MM format)
- **Time period** (morning / afternoon / evening / late night)
- **Time-appropriate greeting** (Good morning, Good afternoon, etc.)
- **List of upcoming active reminders** (if any are pending)

This means Seno knows it's 11:30 PM when you ask "what should I work on tonight?", or that you have a reminder firing in 15 minutes when you ask what to do next.

**Files:** `seno_main.py` — `get_dynamic_system_prompt()` (lines ~299–325)

---

### 6.29 Urgency Detection

If you say anything that implies urgency, Seno automatically:
1. Forces the **FAST** inference profile (temp=0.15, max_tokens=180) regardless of the router
2. Injects a brevity rule: **reply in 1 sentence maximum**
3. Responds in the shortest possible form

**Trigger keywords:** `hurry`, `quick`, `urgent`, `fast`, `emergency`, `asap`, `immediately`, `right now`, `stop right now`, `now now`, `rush`

Example:
> "Seno, quick — what's 15% of 340?"
> → Seno: *"Fifty-one."* (and nothing more)

**Files:** `seno_main.py` — `ask_seno_and_act()`

---

### 6.30 Computer Lock

> "Seno, lock my computer"
> "Seno, lock the screen"

On Windows: `rundll32 user32.dll,LockWorkStation`
On Linux: tries `loginctl lock-session`, `xdg-screensaver lock`, `gnome-screensaver-command --lock` in order
On macOS: `osascript keystroke "q" with command + control`

**Files:** `dispatcher.py` — `lock_computer()`

---

## 7. Configuration Reference (seno_config.json)

All system settings live in `seno_config.json`. You can edit this file while Seno is not running — changes take effect on the next startup (or next conversation turn for some settings).

```json
{
  "wakeword": "seno",
  "wake_aliases": ["seno", "nervous", "travis", "service", ...],
  "model_name": "qwen",
  "personality": "You are Seno, an offline personal AI assistant...",

  "voice_settings": {
    "speaker": "en_1"
  },

  "apps": {
    "chrome": { "win": "chrome.exe", "linux": "google-chrome", "mac": "..." },
    ...
  },

  "focus_mode_close": ["discord", "spotify", "steam", "chrome", "edge", "firefox"],

  "rag_folder": "seno_documents",
  "rag_chunk_chars": 800,
  "rag_chunk_overlap": 100,

  "user_info": {
    "username": "yassine",
    "home_dir": "C:\\Users\\yassine"
  },

  "mode": "assistant"
}
```

| Key | Description |
|---|---|
| `wakeword` | Primary wake word (default: "seno") |
| `wake_aliases` | Phonetic aliases accepted as wake words |
| `model_name` | LLM model label (informational — model path is in `llm_client.py`) |
| `personality` | The base personality sentence injected at the top of every system prompt |
| `voice_settings.speaker` | Silero TTS voice id (`en_0`, `en_1`, ...) |
| `apps` | Application registry — name → {win, linux, mac} paths |
| `focus_mode_close` | Apps automatically closed when focus mode activates |
| `rag_folder` | Relative path to the RAG document folder |
| `rag_chunk_chars` | Maximum characters per RAG document chunk |
| `rag_chunk_overlap` | Character overlap between adjacent chunks |
| `user_info` | Auto-detected username and home directory |
| `mode` | Current conversation mode: `assistant`, `developer`, or `silent` |

---

## 8. File Structure Reference

```
Jarvis_Ai/
│
├── seno_main.py           ← CORE: Main event loop, message router, system prompt
├── seno_ui.py             ← Graphical HUD interface (Iron Man-style)
├── seno_agent.py          ← Autonomous ReAct agent engine
├── dispatcher.py          ← Action dispatcher — all system actions live here
├── llm_client.py          ← LLM interface (llama.cpp, GPU offload, streaming)
├── task_router.py         ← Hybrid Brain: classifies request complexity
├── rag_store.py           ← FAISS vector store for document memory
├── workflow_engine.py     ← Workflow persistence & execution engine
├── error_intel.py         ← Error intelligence database (fuzzy matching)
├── reminder_engine.py     ← Background alarm daemon (1 TPS tick loop)
├── background_agents.py   ← CPU/RAM security monitor daemon
├── learning_engine.py     ← Proactive behavior pattern analyzer
├── plugin_manager.py      ← Dynamic plugin loader & schema injector
├── web_scraper.py         ← Ghost browser (DDG + Google News RSS)
├── system_senses.py       ← Clipboard, active window, system telemetry
├── stt_whisper.py         ← Faster-Whisper speech-to-text
├── tts_silero.py          ← Silero neural text-to-speech
│
├── seno_plugins/          ← All plugin modules (auto-discovered)
│   ├── system/
│   │   ├── read_screen.py
│   │   ├── think_deep.py
│   │   ├── find_document.py
│   │   ├── organize_files.py
│   │   ├── recall_execution.py
│   │   ├── workflow_plugin.py
│   │   └── error_intel_plugin.py
│   ├── coding/
│   │   └── run_python.py
│   ├── web/
│   │   └── scrape_web.py
│   └── custom/
│       ├── change_mode.py
│       ├── reminders_set.py
│       ├── reminders_list.py
│       └── reminders_cancel.py
│
├── seno_documents/        ← Drop .txt/.md files here for RAG indexing
├── seno_workspace/        ← Autonomous agent working directory
├── models/                ← Place your .gguf model files here
│
├── seno_config.json       ← All user settings
├── Seno.bat               ← Launch HUD interface
├── SenoCmd.bat            ← Launch terminal interface
├── setup.bat              ← First-time installation script
└── requirements.txt       ← Python dependencies
```

---

## 9. Data Files Created at Runtime

These files are created and maintained automatically. You should not delete them (they contain Seno's memory).

| File | Purpose |
|---|---|
| `seno_chat_history.json` | Last 10 conversation turns (reloaded on every boot) |
| `seno_reminders.json` | Pending alarm queue (survives shutdown — alarms still fire on reboot) |
| `seno_execution_memory.json` | Autonomous task command chains (muscle memory) |
| `seno_error_db.json` | Error intelligence database (errors + fixes) |
| `seno_workflows.json` | User-defined named automation workflows |
| `seno_setups.json` | Saved application workspace snapshots |
| `seno_task_memory.txt` | Current overarching mission (persistent focus) |
| `seno_documents/seno_conversations.txt` | Session summaries (indexed by RAG) |
| `.rag_cache/` | Cached FAISS index binary (instant RAG restart) |

---

No registration, no config changes, no restart required — just drop the file in and relaunch.

**Minimal plugin template:**

```python
# seno_plugins/custom/my_plugin.py

def get_schema():
    return {
        "name": "my_action",
        "description": "A description of what this action does, when to use it."
    }

def execute(params, context=None):
    # 'params' is a dict of arguments from the LLM
    # 'context' contains system info (optional)
    
    input_text = params.get("input", "")
    # ... your logic here ...
    
    return True, f"I processed your request: {input_text}"
```

- `get_schema()` defines the action name and description injected into the LLM system prompt.
- `execute()` is called when the LLM outputs this action name.

No registration, no config changes, no restart required — just drop the file in and relaunch.

---

## 11. Known Limitations & Notes

**LLM must be the CUDA build.** If you install `llama-cpp-python` without the CUDA wheel, the model runs on CPU (20–30 seconds per response). The standard `pip install` does NOT include CUDA. See Installation step 4.

**TTS always runs on CPU on Windows.** Silero TorchScript has a known segfault on Windows CUDA. This is intentional — do not attempt to move it to GPU.

**Context window is 3072 tokens.** The system prompt alone is ~2200 tokens at runtime (after dynamic injections). This leaves ~800 tokens for conversation history and user input. Very long user messages or deeply nested chat history may get truncated.

**Screen reading requires extra packages.** `easyocr`, `mss`, `opencv-python-headless`, and `Pillow` are not in `requirements.txt` by default (they are large). Install manually if you want the `read_screen` feature.

**Autonomous agent has a 30-second command timeout.** Any `run_command` that takes longer than 30 seconds will be killed and reported as a timeout. Long build processes should be run in the background using `&` or `start` commands.

**The plugin system uses file-level imports.** If a plugin has a missing dependency, it will fail silently on import and that plugin's actions will not be available. Check the startup console for `[Seno] Failed to load plugins:` messages.

**Microphone hot-plug is supported.** If your mic disconnects mid-session, Seno waits 5 seconds, checks for a connected device, and either resumes mic mode or switches to keyboard mode automatically.

---

*Built entirely locally. Runs entirely locally. Thinks entirely locally.*
*Seno — Phase 6 Complete. 19 capability systems. Zero cloud dependencies.*
