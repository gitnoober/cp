from os import path
import sys
# mod = int(1e9 + 7)
# import re
from math import ceil, floor,gcd,log,log2 ,factorial
from collections import defaultdict , Counter
from itertools import permutations
# from bisect import bisect_left, bisect_right
#popping from the end is less taxing,since you don't have to shift any elements
maxx = float('inf')
I = lambda :int(sys.stdin.buffer.readline())
tup= lambda : map(int , sys.stdin.buffer.readline().split())
lint = lambda :[int(x) for x in sys.stdin.buffer.readline().split()]
S = lambda: sys.stdin.readline().replace('\n', '').strip()
def grid(r, c): return [lint() for i in range(r)]
# def debug(*args, c=6): print('\033[3{}m'.format(c), *args, '\033[0m', file=sys.stderr)
stpr = lambda x : sys.stdout.write(f'{x}' + '\n')
star = lambda x: print(' '.join(map(str, x)))
if (path.exists('input.txt')):
	sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w');

#left shift --- num*(2**k) --(k - shift)
# input = sys.stdin.readline

class Node:
	def __init__(self , data):
		self.data = data
		self.next = None
		self.prev = None
class Linkedlist:
	def __init__(self):
		self.head = None

	def push(self , data):
		new = Node(data) 
		new.next = self.head 
		if self.head:
			self.head.prev = new
		self.head = new 

	def p(self,order=None):
		t  = self.head 
		while t :
			print(t.data , end = ' ')
			l = t
			t = t.next
		if order == 'reverse' :
			print()
			while l :
				print(l.data , end = ' ')
				l = l.prev

	def insertafter(self ,prev,data):
		if prev:
			new = Node(data)
			new.next  = prev.next
			new.prev = prev
			prev.next = new
			if new.next :
				new.next.prev = new
		else:
			print("Doesn't exist")
	def append(self , data):
		new = Node(data)
		if self.head :
			l = self.head
			while l.next :
				l =l.next
			l.next = new
			new.prev = l
		else:
			self.head = new
			return




l  = Linkedlist()
l.append(102)
l.push(10)
l.push(103)
l.insertafter(l.head.next,105)
l.append(202)
l.append(1030)
l.p()



