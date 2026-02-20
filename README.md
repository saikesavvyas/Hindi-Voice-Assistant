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

Reduced RAM usage

Faster inference

Smooth operation on Raspberry Pi

2️⃣ ONNX-Based TTS

Hardware-agnostic

Efficient CPU inference

No GPU required

3️⃣ Short Responses

Only essential information spoken

CPU & memory returned as percentages

Lower response latency

## Offline Design Justification

The system is intentionally designed to be fully offline to ensure:

Complete user privacy

Zero cloud dependency

No API keys or subscriptions

Reliable operation in low-connectivity regions

Demonstration of real-world edge AI

## Performance Characteristics
Speech Recognition

Lightweight Hindi ASR

Optimized for command-based speech

Stable accuracy on embedded hardware

Text-to-Speech

Neural ONNX model

Natural-sounding Hindi voice

Efficient ARM CPU execution

Latency

Typical response time: < 2 seconds

Depends on sentence length

## Commands Implemented
Conversational Commands

नमस्ते

तुम कौन हो

तुम क्या कर सकते हो

क्या तुम ऑनलाइन हो

कैसे हो

धन्यवाद

मदद करो

Functional Commands

समय बताओ

सीपीयू बताओ

मेमोरी बताओ

बंद करो

## Challenges & Solutions
HDMI Audio Not Playing

Solution:

aplay -D plughw:0,0
Bluetooth Mic Instability

Solution:
Switched to USB webcam microphone.

Low Microphone Gain

Solution:

peak = np.max(np.abs(audio))
audio *= (20000 / peak)
ARM vs x86 Piper Binary

Solution:
Replaced x86 binary with piper_linux_aarch64.

## Why This Is Impressive

Fully offline voice assistant

Neural ASR + Neural TTS on CPU

Hindi regional language support

Runs on low-power ARM device

Real-world edge AI implementation

Demonstrates:

Embedded AI deployment

System-level optimization

Audio processing pipelines

Efficient model selection

## Learning Outcomes

Offline speech AI systems

ARM-based optimization

Audio pipeline integration

Edge AI deployment

Hindi language processing challenges

## Future Improvements

Wake-word detection

Streaming ASR

Grammar-constrained recognition

Model quantization

Noise suppression

Custom Hindi intent classifier

UI dashboard

## Technologies Summary
Component	Technology
ASR	Vosk + Kaldi
TTS	Piper + ONNX Runtime
Audio I/O	sounddevice + ALSA
Language	Python
OS	Raspberry Pi OS
Hardware	Raspberry Pi (ARM)
