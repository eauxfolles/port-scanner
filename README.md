# port-scanner
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

PoC/Alpha of a tool written in Python to scan through ports of a given IP.

Function: Tool takes IP as parameter, as it accepts indicator for single or multithreading and performs scan through ports.

***Usage:*** "portscan.py -option <ip>"

Where:

- "option" is either "-m" (multithreading) or "-s" (single threading)
- "ip" is the target IP

On a Windows 10 system, scanning for 1000 ports via single threading takes around 12 seconds, multithreading around 2 seconds.  
