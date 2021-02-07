#!/bin/python3
import sys
import socket
from datetime import datetime

#define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname by ipv4
else:
	print("Invalid amount of arguements.")
	print("Syntax: python3 pscanner.py <ip>")

#add pretty Banner
print("                                                                                   ")
print(" _____     _ _   _         _    _____         _      _____                        ") 
print("|     |___|_| |_|_|___ ___| |  |  _  |___ ___| |_   |   __|___ ___ ___ ___ ___ ___") 
print("|   --|  _| |  _| |  _| .'| |  |   __| . |  _|  _|  |__   |  _| .'|   |   | -_|  _|")
print("|_____|_| |_|_| |_|___|__,|_|  |__|  |___|_| |_|    |_____|___|__,|_|_|_|_|___|_|  ")
print("                                                                                   ")
print("-" * 50)
print("Scanning Target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(20,8080):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns error
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()
