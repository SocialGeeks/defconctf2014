#!/usr/bin/env python

# This needs some logic.  It just bruteforces away at the puzzle with no strategy and has yet to win a game.

import socket
from socket import *

def connect(host, port):
	try:
		s = socket(AF_INET, SOCK_STREAM)
	except error, msg:
		print "Failed to create socket. Error code: " + str(msg[0]) + " , Error message: " + msg[1]
		sys.exit()

	try:
		remote_ip = gethostbyname(host)
	except gaierror:
		print "Could not resolve hostname."
		sys.exit()

	s.connect((remote_ip, port))
	return s

def solve(s):
	for x in range(0,3):
		for y in range(0,3):
                	for z in range(0,3):
                        	move = "%s,%s,%s\n" %(x,y,z)
                        	s.sendall(move)
                        	reply = s.recv(4096)
                        	if "won" in reply:
					if "won -" in reply:
						print reply
						solve(s)
					else:
						print reply
						return	
	
host = "3dttt_87277cd86e7cc53d2671888c417f62aa.2014.shallweplayaga.me"
port = 1234

s = connect(host, port)

# intro/banner screen
reply = s.recv(4096)
#print reply

solve(s)

