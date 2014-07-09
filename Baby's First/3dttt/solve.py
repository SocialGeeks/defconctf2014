#!/usr/bin/env python

# This needs some logic.  It takes the center squares then the corners and then just bruteforces away at the puzzle.  
# It ties a lot and occasionally wins.

import socket
from socket import *

def connect(host, port):
	try:
		s = socket(AF_INET, SOCK_STREAM)
	except error, msg:
		print("Failed to create socket. Error code: " + str(msg[0]) + " , Error message: " + msg[1])
		sys.exit()

	try:
		remote_ip = gethostbyname(host)
	except gaierror:
		print("Could not resolve hostname.")
		sys.exit()

	s.connect((remote_ip, port))
	return s

def read_board(reply, board):
	# boards are in reply unless it is a wrong guess. Then it starts with C
	if "C" == reply[0][0]:
		return board

	lines = reply.split("\n")

	z = 0 
	for line in lines:
		try:
			y = line[0]
			if "0" == y or "1" == y or "2" == y:
				y = int(y)
				board[0][y][z] = line[3]
				board[1][y][z] = line[7]
				board[2][y][z] = line[11]
#				print " %s | %s | %s " % (line[3], line[7], line[11])
#				print "%s.%s : %s" % (z, y, line)
#				print board
				if 2 == y:
					z+= 1
					if 3 == z:
						break
		except IndexError:
			pass
	return board

def corners(s, board):
        # take the corners
        moves = ["0,0,0\n", "0,2,0\n" "2,0,0\n", "2,2,0\n",
                 "0,0,1\n", "0,2,1\n" "2,0,0\n", "2,2,1\n",
                 "0,0,2\n", "0,2,2\n" "2,0,2\n", "2,2,2\n"]
        for move in moves:
                s.sendall(move)
                reply = s.recv(4096)
		board = read_board(reply, board)
	return board

def centers(s, board):
        # take the center
        for z in range(3):
                move = "1,1,%s\n" % z 
                s.sendall(move)
                reply = s.recv(4096)
		board = read_board(reply, board)
	return board

def print_board(board):
	print board
	return
	for z in range(3):
		for y in range(3):
			row = ""
			for x in range(3):
				row = "%s | %s " % (row, board[x][y][z]) 
		print row
	print " "
	print "..............................................................."

def solve(s, board):
	board = centers(s, board)
	board = corners(s, board)

	for z in range(3):
		for x in range(3):
                	for y in range(3):
                        	move = "%s,%s,%s\n" %(x,y,z)
                        	s.sendall(move)
                        	reply = s.recv(4096)
				board = read_board(reply, board)
				# print the end game and score
                        	if "won" in reply:
					lines = reply.split("\n")
					for line in lines:
						print line
						if "play" in line:
							break	
					print_board(board)
					# recurse away, they will disconnect us
					solve(s, board)
					

if __name__ == "__main__":

        board = [
                        [
                                [' ',' ',' '],
                                [' ',' ',' '],
                                [' ',' ',' '],
                        ],
                        [
                                [' ',' ',' '],
                                [' ',' ',' '],
                                [' ',' ',' '],
                        ],
                        [
                                [' ',' ',' '],
                                [' ',' ',' '],
                                [' ',' ',' '],
                        ],
                ]
	
	host = "3dttt_87277cd86e7cc53d2671888c417f62aa.2014.shallweplayaga.me"
	port = 1234

	s = connect(host, port)

	# intro/banner screen
	reply = s.recv(4096)

	solve(s, board)

