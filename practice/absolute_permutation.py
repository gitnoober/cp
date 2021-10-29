import os
import sys
import time
import math as mt
import pprint
import itertools as it
import operator as op
import bisect as bs
import functools as fn
from collections import deque, defaultdict , OrderedDict, Counter, ChainMap
maxx, localsys, mod = 1 << 60, 0, int(1e9 + 7)
def nCr(n, r): return reduce(mul, range(n - r + 1, n + 1), 1) // factorial(r)


def ceil(n, x): return (n + x - 1) // x


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
	if k == 0:
		print(*[*range(1 , n + 1)]) 
		continue

	if n % 2 or n%(2*k):
		print(-1) 
		continue

	perm , ok= [] , 1
	for i in range(1 , n+1):
		perm.append(i+k if ok&1 else i-k)
		if not i%k:
			ok^=1

	print(*perm)
