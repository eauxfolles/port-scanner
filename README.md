# port-scanner
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://opensource.org/licenses/MIT)

PoC/Alpha of a tool written in Python to scan through ports of a given IP.

Tool takes IP as parameter, as it accepts indicator for single or multithreading and performs scan through ports. Tested under Windows.

***Usage:*** "portscan.py -option <ip>"

Where:

- "option" is either "-m" (multithreading) or "-s" (single threading)
- "ip" is the target IP

On a Windows 10 system, scanning for 1000 ports via single threading takes around 12 seconds, multithreading around 2 seconds.  
