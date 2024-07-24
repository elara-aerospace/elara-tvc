# elara-tvc

[![CircleCI Build status](https://circleci.com/gh/elara-aerospace/elara-tvc.svg?style=shield)](https://circleci.com/gh/elara-aerospace/elara-tvc)
[![AppVeyor Build status](https://ci.appveyor.com/api/projects/status/x3at1roteloalwas?svg=true)](https://ci.appveyor.com/project/suriyaa/elara-tvc)
[![codecov](https://codecov.io/github/elara-aerospace/elara-tvc/graph/badge.svg?token=8ZW0F2N90I)](https://codecov.io/github/elara-aerospace/elara-tvc)
[![CodeFactor](https://www.codefactor.io/repository/github/elara-aerospace/elara-tvc/badge/main)](https://www.codefactor.io/repository/github/elara-aerospace/elara-tvc/overview/main)
![GitHub repo size](https://img.shields.io/github/repo-size/elara-aerospace/elara-tvc)

> Elara Aerospace's Trust Vector Control (TVC) software

## Installation

To compile the C code into a shared library:

```bash
gcc -shared -o tvc_hardware.so -fPIC tvc_hardware.c
```

## Development Process

Let's break this down into steps:
- Define the basic structure
- Create the main Python script
- Develop C modules for low-level hardware control
- Implement the control algorithm
- Add telemetry and logging

## File Structure

The are the important files containing the TVC software code:
- `tvc_controller.py`: The main Python script.
- `tvc_hardware.c`: The C module for low-level hardware control. This will be compiled into a shared library that our Python script can use.
- `tvc_hardware.so` (on Linux/macOS) or `tvc_hardware.dll` (on Windows): Compiled C shared library.
- `tvc_log.txt`: Log file.

These names clearly indicate the purpose of each file and follow common naming conventions in software development. The prefix `tvc_` helps identify all files related to the Thrust Vector Control system.

## Functionality

This basic structure provides a foundation for the TVC software. Here's what each part does:
- The Python script defines the main control loop and high-level logic.
- The C module handles low-level hardware interactions for better performance.
- The `TVCController` class manages the control algorithm, including target angle, current angle, and PID gains.
- The control loop runs at 100 Hz, constantly adjusting the TVC based on the difference between target and current angles.
- Logging is implemented to track the system's behavior over time.

## Ideas and Future Improvements (Concept)

To improve this system, consider:
- Implementing full PID control instead of just proportional control.
- Adding error handling and system health checks.
- Implementing a communication protocol to receive commands from a ground station.
- Adding more sophisticated modeling of rocket dynamics.
- Implementing sensor fusion if multiple sensors are available.

## License

Copyright (C) 2024 - present Elara Aerospace.
All rights reserved.
