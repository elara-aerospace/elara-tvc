"""
tvc_controller.py

Copyright (C) 2024 - Elara Aerospace. All rights reserved.

This module contains the TVCController class which handles the control of thrust
vectoring by interfacing with the TVC hardware library.
"""

# Load the Python libraries
import ctypes
import time
import logging
from typing import Tuple

# Load the C library
tvc_lib = ctypes.CDLL('./tvc_hardware.so')

# Set up logging
logging.basicConfig(filename='tvc_log.txt', level=logging.INFO)

class TVCController:
    """
    TVCController handles the control of thrust vectoring
    by interfacing with the TVC hardware library.
    """

    def __init__(self):
        """
        Initializes the TVCController with default target angle,
        current angle, and PID gains.
        """
        self.target_angle: Tuple[float, float] = (0.0, 0.0)  # (pitch, yaw)
        self.current_angle: Tuple[float, float] = (0.0, 0.0)
        self.pid_gains: Tuple[float, float, float] = (1.0, 0.1, 0.05)  # (Kp, Ki, Kd)

    def update_target(self, pitch: float, yaw: float):
        """
        Updates the target angles for pitch and yaw.
        
        :param pitch: Target pitch angle.
        :param yaw: Target yaw angle.
        """
        self.target_angle = (pitch, yaw)

    def get_current_angle(self) -> Tuple[float, float]:
        """
        Retrieves the current pitch and yaw angles from the hardware.
        
        :return: Tuple containing the current pitch and yaw angles.
        """
        pitch = tvc_lib.get_pitch_angle()
        yaw = tvc_lib.get_yaw_angle()
        return (pitch, yaw)

    def calculate_adjustment(self) -> Tuple[float, float]:
        """
        Calculates the adjustment needed for pitch and yaw
        based on the target and current angles using a simple P controller.
        
        :return: Tuple containing the adjustments for pitch and yaw.
        """
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
        """
        Applies the calculated adjustments to the servos.
        
        :param adjustment: Tuple containing the adjustments for pitch and yaw.
        """
        tvc_lib.set_pitch_servo(ctypes.c_float(adjustment[0]))
        tvc_lib.set_yaw_servo(ctypes.c_float(adjustment[1]))

    def run_control_loop(self):
        """
        Runs the main control loop, calculating and applying adjustments
        at a frequency of 100 Hz.
        """
        while True:
            adjustment = self.calculate_adjustment()
            self.apply_adjustment(adjustment)
            logging.info(
                "Target: %s, Current: %s, Adjustment: %s",
                self.target_angle, self.current_angle, adjustment
            )
            time.sleep(0.01)  # 100 Hz control loop

if __name__ == "__main__":
    controller = TVCController()
    controller.run_control_loop()
