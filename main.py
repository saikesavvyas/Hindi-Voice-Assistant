import time
import sounddevice as sd
import json
import subprocess
import signal
import sys
import numpy as np
import os
from datetime import datetime
from vosk import Model, KaldiRecognizer

# -------------------------
# CONFIG
# -------------------------
MODEL_PATH = "models/vosk-model-small-hi-0.22"
PIPER_MODEL = "./piper/models/hi_IN-rohan-medium.onnx"
MIC_DEVICE = 1
RECORD_SECONDS = 1.5

model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, 16000)

# -------------------------
# CLEAN EXIT
# -------------------------
def shutdown(signal_received=None, frame=None):
    print("\nShutting down assistant...")
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)

# -------------------------
# RECORD AUDIO
# -------------------------
def record_audio():
    print("Recording...")

    recording = sd.rec(
        int(RECORD_SECONDS * 16000),
        samplerate=16000,
        channels=1,
        dtype='int16',
        device=MIC_DEVICE
    )
    sd.wait()

    audio = recording.astype(np.float32)
    peak = np.max(np.abs(audio))
    if peak > 0:
        audio *= (20000 / peak)

    audio = np.clip(audio, -32768, 32767)
    return audio.astype(np.int16).tobytes()

# -------------------------
# ASR
# -------------------------
def speech_to_text(audio_bytes):
    recognizer.AcceptWaveform(audio_bytes)
    result = recognizer.FinalResult()
    recognizer.Reset()
    return json.loads(result)["text"]

# -------------------------
# SYSTEM FUNCTIONS
# -------------------------
def get_cpu_usage():
    load = os.getloadavg()[0]
    cores = os.cpu_count()
    percent = int((load / cores) * 100)
    return f"सीपीयू उपयोग {percent} प्रतिशत"

def get_memory_usage():
    with open("/proc/meminfo") as f:
        lines = f.readlines()
    total = int(lines[0].split()[1])
    available = int(lines[2].split()[1])
    used = total - available
    percent = int((used / total) * 100)
    return f"मेमोरी उपयोग {percent} प्रतिशत"

# -------------------------
# INTENT ENGINE
# -------------------------
def handle_intent(text):
    text = text.lower()

    if "नमस्ते" in text or "हैलो" in text:
        return "नमस्ते, मैं तैयार हूँ"

    elif "तुम कौन" in text:
        return "मैं ऑफलाइन एआई असिस्टेंट हूँ"

    elif "तुम क्या कर" in text:
        return "मैं समय और सिस्टम जानकारी बता सकता हूँ"

    elif "ऑनलाइन" in text:
        return "नहीं, मैं पूरी तरह ऑफलाइन काम करता हूँ"

    elif "कैसे हो" in text:
        return "मैं ठीक हूँ"

    elif "धन्यवाद" in text:
        return "आपका स्वागत है"

    elif "मदद" in text:
        return "आप समय, सीपीयू और मेमोरी पूछ सकते हैं"

    elif "सीपीयू" in text:
        return get_cpu_usage()

    elif "मेमोरी" in text:
        return get_memory_usage()

    elif "समय" in text:
        return f"अभी समय {datetime.now().strftime('%H:%M')}"

    elif "बंद" in text:
        return "अलविदा", "exit"

    else:
        return "मैं समझ नहीं पाया"

# -------------------------
# TTS
# -------------------------
def speak(text):
    print("Assistant:", text)

    subprocess.run(
        [
            "./piper/piper",
            "--model", PIPER_MODEL,
            "--output_file", "out.wav"
        ],
        input=text.encode("utf-8"),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    subprocess.run(
        ["aplay", "-D", "plughw:0,0", "-q", "out.wav"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

# -------------------------
# MAIN LOOP
# -------------------------
def main():
    print("Offline Hindi AI Assistant Ready")
    speak("नमस्ते, मैं तैयार हूँ")

    while True:
        input("\nPress ENTER to talk (Ctrl+C to exit)")

        audio = record_audio()

        text = speech_to_text(audio)
        print("Recognized:", text)

        if not text.strip():
            continue

        response = handle_intent(text)

        if isinstance(response, tuple):
            speak(response[0])
            shutdown()
        else:
            speak(response)

if __name__ == "__main__":
    main()