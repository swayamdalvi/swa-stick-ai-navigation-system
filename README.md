<p align="center">
  <img src="images/banner.png" width="100%">
</p>

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Raspberry Pi](https://img.shields.io/badge/RaspberryPi-Zero2W-red)
![AI](https://img.shields.io/badge/AI-Enabled-green)
![IoT](https://img.shields.io/badge/IoT-System-orange)


# Swa-Stick — AI Assistive Navigation System

AI-enabled smart assistive navigation system designed to improve mobility, safety, and independence for visually impaired individuals using embedded systems, computer vision, IoT, and intelligent feedback mechanisms.

---

## Why This Project Matters

According to WHO statistics, millions of visually impaired individuals face daily mobility and navigation challenges. Swa-Stick aims to bridge accessibility gaps using affordable embedded AI technology.

---

## Table of Contents

- Overview
- Features
- Hardware
- Software
- Installation
- Usage
- Architecture
- SDG Mapping
- Future Scope
- Authors

---

## Overview

Swa-Stick combines obstacle detection, GPS navigation, voice assistance, OCR-based text recognition, and haptic feedback into a compact embedded solution powered by Raspberry Pi.

The project aims to provide an affordable and intelligent mobility aid capable of real-time environmental awareness and navigation assistance.

---

## Key Features

- Real-time obstacle detection
- AI-assisted environmental awareness
- GPS-based navigation assistance
- Voice interaction and audio feedback
- OCR-based text recognition
- Haptic vibration alerts
- Embedded edge-AI processing
- Portable low-power architecture

---

## Technologies Used

### Hardware
- Raspberry Pi Zero 2W
- Ultrasonic Sensors
- GPS Module (L86)
- INMP441 MEMS Microphone
- MAX98357 Audio Amplifier
- Li-Po Battery System
- Vibration Motors

### Software
- Python
- OpenCV
- TensorFlow Lite
- Tesseract OCR
- Google Maps API
- Speech-to-Text / Text-to-Speech

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/swa-stick.git
cd swa-stick
```

### Create Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Run Main System

Starts the complete Swa-Stick assistive system.

```bash
python3 system/main.py
```

---

### Run AI Assistant

Starts the AI chatbot and vision assistant module.

```bash
python3 ai/ai_assistant.py
```

---

### Run GPS Module

Starts real-time GPS tracking and location detection.

```bash
python3 gps/gps_reader.py
```

---

### Run Ultrasonic Obstacle Detection

Starts obstacle detection using ultrasonic sensors.

```bash
python3 sensors/ultrasonic.py
```

---

## System Architecture

The system continuously captures environmental data using ultrasonic sensors, camera modules, GPS, and voice inputs.

A Raspberry Pi processes the collected information locally and provides:
- audio-based navigation guidance,
- obstacle alerts,
- object recognition,
- and haptic feedback.

![Block Diagram](images/block-diagram.png)

---

## Repository Structure

```text
hardware/   → Circuit diagrams and hardware resources
software/   → Python source code and AI modules
images/     → Architecture diagrams and setup images
docs/       → Reports, presentations, and documentation
```

---

## SDG Alignment

This project contributes toward:
- SDG 3 — Good Health and Well-Being
- SDG 9 — Industry, Innovation and Infrastructure
- SDG 10 — Reduced Inequalities
- SDG 11 — Sustainable Cities and Communities

---

## SDG Mapping

![SDG Mapping](images/sdg-mapping.png)

---

## Research & Documentation

This repository includes:
- Major project report
- Technical documentation
- System architecture diagrams
- Literature review
- Market analysis
- Testing methodology
- Project presentations

---

## Future Improvements

- Advanced computer vision models
- Cloud connectivity
- Mobile application integration
- Emergency assistance features
- Improved battery optimization

---

## Authors

- Swayam Dalvi & Team Members


Department of Electronics & Telecommunication Engineering  
Don Bosco Institute of Technology, Mumbai

---

## Contributions

Contributions, suggestions, and improvements are welcome.

---

## Contact

- LinkedIn: [Swayam Dalvi](https://www.linkedin.com/in/swayam-dalvi-223483260/)
- GitHub: [@swayamdalvi](https://github.com/swayamdalvi)
- Email: swayamdalvi.dbit@gmail.com
