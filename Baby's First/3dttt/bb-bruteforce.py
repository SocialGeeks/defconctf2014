#!/usr/bin/env python

# This needs some logic.  It takes the center squares then the corners and then just bruteforces away at the puzzle.  
# It ties a lot and occasionally wins.
# Credit goes to viking that wrote the first version of this, binbuddha just chopped it up and got lucky.
# ending is:
# You've won 50 rounds...Let's play again
# 
# Just kidding...congrats!
# The flag is: It's much easier if you put on your 3D glasses...

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
        # take the corners
        moves = ["1,1,1\n",

		"0,0,0\n", 
		"0,0,2\n", 

		"2,0,0\n", 
		"2,0,2\n", 

		"0,2,0\n", 
		"0,2,2\n", 

		"2,2,0\n", 
		"2,2,2\n", 

		"1,1,2\n", 
		"1,1,0\n", 

		"1,0,0\n", 
		"1,0,2\n", 

		"1,2,0\n", 
		"1,2,2\n", 

		"0,1,0\n", 
		"2,1,0\n", 

		"0,1,2\n", 
		"2,1,2\n", 

		"0,0,1\n", 
		"0,2,1\n", 

		"2,2,1\n", 
		"2,0,1\n", 

		"0,0,1\n", 
		"2,0,1\n", 

		"1,0,1\n", 
		"1,2,1\n", 

		"0,1,1\n", 
		"2,1,1\n", ]

        for move in moves:
                s.sendall(move)
                reply = s.recv(4096)
        	if "won" in reply:
			lines = reply.split("\n")
			for line in lines:
				print line
				if "play" in line:
					break	
			# recurse away, they will disconnect us
			# to complete the inelegance of this script, I just used wireshark to grab the last line/flag.
			solve(s)

					

if __name__ == "__main__":
	
	host = "3dttt_87277cd86e7cc53d2671888c417f62aa.2014.shallweplayaga.me"
	port = 1234

	s = connect(host, port)

	# intro/banner screen
	reply = s.recv(4096)
	#print reply

	solve(s)
