# 🛰️ Satellite Orientation Simulation Using Quaternions

This Python project simulates a satellite's 3D orientation (attitude) using **quaternions**, which are widely used in aerospace for representing rotations efficiently and avoiding gimbal lock.

> 🚀 Accurately track how a satellite rotates over time based on angular velocity input using quaternion-based orientation math.

---

## 📽️ Demo

![Satellite Rotation Plot](https://github.com/your-username/satellite_orientation_quaternion/demo.gif)
> Real-time plot of satellite orientation (Roll, Pitch, Yaw)

---

## 🧠 Concepts Covered

- Quaternion math for rotation
- Angular velocity to quaternion integration
- Satellite attitude simulation
- Euler angle conversion for visualization
- Real-time plotting using `matplotlib`

---

## 📁 Project Structure

satellite_orientation_quaternion/
├── main.py # Runs the simulation
├── satellite.py # Satellite class with orientation logic
├── utils.py # Quaternion math functions
├── requirements.txt # Dependencies
└── README.md # You are here!

📦 Dependencies
numpy
scipy
matplotlib

📊 Sample Output
The script simulates a satellite rotating around the Z-axis and visualizes the orientation change over time:
📈 Yaw increases linearly (since it’s rotating only around Z)
✅ Smooth orientation updates using quaternion math
🎯 Euler angles converted for better human-readable visualization


🧠 Why Quaternions?
-Quaternions are ideal for satellite orientation because they:
-Avoid gimbal lock
-Require less computation than rotation matrices
-Enable smooth interpolation and real-time updates

📚 References
NASA Technical Reports on Attitude Control
Wikipedia: Quaternion Rotation
SciPy Spatial Transform Docs
