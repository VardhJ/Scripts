#!/bin/python

#To scan ip for a selected port range to check active ports

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])  #Translate hostname too IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: pyhton3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,90):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #stream is the port
		socket.setdefaulttimeout(1) #timeout if port not found
		result = s.connect_ex((target,port)) #returns an error indicator
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
	print("Time of project: "+str(datetime.now()))

except KeyboardInterrupt: #ctrl+c
	print("\nExiting program.")
	sys.exit()        #clean exit 

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error: #socketnotfound
	print("Couldn't connect to server.")
	sys.exit()
