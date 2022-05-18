from os import path
import sys,time
# mod = int(1e9 + 7)
# import re
from math import ceil, floor,gcd,log,log2 ,factorial
from collections import * 
# from bisect import *
maxx = float('inf')
#----------------------------INPUT FUNCTIONS------------------------------------------#
I = lambda :int(sys.stdin.buffer.readline())
tup= lambda : map(int , sys.stdin.buffer.readline().split())
lint = lambda :[int(x) for x in sys.stdin.buffer.readline().split()]
S = lambda: sys.stdin.readline().replace('\n', '').strip()
def grid(r, c): return [lint() for i in range(r)]
stpr = lambda x : sys.stdout.write(f'{x}' + '\n')
star = lambda x: print(' '.join(map(str, x)))
localsys = 0
start_time = time.time()
if (path.exists('input.txt')):
	sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w');
#left shift --- num*(2**k) --(k - shift)
###########################EVEN SUBSEQUENCES##########################
def evensubs():
	for _ in range(I()):
		n = I()
		ls, se , ans  = lint() , set() , 0
		for i in ls:
			if i in se:
				ans+=2
				se.clear()
			else:
				se.add(i)
		print(n - ans)



###########################HORORSCOPE MATRIX(MULTISET PROBLEM)###########


def hororscope():
	for _ in range(I()):
	n , m = tup()
	ar = [lint() for _ in range(n)]
	count = defaultdict(lambda  : defaultdict(int))
	for  i in range(n):
		for j in range(m):
			count[i-j][ar[i][j]]+=1
	unique = sum((1 if len(x) == 1 else 0 for x in count.values()))
	for i in range(I()):
		x ,y ,v = tup()
		x , y = x-1 , y-1
		old = ar[x][y]
		if len(count[x-y]) == 1:
			unique-=1
		count[x-y][old] -=1
		if count[x-y][old] == 0 :
			del count[x-y][old]
		count[x-y][v]+=1
		if len(count[x-y]) == 1:
			unique+=1
		print('Yes') if len(count) == unique else print('No')
		










if localsys:
	print("\n\nTime Elased :",time.time() - start_time,"seconds")



