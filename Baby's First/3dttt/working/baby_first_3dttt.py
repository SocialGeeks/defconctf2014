import socket
from pprint import pprint as pp

class Board():
	def __init__(self):
		## [z][y][x]
		self.board = [
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

		self.moves = { 'X':set(), 'O':set() }

	def state(self, v):
		for z in range(3):
			x1 = x2 = x3 = True
			for i in range(3):
				x1 &= (v == self.get(i,0,z))
				x2 &= (v == self.get(i,1,z))
				x3 &= (v == self.get(i,2,z))
			if x1 or x2 or x3:
				return True

		for z in range(3):
			x1 = x2 = x3 = True
			for i in range(3):
				x1 &= (v == self.get(0,i,z))
				x2 &= (v == self.get(1,i,z))
				x3 &= (v == self.get(2,i,z))
			if x1 or x2 or x3:
				return True

		for y in range(3):
			x1 = x2 = x3 = True
			for i in range(3):
				x1 &= (v == self.get(0,y,i))
				x2 &= (v == self.get(1,y,i))
				x3 &= (v == self.get(2,y,i))
			if x1 or x2 or x3:
				return True

		for z in range(3):
			z1 = z2 = True
			for i in range(3):
				z1 &= (v == self.get(i,i,z))
				z2 &= (v == self.get(2 - i,i,z))
			if z1 or z2:
				return True

		for z in range(3):
			z1 = z2 = True
			for i in range(3):
				z1 &= (v == self.get(i,z,i))
				z2 &= (v == self.get(2 - i,z,i))
			if z1 or z2:
				return True

		for z in range(3):
			z1 = z2 = True
			for i in range(3):
				z1 &= (v == self.get(z,i,i))
				z2 &= (v == self.get(z,2 - i,i))
			if z1 or z2:
				return True

		z1 = z2 = z3 = z4 = True
		for i in range(3):
			z1 &= (v == self.get(i,i,i))
			z2 &= (v == self.get(i,i,2-i))
			z3 &= (v == self.get(2-i,i,i))
			z4 &= (v == self.get(2-i,i,2-i))
		if z1 or z2 or z3 or z4:
			return True

	def best(self, p):
		for x in range(3):
			for y in range(3):
				for z in range(3):
					isset = self.set(x,y,z,p)
					if isset and self.state(p):
						self.set(x,y,z,' ')
						return (x,y,z,'X')
					elif isset:
						self.set(x,y,z,' ')
						
		return None

	def get(self, x,y,z):
		return self.board[z][y][x]


	def set(self, x,y,z,p):
		if p != ' ': 
			self.moves[p].add((x,y,z))
			if self.get(x,y,z) == ' ':
				self.board[z][y][x] = p
				return True
			return False
		self.board[z][y][x] = p
		return True


	def show(self):

		print('')
		print('X:', [(x,y,z) for x,y,z in self.moves['X']])
		print('O:', [(x,y,z) for x,y,z in self.moves['O']])
		for z in self.board:
			print('')
			first = True
			for y in z:
				if not first:
					print('---+---+---')
				print(' ' + ' | '.join(y) + ' ')
				first = False
				
			print('')

b = Board()


b.set(2,0,0,'X')
b.set(1,1,1,'X')
move = b.best('X')
if move: b.set(*move)
b.show()

if b.state('X'):
	print('X wins')
else:
	print('No wins')


exit(0)
moves = [
	b'0,0,0\n',
	b'2,2,0\n',
	b'2,0,0\n',
]

s = socket.socket()
s.connect(('3dttt_87277cd86e7cc53d2671888c417f62aa.2014.shallweplayaga.me', 1234))

for m in moves:
	recv = s.recv(1024)
	print(recv)
	s.send(m)

recv = s.recv(1024)
print(recv)

