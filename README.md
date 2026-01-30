# eSim Automated Tool Manager

A Python-based automated manager for installing, updating, configuring, and managing external tools required by eSim.

## Requirements

- Python 3
- Windows / Linux
- Package manager (apt / chocolatey)

## How to Run

Open terminal inside the folder and run:

python tool_manager.py --list  
python tool_manager.py --install ngspice  
python tool_manager.py --version ngspice  
python tool_manager.py --update ngspice  
python tool_manager.py --check-deps  
python tool_manager.py --config  

## Features

- Tool installation management
- Version control and update system
- Dependency checker
- Environment configuration
- CLI Interface
- Logging support
