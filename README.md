
 # 🛰️ Satellite Orientation Simulation Using Quaternions

This project simulates the 3D rotation (attitude) of a satellite using **quaternions**, which are mathematical tools commonly used in aerospace for smooth and efficient orientation tracking. The simulation visualizes how a satellite rotates over time based on constant angular velocity input.

---

## 📌 Key Features

- Simulate satellite orientation using quaternion math.
- Convert quaternion orientation to Euler angles for easier interpretation (Roll, Pitch, Yaw).
- Plot real-time orientation change using `matplotlib`.
- Modular code with clean structure and reusable functions.

---

## 📁 Project Structure

satellite_orientation_quaternion/
├── main.py # Main script to run the simulation
├── satellite.py # Satellite class to update orientation
├── utils.py # Quaternion math and normalization
├── requirements.txt # Python package dependencies
└── README.md # Project documentation (you are here)

---

## 🧠 Background: Why Quaternions?

- Avoid **gimbal lock**, a common problem with Euler angles.
- More efficient and numerically stable than rotation matrices.
- Preferred in aerospace for representing and computing 3D orientations.

---

## 📦 Requirements

Install the required Python packages using pip:
pip install -r requirements.txt
Or manually install them:
pip install numpy scipy matplotlib

---

🚀 How to Run the Project
1. Clone the Repository
git clone https://github.com/your-username/satellite_orientation_quaternion.git
cd satellite_orientation_quaternion
2. (Optional) Create a Virtual Environment
python -m venv venv

# Activate:
# On Windows:
venv\Scripts\activate

# On macOS/Linux:

source venv/bin/activate
1. Install the Dependencies
pip install -r requirements.txt
2. Run the Simulation
python main.py
A plot window will open showing the evolution of Roll, Pitch, and Yaw over time.


🧪 Sample Output
The simulation shows how a satellite rotates over time using quaternions. The orientation is converted to Euler angles and plotted:<img width="1470" height="956" alt="Screenshot 2025-07-11 at 23 00 49" src="https://github.com/user-attachments/assets/dcd3b3af-7c5c-4ca2-8cbe-71413403b10f" />



🔮 Future Enhancements

✅ Add 3D visualization using vpython or matplotlib 3D.

✅ Simulate variable angular velocities or real IMU data.

✅ Integrate with Kalman Filter for noisy data estimation.

✅ Add GUI or web interface using Streamlit.


📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

👨‍💻 Author
Urvashi Singh
B.Tech in AI & Data Science
https://www.linkedin.com/in/urvashi-singh-25495a25a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

