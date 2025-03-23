# Dino Gesture Control 🦖✋
Control the Google Chrome Dino game using hand gestures with OpenCV and MediaPipe. Raise your fingers, and the Dino jumps automatically—no keyboard needed!

# Demo
![Demo](demo.gif)

## Features
✅ Tracks hand movements in real-time using OpenCV & MediaPipe  
✅ Detects finger motion to simulate the "space" key press  
✅ Works seamlessly with the Google Chrome Dino game  
✅ No additional hardware required—just a webcam  

## Installation
1️⃣ Clone the repository   
 ```bash
git clone https://github.com/NipunDharmarathne/DinoGestureControl.git  
cd DinoGestureControl  
 ```

2️⃣ Create the Virtual Environment  
###### For Windows:
 ```bash
python -m venv venv
 ```
###### For macOS/Linux:
 ```bash
python3 -m venv venv
 ```

3️⃣ Activate the Virtual Environment  
###### For Windows:
 ```bash
venv\Scripts\activate
 ```
###### For macOS/Linux:
 ```bash
source venv/bin/activate
 ```

4️⃣ Install dependencies  
 ```bash
pip install -r requirements.txt  
 ```

5️⃣ Run the script  
 ```bash
python dino_gesture_control.py 
 ```  
 
## How It Works
1️⃣ The webcam captures real-time hand gestures.  
2️⃣ MediaPipe detects finger positions.  
3️⃣ The script calculates the average Y-coordinate of four fingers.  
4️⃣ If fingers move upwards beyond a threshold, the "space" key is pressed, making the Dino jump!  

## Dependencies
✔️ opencv-python – Captures video from the webcam and processes frames for hand detection.  
✔️ mediapipe – Detects and tracks hand landmarks to recognize finger movements.  
✔️ pyautogui – Simulates keyboard input (pressing the spacebar) to make the dino jump.  
(All dependencies are automatically installed via requirements.txt.)

## Usage Tips
➡️ Ensure proper lighting for accurate hand tracking.  
➡️ Keep your fingers visible to the camera.  
➡️ Adjust the threshold in the script if the jumps feel too sensitive.  

## License
📜 This project is licensed under the MIT License.

## Contributing
🚀 Feel free to contribute by improving gesture detection or adding new features!
