from sys import stdout

pre_defined_matrix = [[2,3,1,1],[1,2,3,1],[1,1,2,3],[3,1,1,2]]

def make_matrix(message):
	arr = []
	if len(message) < 16:
		message += ' '*(16 - len(message))

	for i in range(0,len(message),4):
		a = []
		for j in range(i,i+4):
			a.append(ord(message[j]))
		arr.append(a)
	# print_matrix(arr)
	return arr

# make_matrix('saikrishna')

def xor_matrix(a,b):
	c = [[0 for _ in range(4)] for __ in range(4)]
	for i in range(4):
		for j in range(4):
			c[i][j] = a[i][j] ^ b[i][j]
	return c

def clean_matrix(a):
	for i in range(4):
		for j in range(4):
			if a[i][j] < 48:
				a[i][j]^=65
	return a

def print_matrix(a):
	for i in a :
		print(i)
	print()


def rotate_key_matrix(a):
	# rotate outer matrix
	idx1 = [(0,0),(0,1),(0,2),(0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0),(2,0),(1,0)]
	idx2 = [(1,0),(0,0),(0,1),(0,2),(0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0),(2,0)]
	c = [[0 for _ in range(4)] for __ in range(4)]

	for i in range(len(idx1)):
		x,y = idx1[i]
		x2,y2 = idx2[i]
		c[x][y] = a[x2][y2]

	# rotate outer matrix
	idx1 = [(1,1),(1,2),(2,1),(2,2)]
	idx2 = [(2,1),(1,1),(2,2),(1,2)]

	for i in range(len(idx1)):
		x,y = idx1[i]
		x2,y2 = idx2[i]
		c[x][y] = a[x2][y2]

	return c
	

# 11 12 21 22
# 21 11 22 12


def convert_to_string(a):
	s = []
	for i in range(4):
		for j in range(4):
			s.append(chr(a[i][j]))

	return ''.join(s)

def each_round(message,key,pre_defined_matrix):

	m = make_matrix(message)
	mp = xor_matrix(m,pre_defined_matrix)
	matrix_key = make_matrix(key)
	mk = xor_matrix(mp,matrix_key)
	key_matrix = rotate_key_matrix(matrix_key)
	me = xor_matrix(mk, key_matrix)
	me = clean_matrix(me)
	s = convert_to_string(me)
	next_key = convert_to_string(key_matrix)
	return s,next_key

def next_round(message,key,pre_defined_matrix,matrix_key):
	m = make_matrix(message)
	mp = xor_matrix(m,pre_defined_matrix)

	mk = xor_matrix(mp, matrix_key)
	key_matrix = rotate_key_matrix(matrix_key)
	me = xor_matrix(mk,key_matrix)
	me = clean_matrix(me)
	s = convert_to_string(me)
	return s, convert_to_string(key_matrix)



def break_string(tot):
	a = message[:16]
	b = message[16:]
	return a,b

message = input()
encrypted = input()
key = input()
if len(message) <= 16:
	cnt = 0
	while message != encrypted:
		message, key =  each_round(message,key,pre_defined_matrix)
		pre_defined_matrix = rotate_key_matrix(pre_defined_matrix)
		cnt+=1

	stdout.write(str(cnt))
else:	
	a = message[:16]
	b = message[16:]
	cnt = 0
	while message != encrypted:
		a, key1 =  each_round(a, key , pre_defined_matrix)
		b, key2 =  each_round(b, key , pre_defined_matrix)
		pre_defined_matrix = rotate_key_matrix(pre_defined_matrix)
		message = a + b
		key = key1
		# print(message)
		cnt+=1
	print(cnt)




"""
saikrishna
cp`bskpio`cbb``c
sai

abcdefghijklmnopqrstuvwxyz
kjdoifeeihkcomms;{u~:tw6{zclbcbc
hello
"""
	