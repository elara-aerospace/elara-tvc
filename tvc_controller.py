import ctypes
import time
import logging
from typing import Tuple

# Load the C library
tvc_lib = ctypes.CDLL('./tvc_hardware.so')

# Set up logging
logging.basicConfig(filename='tvc_log.txt', level=logging.INFO)

class TVCController:
    def __init__(self):
        self.target_angle: Tuple[float, float] = (0.0, 0.0)  # (pitch, yaw)
        self.current_angle: Tuple[float, float] = (0.0, 0.0)
        self.pid_gains: Tuple[float, float, float] = (1.0, 0.1, 0.05)  # (Kp, Ki, Kd)

    def update_target(self, pitch: float, yaw: float):
        self.target_angle = (pitch, yaw)

    def get_current_angle(self) -> Tuple[float, float]:
        pitch = tvc_lib.get_pitch_angle()
        yaw = tvc_lib.get_yaw_angle()
        return (pitch, yaw)

    def calculate_adjustment(self) -> Tuple[float, float]:
        current = self.get_current_angle()
        error = (
            self.target_angle[0] - current[0],
            self.target_angle[1] - current[1]
        )
        # Simple P control for now, can be expanded to PID
        adjustment = (
            error[0] * self.pid_gains[0],
            error[1] * self.pid_gains[0]
        )
        return adjustment

    def apply_adjustment(self, adjustment: Tuple[float, float]):
        tvc_lib.set_pitch_servo(ctypes.c_float(adjustment[0]))
        tvc_lib.set_yaw_servo(ctypes.c_float(adjustment[1]))

    def run_control_loop(self):
        while True:
            adjustment = self.calculate_adjustment()
            self.apply_adjustment(adjustment)
            logging.info(f"Target: {self.target_angle}, Current: {self.current_angle}, Adjustment: {adjustment}")
            time.sleep(0.01)  # 100 Hz control loop

if __name__ == "__main__":
    controller = TVCController()
    controller.run_control_loop()
