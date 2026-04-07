(!)[https://img.shields.io/badge/Python-1343F2]

# SysMonitor
SysMonitor is an open source code written in Python that monitors the system in any OS of your computer. It monitors memory, cpu usage, processes, disk usage, and network traffic. The code will show the information about the hostname, architecture, machine and the version of your computer.

## Features
- Full computer information display.
- User friendly CLI based UI.
- Real time CPU Usage calculation.
- Arranged layout.
- Nettwork traffic and adaptors display
- Disk usage
- Memory and swap memory usage
- Top processes with usage display.

## Installation
1. Type the following command below to get the source code.
```
git clone https://github.com/Venomsec45/SysMonitor.git
```

2. Go to the code's directory
```
cd SysMonitor
```

3. Create the virtual environment
```
python3 -m venv ~/.venv
```

4. Activate the virtual environment
```
source ~/.venv/bin/activate
```

Reminder:
- Creating and activating the virtual environment will vary different in all OS. You may use commands based on your OS.

5. Install missing dependencies
```
pip install -r requirements.txt
```

Reminder:
- Python is needed to be installed to use pip to install these dependencies.
- You may manually install dependencies but it will consume a lot of time.

## Usage
Run the code to monitor the system.
```
python3 main.py
```

## Limitations
- In Unix/Linux systems, running the code with sudo may be required as the code will run to an error. Type the command below to run the code with sudo.
```
sudo python3 main.py
```
- In Windows, running the code as an administrator may be required as the protective measures will prevent the code from checking system processes and information.
- The code has no GUI provided.
- No process termination.
- No GPU Usage display.
- No webhost display.

## Potential features to be added
- GPU Usage display.
- Process termination.
- GUI display.
- Simple and deep monitor modes.
- Webhost display.
- Interactive UI.







