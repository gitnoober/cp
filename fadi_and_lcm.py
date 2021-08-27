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
nCr = lambda n, r :fn.reduce(op.mul, range(n - r + 1, n + 1), 1) // mt.factorial(r)

ceil = lambda a, b : (a+b-1)//b

lcm = lambda a, b: a * b // mt.gcd(a, b)

gcdm = lambda *args: reduce(mt.gcd, args, 0)

lcm = lambda a, b: a * b // mt.gcd(a, b)

lcmm = lambda *args: reduce(lcm, args, 1)


osi, oso = '/home/priyanshu/Documents/cp/input.txt', '/home/priyanshu/Documents/cp/output.txt'
if os.path.exists(osi):
    sys.stdin = open(osi, 'r')
    sys.stdout = open(oso, 'w')

input = sys.stdin.readline

def maps(): return map(int, input().split())

#   THINK ABOUT THE EDGE CASES ..........

#   DON'T SUBMIT UNLESS YOU ARE ABSOLUTELY SURE !!!!!

def prim(n):
	d = defaultdict(int)
	while not (n % 2):
		d[2]+=1
		n//=2
	for ii in range(3 , int(n**0.5)+ 1 , 2):
		while n % ii == 0:
			d[ii]+=1
			n//=ii
	if n > 1:d[n]+=1
	d[1] =1
	se = {pow(i,d[i]) for i in d}
	return se

X, = maps()
se , se_ , ans = prim(X) , set() , maxx

for r in range(1 , len(se)+1):
	se_.update((fn.reduce(op.mul,i) for i in it.combinations(se,r)))

for i in se_:
	for j in se_:
		if lcm(i,j)==X:
			tm = max(i,j)
			if tm < ans:
				ans , a , b = tm , i , j
print(a,b)

