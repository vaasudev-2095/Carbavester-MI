#!/usr/bin/env python3
"""
human_trigger.py
If a person is in view, send 'L' over serial; otherwise 'H'.
Tested with Python ≥3.9, OpenCV ≥4.8, ultralytics ≥8.1.0, pyserial ≥3.5
"""

import cv2
from ultralytics import YOLO               # pip install ultralytics
import serial                               # pip install pyserial
import time

# --- CONFIG ------------------------------------------------------------------
CAM_INDEX        = 0         # default webcam
# CAM_INDEX        = 1     #droid cam
MODEL_WEIGHTS    = 'yolov8n.pt' # or yolov8s.pt for higher accuracy
SERIAL_PORT      = 'COM13'       # WIN: something like COM3,   *nix: /dev/ttyACM0
BAUD             = 115200
CONF_THRESHOLD   = 0.5          # detection confidence
# -----------------------------------------------------------------------------


def main():
    # 1. Connect to Arduino
    ser = serial.Serial(SERIAL_PORT, BAUD, timeout=1)
    time.sleep(2)               # allow Arduino to reset

    # 2. Load YOLOv8
    model = YOLO(MODEL_WEIGHTS)

    # 3. Open camera
    cap = cv2.VideoCapture(CAM_INDEX, cv2.CAP_DSHOW)  # CAP_DSHOW avoids long delay on Windows
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam")

    send_state = None            # track last message to avoid spamming serial

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠️  Frame grab failed"); break

            # Run inference (640 px default)
            results = model(frame, verbose=False)[0]

            # Check for "person" detections above threshold
            human_here = any(det.conf > CONF_THRESHOLD and det.cls == 0  # class 0 = person
                              for det in results.boxes)

            # Send serial update only if state changed
            new_state = 'L' if human_here else 'H'
            if new_state != send_state:
                ser.write(new_state.encode())
                send_state = new_state

            # Draw & show for debugging
            annotated = results.plot()   # Ultralytics helper draws boxes
            label = "HUMAN" if human_here else "NO HUMAN"
            cv2.putText(annotated, label, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if human_here else (0, 0, 255), 2)
            cv2.imshow("YOLOv8 Human Detector", annotated)

            if cv2.waitKey(1) & 0xFF in (27, ord('q')):  # ESC/q to quit
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        ser.close()


if __name__ == "__main__":
    main()
