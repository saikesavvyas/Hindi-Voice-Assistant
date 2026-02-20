# Hindi-Voice-Assistant
A low-latency, fully offline Hindi voice assistant designed to run entirely on a Raspberry Pi (ARM CPU).
The system performs speech recognition, intent processing, and natural Hindi speech synthesis without any cloud services, APIs, or internet dependency.

## Table of Contents

- [About The Project](#about-the-project)
- [Objective](#objective)
- [Key Capabilities](#key-capabilities)
- [System Architecture](#system-architecture)
- [Hardware Used](#hardware-used)
- [Software Stack](#software-stack)
- [Data Flow](#data-flow)
- [Models Used](#models-used)
- [Optimization Decisions](#optimization-decisions)
- [Offline Design Justification](#offline-design-justification)
- [Performance Characteristics](#performance-characteristics)
- [Commands Implemented](#commands-implemented)
- [Challenges & Solutions](#challenges--solutions)
- [Why This Is Impressive](#why-this-is-impressive)
- [Learning Outcomes](#learning-outcomes)
- [Future Improvements](#future-improvements)
- [Technologies Summary](#technologies-summary)

## About The Project

Voice assistants are typically cloud-dependent, raising concerns around privacy, latency, and reliability.
This project demonstrates a completely offline Hindi voice assistant, capable of running on a low-power ARM device, making it suitable for edge AI, embedded systems, and rural or low-connectivity environments.

## Objective

To develop a privacy-preserving, offline Hindi voice assistant that can:
1.   Recognize Hindi speech (ASR)
2.   Understand predefined spoken commands
3.   Respond using natural Hindi speech (TTS)
4.   Provide system information (CPU, Memory, Time)
5.   Run entirely on CPU without internet access

## Key Capabilities

🎙️ Offline Hindi Speech Recognition

🧠 Intent recognition using lightweight Python logic

🔊 Natural Hindi Text-to-Speech output

📊 System information reporting

⚡ Low-latency response on ARM CPU

🔒 No cloud, no APIs, no data leakage

## System Architecture
High-Level Architecture
Hindi Speech → Offline ASR → Intent Processing → Response Generation → Offline TTS → Audio Output

✔ All components run locally
✔ No internet or external services required

## Hardware Used
### Primary Device

Raspberry Pi 4 / Raspberry Pi 5

ARM aarch64 architecture

### Peripherals

USB webcam (used as microphone)

HDMI monitor (audio output)

Standard Raspberry Pi power supply

### Audio Configuration

Input: USB Microphone

Output: HDMI audio (plughw:0,0)

## Software Stack
### Operating System

Raspberry Pi OS (Debian-based, ARM64)

### Programming Language

Python 3.10+


### Key Libraries

| Library	| Purpose |
| :--- | :--- |
| sounddevice	| Audio recording |
| vosk	| Offline Hindi ASR |
| numpy	 | Audio normalization |
| subprocess |	Running Piper + aplay |
| datetime	| Time queries |
| os |	CPU & memory statistics |

## Models Used
### Speech-to-Text (ASR)

Model: vosk-model-small-hi-0.22

Framework: Vosk API

Engine: Kaldi

#### Why Vosk?

1.   Lightweight

2.   Fully offline

3.   CPU-optimized

4.   Embedded-friendly

5.   Hindi language support

### Text-to-Speech (TTS)

Model: hi_IN-rohan-medium.onnx

Framework: Piper TTS

Inference Engine: ONNX Runtime

#### Why Piper?

1.   Neural TTS on CPU

2.   Low memory footprint (~60 MB)

3.   Fast inference on ARM

4.   Natural Hindi voice output

## Data Flow

Audio captured via USB microphone

Audio streamed to Vosk ASR

Hindi speech converted to text

Intent engine processes command

Response text generated

Piper synthesizes Hindi speech

Audio played via HDMI speaker

## Optimization Decisions

1️⃣ Small ASR Model

1.   Reduced RAM usage
2.   Faster inference
3.   Smooth operation on Raspberry Pi

2️⃣ ONNX-Based TTS

1.   Hardware-agnostic
2.   Efficient CPU inference
3.   No GPU required

3️⃣ Short Responses

1.   Only essential information spoken
2.   CPU & memory returned as percentages
3.   Lower response latency

## Offline Design Justification

The system is intentionally designed to be fully offline to ensure:

Complete user privacy,
Zero cloud dependency,
No API keys or subscriptions,
Reliable operation in low-connectivity regions,
Demonstration of real-world edge AI.

## Performance Characteristics
### Speech Recognition

Lightweight Hindi ASR

Optimized for command-based speech

Stable accuracy on embedded hardware

### Text-to-Speech

Neural ONNX model

Natural-sounding Hindi voice

Efficient ARM CPU execution

### Latency

Typical response time: < 2 seconds

Depends on sentence length

## Commands Implemented
### Conversational Commands

1.   नमस्ते
2.   तुम कौन हो
3.   तुम क्या कर सकते हो
4.   क्या तुम ऑनलाइन हो
5.   कैसे हो
6.   धन्यवाद
7.   मदद करो
### Functional Commands

8.   समय बताओ
9.   सीपीयू बताओ
10.   मेमोरी बताओ
11.   बंद करो

## Challenges & Solutions
### HDMI Audio Not Playing

Solution:

aplay -D plughw:0,0
### Bluetooth Mic Instability

Solution:
Switched to USB webcam microphone.

### Low Microphone Gain

Solution:

peak = np.max(np.abs(audio))
audio *= (20000 / peak)
### ARM vs x86 Piper Binary

Solution:
Replaced x86 binary with piper_linux_aarch64.

## Why This Is Impressive

1.   Fully offline voice assistant
2.   Neural ASR + Neural TTS on CPU
3.   Hindi regional language support
4.   Runs on low-power ARM device
5.   Real-world edge AI implementation

### Demonstrates:

1.   Embedded AI deployment
2.   System-level optimization
3.   Audio processing pipelines
4.   Efficient model selection

## Learning Outcomes

1.   Offline speech AI systems
2.   ARM-based optimization
3.   Audio pipeline integration
4.   Edge AI deployment
5.   Hindi language processing challenges

## Future Improvements

1.   Wake-word detection
2.   Streaming ASR
3.   Grammar-constrained recognition
4.   Model quantization
5.   Noise suppression
6.   Custom Hindi intent classifier
7.   UI dashboard

## Technologies Summary
| Component |	Technology |
| :--- | :--- |
| ASR	| Vosk + Kaldi |
| TTS	| Piper + ONNX |
| Audio I/O	| sounddevice + ALSA |
| lAnguage	| Python |
| OS |	Raspberry Pi OS |
| Hardware	| Raspberry Pi (ARM) |

## Team Members
| S Praveen Kumar | vinupraveen2006@gmail.com |
| :--- | :--- |
| Sai Kesav Vyas S | saikesavv@gmail.com |
| R SHreeram | rshreeram.ece2023@citchennai.net |
