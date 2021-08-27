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
def nCr(n, r): return fn.reduce(op.mul, range(n - r + 1, n + 1), 1) // mt.factorial(r)

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
	n,k = maps()
	a = sorted([*maps()])[::-1]
	w = sorted([*maps()])
	ii = k
	l = 0
	r = n-1
	ans = 0
	for i in range(k):
		if w[i] > 1:
			ii = i
			break
		ans += 2*a[l]
		l+=1
	for j in range(k-1 , ii-1 , -1):
		ans+=a[l]+a[r]
		r -=(w[j]-1)
		l +=1
	print(ans)





