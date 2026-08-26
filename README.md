# automation-tool-18

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

automation-tool-18 is a Python library for creating game automation scripts. It simplifies the development of tools that perform repetitive in-game tasks using input simulation and screen analysis.

## Features
- Record and playback of mouse and keyboard macros with adjustable timing parameters
- Integration with OpenCV for real-time image matching and event triggering
- Support for loading automation profiles from YAML configuration files
- Randomized input delays and movement patterns to reduce detection risks

## Installation

```bash
git clone https://github.com/Developer/automation-tool-18.git
cd automation-tool-18
pip install -r requirements.txt
```

## Usage

Execute the tool using a configuration file:

```bash
python -m automation_tool_18 --config config/farming.yaml
```