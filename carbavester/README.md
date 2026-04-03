# 🚜 **Human Detection Trigger System**

### *Step one towards a complete Carbavester design*

---

## 📌 **Overview**

This project implements a **real-time human detection system** using *YOLOv8* and a live camera feed.  
Based on detection results, signals are sent to an **Arduino** to control motors and improve operational safety.

---

## ⚙️ **Features**

- 🔍 **Real-time human detection** using *YOLOv8*  
- 🔌 **Serial communication** between Python and Arduino  
- 🤖 **Automatic motor control**  
- ⚡ **Lightweight and efficient system**

---

## 🔄 **Workflow**

**Camera → YOLO Detection → Python Signal → Arduino → Motor Control**

- 🚫 **Human detected** → *System stops*  
- ✅ **No human detected** → *System moves*

---

## 📁 **Project Structure**

- **`human_trigger.py`** – *Detection and signal transmission*  
- **`h_trigger.ino`** – *Motor control logic on Arduino*  
- **`yolov8n.pt`** – *Pretrained detection model*  

---

## 🧰 **Requirements**

- **Python 3.9+**  
- **OpenCV**  
- **Ultralytics YOLOv8**  
- **PySerial**  
- **Arduino IDE**

---

## 📥 **Installation**

```bash
pip install ultralytics opencv-python pyserial
```
▶️ Usage
- 🔌 Connect Arduino to your system
- ⚙️ Update the serial port in the Python file
- ⬆️ Upload Arduino code
- ▶️ Run the script:
```bash
python human_trigger.py
```
**📊 Output Logic**
| **Detection** | **Signal** | **Action** |
| ------------- | ---------- | ---------- |
| *Human*       | **L**      | 🚫 Stop    |
| *No Human*    | **H**      | ✅ Move    |

**🎯 Goal :**
🎯 Goal

**To create a single operational brain using Python and Arduino:**

- 🧠 The laptop (Processor) acts as the main processing unit
- 🔗 The Arduino acts as a node in a larger neural system
- ⚙️ Enables expansion into multiple intelligent modules
- 🚀 Designed to scale into a distributed automation system capable of handling multiple tasks beyond detection

