#!/usr/bin/env python3
# ==============================================================================
# Name: portscan.py (Port Scanner)
# Version: v2 (alpha)
# Author: eauxfolles
# Date: 19.04.2020
# Description: Script to scan ports utilizing multithreading
# Usage: "portscan.py -option <ip>"
# ==============================================================================

from os import system, name
import time
import sys
import socket
import threading
from queue import Queue

thread_bool = True			# switch to use or ignore multithreading
threads_amount = 50			# number of possible threads
thread_overview = []			# overview of the running threads
my_queue = Queue()			# defining the queue including ports to be scanned
target_ip = ""				# holding the ip to be scanned
port_low = 1				# first port to be scanned (start of range)
port_high = 1000			# last port to be scanned (end of range, max 65535)
time_start = 0				# time measured prior performing the scans
time_end = 0				# time measured after performing the scans

# function to validate input provided with command line (has to be 2 parameters or "-help")
def validate_command_line():

	if len(sys.argv) < 2:
		print_header(exit_code = "error: no parameters provided")
	elif sys.argv[1] == "-help" or sys.argv[1] == "--help":
			print_header(exit_code = "usage: portscan.py -option <ip>")
	elif len(sys.argv) == 3:
		target_ip = socket.gethostbyname(sys.argv[2])
		if sys.argv[1] == "-m":
			thread_bool = True
		elif sys.argv[1] == "-s":
			thread_bool = False
		else:
			print_header(exit_code = "error: wrong specification of thread-parameter")
	else:
		print_header(exit_code = "error: wrong number of parameters")

	return thread_bool, target_ip

# function to scan ports of defined ip using multithreading
def scan_multithread():

	print_header()
	print("Multithreading:\n")
	my_queue = fill_queue()

	for i in range(threads_amount):
		new_thread = threading.Thread(target=loop_queue)
		thread_overview.append(new_thread)

	for j in thread_overview:
		j.start()

	for k in thread_overview:
		k.join()

# function to fill the queue with ports
def fill_queue(): 

	for i in range(port_low, port_high):
		my_queue.put(i)
	return my_queue

# function used for initiating threads
def loop_queue():

	while not my_queue.empty():
		current_port = my_queue.get()
		scan_port(current_port)

# function to scan ports of defined ip using single threading
def scan_singlethread(): 

	print_header()
	print("Single Threading:\n")
	for port in range(port_low, port_high):
		scan_port(port)

# helper-function which scans single port
def scan_port(single_port):

		my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.01)
		try:
			result = my_socket.connect_ex((target_ip, single_port))
			if result == 0:
				print("port " + str(single_port) + " is open")
#			else:
#				print("port " + str(single_port) + " is closed")
			my_socket.close()
		except:
			pass

# function to print header and error/help-messages
def print_header(exit_code = "no"):

	if name == "nt":
		system("cls")
	else: 
		system("clear")

	print("portscan.py - v2", "\n")

	if exit_code != "no":
		print(exit_code, "\n")
		sys.exit()

# main body calling functions
thread_bool, target_ip = validate_command_line()

time_start = time.perf_counter()

if thread_bool == True:
	scan_multithread()
else: 
	scan_singlethread()

time_end = time.perf_counter()

print("\nscan took %.2f seconds" % round(float((time_end - time_start)),2) + "\n")
