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

for _ in range(*maps()):
	n , k = maps()
	d = {}
	L = []
	for __ in range(k):
		u , v = maps()
		if u > v:
			u,v = v , u
		d[u] = v
		d[v] = u
		L.append((u,v))

	free = []
	for i in range(1 , 2*n + 1):
		if i not in d:
			free.append(i)

	#there are exactly 2*(n-k) free points
	ans = 0
	for i in range(n-k):
		if free[i] < free[i+n-k]:
			L.append((free[i] , free[i+n-k]))
			#the chord which connects opposite points is the ideal chord (which can intersect more with more chords)

	L.sort()
	#can also use the intersection formula
	for i in range(n):
		for j in range(n):
			if L[i][0] < L[j][0] < L[i][1] < L[j][1]:
				ans+=1
	print(ans)
