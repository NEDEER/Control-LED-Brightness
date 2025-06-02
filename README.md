# 🤚💡 Hand Gesture Controlled LED Brightness with Arduino

This project demonstrates how to **control the brightness of an LED using hand gestures** detected via a **webcam**. Using **Python**, the **CVZone** library, and an **Arduino**, the system tracks the distance between fingers and adjusts the LED's brightness in real-time through PWM (Pulse Width Modulation).

---

## 🎯 Features

- Real-time gesture tracking using a PC camera
- Adjust LED brightness by changing the distance between thumb and index finger
- Smooth analog control using Arduino PWM output
- Serial communication between Python and Arduino

---

## 🧰 Components Required

| Component         | Description                          |
|------------------|--------------------------------------|
| Arduino Uno/Nano | Microcontroller board                |
| 1x LED           | To show brightness changes           |
| 1x Resistor      | 220Ω resistor for the LED            |
| Jumper Wires     | For connections                      |
| Breadboard       | For prototyping                      |
| PC Webcam        | Laptop webcam or USB webcam          |

---

## ✨ How It Works

1. The **webcam** captures the hand in real-time.
2. Python uses **CVZone's HandTrackingModule** to detect landmarks on the hand.
3. The distance between the **thumb and index finger tips** is calculated.
4. This distance is mapped to a value between **0 and 255**.
5. The value is sent to the **Arduino via serial**, which adjusts the **PWM signal** to change LED brightness.
<img width="326" alt="image" src="https://github.com/user-attachments/assets/f47aab9b-f9a0-4742-8ba3-ba9c1403af96" />

---

## 💻 Software Setup

### 1. Install Python Libraries

```bash
pip install opencv-python cvzone pyserial numpy
