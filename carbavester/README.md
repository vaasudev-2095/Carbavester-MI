# Carbavester

Carbavester is an automated carbonation system for beverages using Arduino and YOLOv8 computer vision.

## Hardware Components
- Arduino Uno
- Ultrasonic sensor (HC-SR04)
- Servo motor for valve control
- Raspberry Pi or similar for running YOLOv8
- CO2 canister with regulator
- Glass/bottle holder

## Software Components
- `h_Trigger/h_Trigger.ino`: Arduino firmware for sensor reading and valve control
- `h_trigger.py`: Python script for YOLOv8 detection and triggering Arduino
- `yolov8n.pt`: YOLOv8 nano model trained for bottle detection

## Setup Instructions

### 1. Hardware Setup
