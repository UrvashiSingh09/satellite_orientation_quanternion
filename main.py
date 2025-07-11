import numpy as np
import matplotlib.pyplot as plt
from satellite import Satellite
from scipy.spatial.transform import Rotation as R

# Initial orientation: no rotation
initial_quaternion = np.array([1.0, 0.0, 0.0, 0.0])

# Constant angular velocity: 10°/sec around Z-axis (converted to radians/sec)
omega = np.radians([0, 0, 10])

sat = Satellite(initial_quaternion, omega)

# Simulate for 10 seconds
dt = 0.1
time_steps = int(10 / dt)

orientations = []

for _ in range(time_steps):
    sat.update_orientation(dt)
    orientations.append(sat.get_orientation().copy())

# Convert quaternion to Euler angles for plotting
euler_angles = [R.from_quat(q[[1,2,3,0]]).as_euler('xyz', degrees=True) for q in orientations]
euler_angles = np.array(euler_angles)

# Plot results
plt.figure(figsize=(10,6))
plt.plot(euler_angles[:, 0], label="Roll (X)")
plt.plot(euler_angles[:, 1], label="Pitch (Y)")
plt.plot(euler_angles[:, 2], label="Yaw (Z)")
plt.title("Satellite Orientation (Euler Angles) Over Time")
plt.xlabel("Time step")
plt.ylabel("Degrees")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
