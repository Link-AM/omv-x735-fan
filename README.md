# omv-x735-fan Control Script

This project contains a few small scripts intended to control a PWM fan connected to a Raspberry Pi based on the core temperature of the Pi.  I originally made it as a better solution to control my x735 board PWM fan on a raspberry pi 4 with OpenMediaVault installed, because the software provided by the x735 manufacturer was deprecated and I was not happy with the fan speed settings.

## 📁 Files
### install.sh
This shell script installs `omv-x735-fan` files.  It installs the python script to /usr/local/bin/, makes it executable, and sets it up to run as a service via the other shell script.

### omv-x735-fan.py
This is the main Python script that controls the fan.  It continuously checks the core temperature and adjusts the speed of the fan accordingly.

### omv-x735-fan.sh
This shell script is used to start and stop the omv-x735-fan.py script as a service. It provides the following commands:

- **start**: Starts the `omv-x735-fan.py` script in the background.
- **stop**: Stops the `omv-x735-fan.py` script by killing the process.

This script is designed to be placed in /etc/init.d/ and run at startup.

## 📋 Requirements
Python
RPi.GPIO and gpiozero Python libraries
Raspberry Pi with a fan connected to a GPIO pin

## 🛠️ Installation
To install the service, run the `install.sh` script with superuser privileges:

```bash
sudo ./install.sh
```
This will copy the necessary files to their appropriate locations and tell the service to start on boot.  It will also start the service immediately without needing to reboot.

To stop the service, use the following command:

```bash
sudo ./omv-x735-fan.sh stop
```

If you want to manually start the service after it has been stopped, you can do so with the following command:

```bash
sudo /etc/init.d/omv-x735-fan.sh start
```

## 🐞 Debugging
The Python script includes a DEBUG_LOGGING constant that can be set to True to enable debug logging. When debug logging is enabled, the script prints the core temperature and the fan speed each time they are checked or changed.
