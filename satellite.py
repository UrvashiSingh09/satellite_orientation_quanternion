import numpy as np
from utils import quaternion_derivative, normalize_quaternion

class Satellite:
    def __init__(self, initial_orientation, angular_velocity):
        self.orientation = np.array(initial_orientation)  # Quaternion [w, x, y, z]
        self.angular_velocity = np.array(angular_velocity)  # [rad/s]

    def update_orientation(self, dt):
        dq = quaternion_derivative(self.orientation, self.angular_velocity)
        self.orientation += dq * dt
        self.orientation = normalize_quaternion(self.orientation)

    def get_orientation(self):
        return self.orientation
