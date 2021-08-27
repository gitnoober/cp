import os
import sys
import time
import math as mt
import itertools as it
import operator as op
import bisect as bs
import heapq as hp
import functools as fn
from collections import deque, defaultdict , OrderedDict, Counter, ChainMap , _chain
maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)
def nCr(n, r): return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceil(n, x): return (n + x - 1) // x


def lcm(x , y): return x * y // mt.gcd(x,y)


osi, oso = '/home/priyanshu/Documents/cp/input.txt', '/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
    sys.stdin = open(osi, 'r')
    sys.stdout = open(oso, 'w')

input = sys.stdin.readline

def maps(): return map(int, input().split())

#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!

r , c , n = maps()
arr = [[i for i in input().rstrip()] for _ in range(r)]
t = [(0,0) , (0,1) , (1 , 0) , (0 , -1 ) , (-1 , 0)]
if n ==1 :
	[print(''.join(i)) for i in arr] ,exit()
if n %2 ==0:
	[print('O'*c) for _ in range(r)],exit()
og = [i[:] for i in arr] ; X = (n-3)//2
for _ in range(2):
	ARR = [i[:] for i in arr]
	for i in range(r):
		for j in range(c):
			if arr[i][j] == 'O':
				for q ,w in t:
					x ,y = i+q , j+w
					if x >=0 and x < r and y >=0 and y < c:
						ARR[x][y] = '-1'

	arr = [['.' if x == '-1' else 'O' for x in i] for i in ARR]
	if X % 2 == 0:[print(''.join(i)) for i in arr] ,exit()

[print(''.join(i)) for i in arr]
